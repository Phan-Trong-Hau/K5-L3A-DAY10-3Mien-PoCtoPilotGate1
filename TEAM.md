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

Đã dùng Codex hỗ trợ điền bảng thành viên và phân vai, gắn remote upstream, cấu hình danh tính Git theo MSSV, chạy 13 test công khai (OK), và soạn thước đo offline cho bước chọn chính sách ở Phiếu A/A2. Sau khi cả nhóm xác nhận ngưỡng, đã ký tiêu chí ở commit 38883f6 và push trước baseline; chạy baseline, phân tích T-002@55, triển khai ba cổng ở guards.py, đo lại và chạy hai adhoc. Đã áp dụng cấu hình vận hành nhóm duyệt, chốt snapshot vòng 1 1c93c400, đo prepared 110/110 đúng. Đề xuất v1 đang chờ nhóm duyệt; chưa nhận thẻ hay chạy grade.

### Bằng chứng

Commit `05587ec`: bảng thành viên và phân vai. Phiếu A/A2, câu 1.3: thước đo chọn phiên bản chính sách. Lệnh `python3 -m unittest discover -s tests`: 13 tests, OK. Baseline `R-base-before-20261118-150607-b45eeb`: hoàn thừa 20000đ, 1 lỗi hãng oan. Sau cổng `R-base-after-20261118-150649-f6305b`: 110/110 đúng, không hoàn thừa/lỗi oan/PII; 13 tests OK. Chi tiết Phiếu B/B0–B8; Codex hỗ trợ soạn bản đồ dữ liệu, HAZOP, checklist và runbook từ cấu hình nhóm duyệt; không ghi đây là kết quả diễn tập thực tế của từng thành viên. Prepared `R-base-prepared-20261118-151443-f76021`: 4456đ/ticket, ROI 1.24, queue_stuck=0.

### Exit ticket

_Chính thành viên viết một điều học được và một điều còn chưa chắc._

## BuiGiaHuy-2A202603525

### Phần việc phụ trách

Sản phẩm và kinh doanh.

### Đóng góp cụ thể

_Chính thành viên bổ sung sau khi thực hiện; ghi rõ phần việc có dùng AI._

### Bằng chứng

_Chính thành viên bổ sung mã commit, mã lần chạy hoặc dòng trong phiếu._

### Exit ticket

_Chính thành viên viết một điều học được và một điều còn chưa chắc._

## NgoDucThinh-2A202603548

### Phần việc phụ trách

Vận hành và pháp lý.

### Đóng góp cụ thể

_Chính thành viên bổ sung sau khi thực hiện; ghi rõ phần việc có dùng AI._

### Bằng chứng

_Chính thành viên bổ sung mã commit, mã lần chạy hoặc dòng trong phiếu._

### Exit ticket

_Chính thành viên viết một điều học được và một điều còn chưa chắc._

## DoDuyBo-2A202603591

### Phần việc phụ trách

Vận hành và pháp lý. Phụ trách Câu 1.2 (Phiếu A mục A1 - mục tiêu từ góc nhìn chị Oanh và chị Hạnh), cùng nhóm xây dựng tiêu chí rủi ro vận hành, HAZOP và quản lý runbook.

### Đóng góp cụ thể

Đã hoàn thành câu 1.2 trong Phiếu A mục A1: xác định rõ mục tiêu vận hành và đối soát từ góc nhìn của chị Oanh (Kế toán đối soát) và chị Hạnh (Trưởng ca CSKH), liên kết trực tiếp với các giới hạn thực tế trong `data/world.json` (`ops_limits`, `ops_facts`: SLA 60 phút, công suất 6 ca/giờ, trần ngân sách ngày 2.000.000đ). Có dùng trợ lý AI hỗ trợ rà soát dữ kiện và thuật ngữ.

### Bằng chứng

Phiếu A (`templates/form-a-criteria.md`), mục A1, Câu 1.2.

### Exit ticket

_Chính thành viên viết một điều học được và một điều còn chưa chắc._
