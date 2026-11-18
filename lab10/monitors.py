"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
Một trial = {"ticket_id", "seed", "day", "status", "amount_vnd", "ticket", "events", "ledger", "faults", "outbound",
             "arrive_min", "warehouse", "cost_vnd", "review_kind", "queue_wait_min", "queue_stuck"}
  "day"            một ngày vận hành giả lập: các ticket cùng "day" và cùng "seed" chạy nối nhau trên cùng một sổ cái
  "arrive_min"     phút ticket tới trong ca (0..480)          "warehouse"   kho của đơn
  "cost_vnd"       tiền LLM + nền tảng đã tốn cho ticket      "review_kind" None / "escalated" (trợ lý chuyển người) /
  "queue_wait_min" số phút chờ người duyệt (None nếu không vào hàng chờ)     "recheck" (nhân viên tự kiểm lại)
Chỉ số có thể là kỹ thuật (tỉ lệ model đè số trong ticket lên DB), vận hành (số ca cần người trong giờ đông nhất),
hay kinh doanh (tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người).

lab10.grade kiểm: monitor chạy không lỗi, và giá trị trên gói sự cố khác giá trị trên bộ nền,
tức là monitor "sáng đèn" khi sự cố xảy ra.
"""


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


def max_review_wait_minutes(trials):
    """Longest observed review wait, including escalated and sampled tickets."""
    return max((t.get("queue_wait_min") or 0 for t in trials), default=0)


def policy_fail_open_rate(trials):
    """Fraction of tickets with an unsafe policy-check fallback proposal."""
    return sum(any(e.get("type") == "llm_fallback"
                   and e.get("purpose") == "policy_check"
                   and e.get("mode") == "fail_open"
                   for e in t.get("events", []))
               for t in trials) / max(1, len(trials))


MONITORS = {
    "max_review_wait_minutes": max_review_wait_minutes,
    "policy_fail_open_rate": policy_fail_open_rate,
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
}
STARTER_MONITORS = ("escalation_rate",)
