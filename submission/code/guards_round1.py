"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


def pre_guard(ctx):
    # B6 kỹ thuật: chỉ dùng phiên bản có hiệu lực, không tin cờ index_active.
    policies = ctx.tools.lookup_policies()
    active = [p for p in policies
              if p["effective_from"] <= ctx.as_of
              and (not p.get("effective_to") or ctx.as_of <= p["effective_to"])]
    if len(active) != 1:
        return Verdict.escalate("không xác định duy nhất chính sách có hiệu lực")
    return Verdict.allow(policy_id=active[0]["policy_id"])


def write_gate(ctx, action):
    tool = action.get("tool")
    if tool not in ("issue_refund", "file_carrier_fault"):
        return Verdict.allow()
    order = ctx.tools.lookup_order(action.get("order_id"))
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if order is None or policy is None:
        return Verdict.escalate("thiếu đơn hoặc chính sách để kiểm lệnh ghi")
    if (action.get("order_id") != ctx.ticket.get("order_id")
            or order["customer_id"] != ctx.ticket["customer_id"]):
        return Verdict.escalate("lệnh ghi không khớp đơn và chủ đơn của ticket")
    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    delay = H.db_delay_days(parcel, ctx.as_of)
    if tool == "issue_refund":
        # B6 kỹ thuật: quyền lợi phải tính từ DB; không đọc nhãn hay seed.
        if parcel.get("delay_cause") is None and delay > 0:
            return Verdict.escalate("thiếu nguyên nhân trễ trong tracking")
        entitled = H.entitlement_vnd(policy, order, delay, parcel.get("delay_cause"))
        paid = sum(r["amount_vnd"] for r in ctx.tools.ledger_rows(order_id=order["order_id"]))
        remaining = max(0, entitled - paid)
        if remaining == 0:
            return Verdict.deny("không còn quyền lợi hoàn theo tracking, chính sách và sổ cái")
        if (action.get("amount_vnd") != remaining
                or action.get("payer", "LOGIX") != "LOGIX"
                or action.get("basis", "policy") != "policy"):
            return Verdict.escalate("đề xuất hoàn không khớp quyền lợi còn lại hoặc căn cứ chính sách")
    else:
        # B6 pháp lý: xác minh đúng kiện, đúng hãng và nguyên nhân có ghi nhận.
        if not H.carrier_at_fault(policy, parcel, delay):
            return Verdict.deny("tracking không đủ căn cứ ghi lỗi hãng")
        if (action.get("parcel_id") != parcel["parcel_id"]
                or action.get("carrier_id") != parcel["carrier_id"]
                or action.get("driver_id") != parcel.get("driver_id")
                or action.get("delay_days") != delay):
            return Verdict.modify("ghi lỗi theo kiện và độ trễ thực trong tracking",
                                  parcel_id=parcel["parcel_id"], carrier_id=parcel["carrier_id"],
                                  driver_id=parcel.get("driver_id"), delay_days=delay)
    return Verdict.allow()
