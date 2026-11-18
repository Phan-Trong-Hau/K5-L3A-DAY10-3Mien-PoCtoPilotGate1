# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): `3Mien`
- Lớp: `L3A`
- Repo của bàn: `K5-L3A-DAY10-3Mien-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8):

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

Kỹ sư cổng; trưởng nhóm. Phụ trách cấu hình repo, test công khai, câu 1.3 (Phiếu A/A2); tiếp theo là lệnh đánh giá, trace, cổng và chỉ số theo dõi khi đủ điều kiện của từng mốc.

### Đóng góp cụ thể

Đã dùng Codex hỗ trợ điền bảng thành viên và phân vai, gắn remote upstream, cấu hình danh tính Git theo MSSV, chạy 13 test công khai (OK), và soạn thước đo offline cho bước chọn chính sách ở Phiếu A/A2. Sau khi cả nhóm xác nhận ngưỡng, đã ký tiêu chí ở commit 38883f6 và push trước baseline; chạy baseline, phân tích T-002@55, triển khai ba cổng ở guards.py, đo lại và chạy hai adhoc. Đã áp dụng cấu hình vận hành nhóm duyệt, chốt snapshot vòng 1 1c93c400, đo prepared 110/110 đúng. Nhóm đã chốt v1 Cải tiến thêm, hẹn quyết định lại 2026-11-20 (GMT+7); chưa nhận thẻ hay chạy grade.

### Bằng chứng

Commit `05587ec`: bảng thành viên và phân vai. Phiếu A/A2, câu 1.3: thước đo chọn phiên bản chính sách. Lệnh `python3 -m unittest discover -s tests`: 13 tests, OK. Baseline `R-base-before-20261118-150607-b45eeb`: hoàn thừa 20000đ, 1 lỗi hãng oan. Sau cổng `R-base-after-20261118-150649-f6305b`: 110/110 đúng, không hoàn thừa/lỗi oan/PII; 13 tests OK. Chi tiết Phiếu B/B0–B8; Codex hỗ trợ soạn bản đồ dữ liệu, HAZOP, checklist và runbook từ cấu hình nhóm duyệt; không ghi đây là kết quả diễn tập thực tế của từng thành viên. Prepared `R-base-prepared-20261118-151443-f76021`: 4456đ/ticket, ROI 1.24, queue_stuck=0.

### Exit ticket

_Chính thành viên viết một điều học được và một điều còn chưa chắc._

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
