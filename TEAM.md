# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): `3Mien`
- Lớp: `L3A`
- Repo của bàn: `K5-L3A-DAY10-3Mien-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): **S4**

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Phan Trọng Hậu | 2A202603547 | Kỹ sư cổng | Có |
|   2 | Bùi Gia Huy | 2A202603525 | Sản phẩm và kinh doanh | |
|   3 | Ngô Đức Thịnh | 2A202603548 | Vận hành và pháp lý | |
|   4 | Đỗ Duy Bộ | 2A202603591 | Vận hành và pháp lý | |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## PhanTrongHau-2A202603547

### Phần việc phụ trách

**Vai:** Kỹ sư cổng; trưởng nhóm. Phụ trách cấu hình repo và Git, bảng thành viên; câu 1.3 (Phiếu A/A2); câu 2.1–2.2 (đánh giá, trace và soát lỗi); câu 2.6–2.8 (cổng, tránh rò rỉ dữ liệu đánh giá, behavioral test); chốt bản kỹ thuật vòng 1 và cung cấp bằng chứng cho quyết định chung. Ở vòng 2 phụ trách trace, sửa cổng, thêm monitor và kiểm regression khi có thẻ được giao.

Ngưỡng chấp nhận, cấu hình ngân sách/nhân sự/pháp lý và quyết định v1/v2 là nội dung nhóm thống nhất hoặc thành viên phụ trách chốt; không coi đó là quyết định cá nhân của kỹ sư cổng.

### Đóng góp cụ thể

- Chuẩn bị repo: gắn upstream tới repo mẫu, cấu hình Git theo MSSV và email giả, điền bảng bốn thành viên/phân vai và push lên origin/main.
- Đọc README, CHECKPOINTS, RUBRIC, RULES, SUBMISSION; đối chiếu PRD v1.1 và eval card Lab 9. Thiết kế thước đo offline về chọn đúng phiên bản chính sách theo ngày hiệu lực tại Phiếu A/A2.
- Sau khi cả nhóm xác nhận tiêu chí, thực hiện ký và push tiêu chí trước baseline; giữ nguyên file tiêu chí và hash sau ký.
- Đo baseline 22 ticket × 5 seed. Phân tích `T-002@55`: trace ghi đè độ trễ tracking từ 2 thành 5 ngày, dẫn tới hoàn thừa 20000đ và ghi một lỗi oan cho VNX. Phân biệt lỗi quan sát được với rủi ro chưa kiểm chứng.
- Triển khai ba cổng chung trong `lab10/guards.py`: ghim chính sách hiệu lực; kiểm chủ đơn, quyền lợi còn lại từ tracking/chính sách/ledger trước hoàn; kiểm đúng kiện và căn cứ ghi lỗi hãng. Không phân nhánh theo mã ticket, seed hoặc nhãn kết quả.
- Chạy lại bộ nền, 13 test công khai và hai ticket adhoc. Bộ nền sau cổng đạt 110/110 lần chạy, không làm hỏng 109 ca trước đúng. Hai adhoc ở seed 11 không sinh hoàn/lỗi hãng trên đơn chưa đủ điều kiện; extractor không tin lời khai ở hai lần này, nên không coi chúng là bằng chứng riêng cho nhánh model_override.
- Áp dụng cấu hình vận hành sau khi nhóm duyệt; chốt bản kỹ thuật prepared với hash `1c93c400`. Lưu báo cáo và nhật ký thật vào `submission/runs/` để bàn giao.
- Cung cấp số liệu cho nhóm chốt v1 **Cải tiến thêm**: dù tổng thể đạt, nhóm kho không xác định tốn 10359đ/ticket và còn thiếu kiểm chứng quyền phê duyệt, tải đỉnh. Hẹn đánh giá lại 2026-11-20 (GMT+7).

**Sử dụng AI:** Codex hỗ trợ đọc repo, soạn thước đo/báo cáo, triển khai cổng, chạy lệnh và quản lý Git. Trong phiên làm việc, Codex cũng đã hỗ trợ soạn bản đồ dữ liệu, HAZOP, checklist, runbook và áp dụng cấu hình được nhóm duyệt; các phần nghiệp vụ này cần thành viên phụ trách rà soát. Không ghi nhận việc soạn tài liệu là một cuộc diễn tập vận hành hay phê duyệt release đã xảy ra.

### Bằng chứng

| Nội dung | Commit / file / lần chạy | Kết quả |
|---|---|---|
| Bảng thành viên, phân vai | `05587ec`, `TEAM.md` | Bốn thành viên, Hậu là trưởng nhóm và kỹ sư cổng |
| Thước đo và nguồn Lab 9 | `64ea0d1`, Phiếu A/A2 | Metric chọn chính sách, nguồn PRD/eval card |
| Ký trước khi đo | `38883f6`, đã push qua `6908bae`; Phiếu A/A5 | Hash tiêu chí `5c491d8c`, kiểm verify còn nguyên |
| Baseline | `R-base-before-20261118-150607-b45eeb` | pass_rate 0.9909; pass^5 0.9545; hoàn thừa 20000đ; lỗi hãng oan 1 |
| Cổng và kiểm lại | `1f1a5a0`; `R-base-after-20261118-150649-f6305b`; Phiếu B/B1–B2, B7.1–B7.3 | pass_rate/pass^5=1.0; hoàn thừa/lỗi oan/PII=0; 13 tests OK |
| Cấu hình nhóm duyệt | `R-base-after-20261118-151304-f76021` | 4456đ/ticket; ROI 1.24; escalation 22.73%; review_rate kể cả kiểm mẫu 27.27% |
| Chốt kỹ thuật vòng 1 | `4f6f5b6`; `R-base-prepared-20261118-151443-f76021`; snapshot `1c93c400` | 110/110 đúng; CI95% [1.0;1.0]; queue_stuck=0; độ phủ 100% |
| Quyết định chung v1 | `8a38bca`, Phiếu B/B8 | Nhóm xác nhận Cải tiến thêm; chưa cho pilot khách thật |

Các báo cáo tương ứng và `journal.jsonl` nằm trong `submission/runs/`. Kết quả là đo trên dữ liệu mock; không suy rộng thành bảo đảm an toàn production hoặc kết quả test ẩn.

**Tiến độ vòng 2 — S4:** Đã nhập S4 từ repo `minhhai203/K5_L3_Day10_PoC-to-Pilot_Gate1_cards`, commit `997c81b`; đo trước sửa, trace S4-07, S4-08 (seed11/22), S4-02 và hàng chờ S4-33. Bổ sung guard đọc trần ngày từ ops_limits và hai monitor không dùng nhãn. Sau sửa S4 205/205 đúng, max hoàn tự động294000đ≤300000đ; bộ nền110/110, 13 tests OK. Grade `R-S4-grade-20261118-163826-906777`: integrity/criteria/regression/monitor đạt, visible chưa đạt vì vẫn10 ca ùn, chờ128 phút. Chi phí S4 6677đ/ticket, ROI0.50. Không đổi cấu hình nhân sự/phạm vi, không tự chốt v2; bàn giao nhóm xử lý vận hành. Chi tiết Phiếu C/C0–C2, C7–C8 và đầu vào kỹ thuật C6/C9. Có dùng Codex hỗ trợ triển khai, đo và soạn bằng chứng.

### Exit ticket

_Chưa điền: Hậu tự xác nhận một điều học được và một điều còn chưa chắc sau khi đọc kết quả; không tự ghi trải nghiệm học tập thay thành viên._

## BuiGiaHuy-2A202603525

### Phần việc phụ trách

Sản phẩm và kinh doanh. Phụ trách Khối 1 (mục tiêu hệ thống câu 1.1, đọc khoảng tin cậy câu 1.5, câu tiêu chí câu 1.6 và chốt ngưỡng `config/acceptance_criteria.json`), Khối 2A (bản đồ dữ liệu và phân tích drift câu 2.3), Khối 2B (cổng kinh doanh `business` câu 2.9 trong `config/operating_gates.json`), và cùng nhóm chốt quyết định Gate 1 v1/v2.

### Đóng góp cụ thể

- Cùng nhóm thảo luận, rà soát dữ liệu `data/world.json` và chốt bộ ngưỡng chấp nhận ở Khối 1 (`pass_rate_min = 0.97`, `pass_k_min = 0.95`, các chỉ số an toàn `= 0`, `escalation_rate_max = 0.25`, `cost_per_ticket_vnd_max = 8000`, `roi_min = 0.25`, `queue_stuck_max = 0`) trước khi ký ở commit `38883f6`.
- Soạn thảo và đối chiếu phương án cho Bản đồ dữ liệu + concept drift `REFUND-v3` → `REFUND-v4` ngày `2026-12-01` (Phiếu B mục B3) và 4 cổng kinh doanh (`daily_refund_cap_vnd = 2000000`, `cost_budget_per_ticket_vnd = 1500`, `pilot_scope` all 100%, `roi_min = 0.25` ở mục B7.4); đồng bộ theo bản chốt Vòng 1 của nhóm ở commit `8a38bca` (`snapshot 1c93c400`, quyết định `v1 = Cải tiến thêm`).
- Có sử dụng trợ lý AI để đọc hiểu đề bài, rà soát `data/world.json`, kiểm tra công thức chi phí/ROI và soạn thảo nội dung rà soát cho Phiếu A/B.

### Bằng chứng

Commit ký tiêu chí `38883f6` (hash `5c491d8c`); Phiếu A (`templates/form-a-criteria.md`) mục A1/A3/A4; Phiếu B (`templates/form-b-evaluation-gates.md`) mục B3, B7.4 và B8 (chốt v1 **Cải tiến thêm** với `R-base-after-20261118-151304-f76021` và `R-base-prepared-20261118-151443-f76021`); khối `"business"` trong `config/operating_gates.json`.

### Exit ticket

_Chính thành viên viết một điều học được và một điều còn chưa chắc._

## NgoDucThinh-2A202603548

### Phần việc phụ trách

Vận hành và pháp lý. Phụ trách Câu 1.4 (Phiếu A, mục A2 - Telemetry production), góp ý Pre-mortem góc nhìn Vận hành & Pháp lý (Phiếu B, mục B6, Câu 2.5), rào chắn pháp lý (`config/operating_gates.json` mục `legal`) và Runbook phần 1–3 + Giờ cao điểm (Phiếu B, mục B7.5–B7.6); tiếp theo là phần việc Vận hành & Pháp lý ở Khối 3 (Phiếu C).

### Đóng góp cụ thể

- Đã hoàn thành **Câu 1.4 (Phiếu A, mục A2)**: thiết kế chỉ số telemetry production cho luồng `file_carrier_fault` + `notify_carrier` (tỉ lệ biên bản ghi lỗi bị hãng phản đối/đối soát lại qua `NV-OANH`, cửa sổ trượt 24h & 7 ngày theo `suspend_after_strikes_7d = 3`, kèm điểm mù tín hiệu).
- Kiểm tra tính nhất quán giữa Câu 1.4 với Câu 1.2, 1.6 và `config/acceptance_criteria.json`.
- Tham gia bổ sung góc nhìn Vận hành & Pháp lý ở **Pre-mortem (Câu 2.5, mục B6)** và soạn phương án rào chắn pháp lý (`legal.pii_fields_blocked_to_third_party`, `legal.carrier_fault_requires_recorded_cause`) cùng **Runbook 1–3 & Giờ cao điểm (Câu 2.10, mục B7.5–B7.6)**, đồng bộ với bản chốt vòng 1 của nhóm.
- Có sử dụng trợ lý AI hỗ trợ rà soát dữ kiện `data/world.json`, kiểm tra cấu trúc phiếu và xử lý conflict Git khi đồng bộ bài nhóm.

### Bằng chứng

- Commit `707c833` (`cau 1.4`) và merge commit `6908bae`.
- Phiếu A (`templates/form-a-criteria.md`), mục A2, Câu 1.4 (cột Telemetry production).
- Phiếu B (`templates/form-b-evaluation-gates.md`), mục B6 (Câu 2.5) và mục B7.5–B7.6 (Câu 2.10); `config/operating_gates.round1.json` mục `legal` (bản chốt vòng 1 ở commit `4f6f5b6` / `8a38bca`).

### Exit ticket


## DoDuyBo-2A202603591

### Phần việc phụ trách

Vận hành và pháp lý. Phụ trách Câu 1.2 (Phiếu A mục A1 - mục tiêu từ góc nhìn chị Oanh và chị Hạnh); Câu 2.4 (Phiếu B mục B4 HAZOP vòng 1, B5 checklist); Câu 2.10 phần 1 (`operations.pic`, `reviewers_on_shift`, `review_capacity_per_hour`, `max_queue_wait_minutes`); Câu 3.1/C4 (HAZOP của thẻ sự cố vòng 2).

### Đóng góp cụ thể

Đã hoàn thành câu 1.2 trong Phiếu A mục A1: xác định rõ mục tiêu vận hành và đối soát từ góc nhìn của chị Oanh (Kế toán đối soát) và chị Hạnh (Trưởng ca CSKH), liên kết trực tiếp với các giới hạn thực tế trong `data/world.json` (`ops_limits`, `ops_facts`: SLA 60 phút, công suất 6 ca/giờ, trần ngân sách ngày 2.000.000đ). Có dùng trợ lý AI hỗ trợ rà soát dữ kiện và thuật ngữ.

Câu 2.4: rà soát HAZOP vòng 1 trên `issue_refund` (5 dòng kỹ thuật, có nhánh chưa thấy trên trace: approval INVALID, ghi lặp PERTURBED, policy_check INCAPABLE) và 3 dòng ngoài kỹ thuật (người duyệt, ngân sách, dữ liệu gửi hãng); đối chiếu cột "Hiện có gì ngăn" với code thật (`lab10/guards.py`, `lab10/tools.py`). Ghi nhận hai khoảng hở chuyển sang vòng 2: guard chưa kiểm trần 300.000đ/khách/ngày và 2 lỗi/hãng/ngày trong `ops_limits`; trần ngày của host chỉ tính khoản không có `approval_id`, nên một mã duyệt không hợp lệ cũng đi vòng qua trần.

Câu 2.10 phần 1: đặt `operations.pic = NV-TUNG` (người giữ công tắc trong `staff`), `reviewers_on_shift = 1` (`ops_facts.default_reviewers_on_shift`), `review_capacity_per_hour = 6` (= 1 người × 6 ca/giờ, không vượt sức thật), `max_queue_wait_minutes = 60` (= `ops_limits.review_sla_minutes`). Có dùng trợ lý AI để đối chiếu số với `data/world.json`.

### Bằng chứng

Phiếu A (`templates/form-a-criteria.md`), mục A1, Câu 1.2. Phiếu B mục B4, B5 (PIC dòng 8). `config/operating_gates.json` mục `operations`, đã chốt trong snapshot vòng 1 `1c93c400`. Prepared `R-base-prepared-20261118-151443-f76021`: `ops.queue` 1 người, 6 ca/giờ, SLA 60, chờ tối đa 0 phút, `stuck = 0`, `ops.violations` rỗng; 13 tests OK.

### Exit ticket

_Chính thành viên viết một điều học được và một điều còn chưa chắc._
