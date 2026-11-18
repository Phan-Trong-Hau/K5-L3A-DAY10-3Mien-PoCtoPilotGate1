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

Sản phẩm và kinh doanh. Phụ trách Khối 1 (mục tiêu hệ thống câu 1.1, đọc khoảng tin cậy câu 1.5, câu tiêu chí câu 1.6 và chốt ngưỡng `config/acceptance_criteria.json`), Khối 2A (bản đồ dữ liệu và phân tích drift câu 2.3), Khối 2B (cổng kinh doanh `business` câu 2.9 trong `config/operating_gates.json`), và Khối 3 Vòng 2 trên thẻ **S4** (cập nhật trần hoàn tự động ngày sale, cân bằng chi phí/ROI khi tăng người trực, điền Phiếu C và chốt quyết định Gate 1 v2).

### Đóng góp cụ thể

- **Vòng 1:** Cùng nhóm thảo luận, rà soát dữ liệu `data/world.json` và chốt bộ ngưỡng chấp nhận ở Khối 1 (`pass_rate_min = 0.97`, `pass_k_min = 0.95`, các chỉ số an toàn `= 0`, `escalation_rate_max = 0.25`, `cost_per_ticket_vnd_max = 8000`, `roi_min = 0.25`, `queue_stuck_max = 0`) trước khi ký ở commit `38883f6`. Soạn thảo và đối chiếu Bản đồ dữ liệu + concept drift `REFUND-v3` → `REFUND-v4` ngày `2026-12-01` (Phiếu B mục B3) và 4 cổng kinh doanh ở mục B7.4; đồng bộ theo bản chốt Vòng 1 của nhóm ở commit `8a38bca` (`snapshot 1c93c400`, quyết định `v1 = Cải tiến thêm`).
- **Vòng 2 (Thẻ S4):**
  - Phân tích đánh đổi chi phí – ROI – công suất ca trực trên gói S4 khi chuyển từ `1` người (`10` ca ùn, chờ `128.0` phút) lên `2` người (`7.409đ/ticket ≤ 8.000đ`, `ROI = 0.35 ≥ 0.25`, `0` ca ùn, chờ `38.0` phút) so với `3` người (`8.140đ/ticket > 8.000đ`, `ROI = 0.23 < 0.25` — vi phạm ngưỡng đã ký).
  - Cập nhật `config/operating_gates.json`: điều chỉnh `business.daily_refund_cap_vnd = 300000` (khớp trần ngày sale 11.11 của Finance trong `incidents/S4/world_patch.json`) và phối hợp tăng `operations.reviewers_on_shift = 2`, `review_capacity_per_hour = 12`.
  - Hoàn thiện các phần kinh doanh/vận hành/phân tích trong Phiếu C (`templates/form-c-incident.md` mục `C0, C1, C4, C5, C6, C7, C9, C10, C11, C12`), cập nhật `submission/submission.json`, và chốt quyết định **v2 = Cải tiến thêm** cùng 3 dòng bắt buộc dù `grade` đạt `PASS-VISIBLE` (vì `S4 escalation_rate = 0.5317 > 0.25` và `base kho ? = 10.359đ > 10.000đ`).
- **Sử dụng AI:** Có sử dụng trợ lý AI để đọc hiểu đề bài, mô phỏng phương án số người trực (`1..4` người), rà soát `data/world.json` và `incidents/S4/world_patch.json`, soạn thảo nội dung Phiếu A/B/C và kiểm tra tính nhất quán bài nộp.

### Bằng chứng

Commit ký tiêu chí `38883f6` (hash `5c491d8c`); Phiếu A (`templates/form-a-criteria.md`) mục A1/A3/A4; Phiếu B (`templates/form-b-evaluation-gates.md`) mục B3, B7.4 và B8 (`v1 = Cải tiến thêm`); `config/operating_gates.json` (`daily_refund_cap_vnd = 300000`, `reviewers_on_shift = 2`, `review_capacity_per_hour = 12`); Phiếu C (`templates/form-c-incident.md`) mục C0–C12; lần chạy `R-S4-after-20261118-171004-7810a2`, `R-base-after-20261118-171005-7810a2` và `R-S4-grade-20261118-171005-7810a2` (`PASS-VISIBLE`); `submission/submission.json`.

### Exit ticket

- **Một điều học được:** Đặt cổng phòng ngừa ở tầng kỹ thuật (`write_gate` chặn `fail_open`) giúp triệt tiêu hoàn toàn hoàn thừa và phạt oan hãng, nhưng trong sản phẩm AI thực tế thì nút thắt kinh doanh & vận hành (trần ngân sách ngày sale bị siết bất ngờ và tải hàng chờ giờ cao điểm vượt công suất người duyệt) vẫn đủ làm hệ thống vỡ SLA nếu không thiết kế đồng bộ cả code, con số cấu hình và quy trình trực ca.
- **Một điều còn chưa chắc:** Trên dữ liệu thật ngoài production, tỉ lệ `escalation_rate` vào ngày sale (hiện `0.5317` trên S4) nếu kéo dài hoặc lượng ticket tăng quá `3x` (> 12 ca/giờ) sẽ đòi hỏi lọc sớm ca `DAMAGED`/`NOT_RECEIVED` và `kho ?` — chưa chắc ngưỡng `review_sampling_pct = 10%` và `decision_note` trong thực tế có giữ được tốc độ duyệt `0,4 ca` (4 phút/ca) như mô phỏng hay không.

## NgoDucThinh-2A202603548

### Phần việc phụ trách

Vận hành và pháp lý. Phụ trách Câu 1.4 (Phiếu A, mục A2 - Telemetry production), góp ý Pre-mortem góc nhìn Vận hành & Pháp lý (Phiếu B, mục B6, Câu 2.5), rào chắn pháp lý (`config/operating_gates.json` mục `legal`) và Runbook phần 1–3 + Giờ cao điểm (Phiếu B, mục B7.5–B7.6); ở Vòng 2 (thẻ S4) phụ trách bổ sung B7.6 sau S4 và hoàn thiện Phiếu C mục C4 (HAZOP S4), C6 (Fault tree trước sửa), C9 (Fault tree sau sửa) và C11 (Runbook 4–5).

### Đóng góp cụ thể

- **Vòng 1:** Hoàn thành **Câu 1.4 (Phiếu A, mục A2)** thiết kế telemetry production cho `file_carrier_fault` + `notify_carrier` (tỉ lệ khiếu nại từ hãng qua `NV-OANH`, cửa sổ 24h & 7 ngày theo `suspend_after_strikes_7d = 3`); kiểm tra nhất quán giữa Câu 1.4 với Câu 1.2, 1.6 và `acceptance_criteria.json`. Tham gia bổ sung góc nhìn Vận hành & Pháp lý ở **Pre-mortem (Câu 2.5, mục B6)** và soạn rào chắn `legal` + **Runbook 1–3 & Giờ cao điểm (Câu 2.10, mục B7.5–B7.6)**, đồng bộ với bản chốt vòng 1 của nhóm.
- **Vòng 2 (thẻ S4):** . Hoàn thành **C4 (HAZOP S4)**, **C6 (Fault tree trước sửa)**, **C9 (Fault tree sau sửa)** và **C11 (Runbook 4 & Runbook 5)** trên `templates/form-c-incident.md` bám sát dữ kiện `incidents/S4/world_patch.json` và report các mốc `prepared` / `after`.
.

### Bằng chứng

- Commit `707c833` (`cau 1.4`), `6908bae` (merge Phiếu A), `13c2952` (`C4&C6`), `3c84494`.
- Phiếu A (`templates/form-a-criteria.md`), mục A2, Câu 1.4 (cột Telemetry production).
- Phiếu B (`templates/form-b-evaluation-gates.md`), mục B6 (Câu 2.5) và mục B7.5–B7.6 (Câu 2.10, gồm bổ sung sau S4); `config/operating_gates.round1.json` mục `legal` (bản chốt vòng 1 ở commit `4f6f5b6` / `8a38bca`).
- Phiếu C (`templates/form-c-incident.md`), mục C4, C6, C9 và C11 (Runbook 4–5) gắn với mã lần chạy `R-S4-prepared-20261118-171006-7810a2` và `R-S4-after-20261118-171006-7810a2` (`R-S4-grade-20261118-171005-7810a2`).

### Exit ticket

- **Một điều học được:** Cách dùng HAZOP (đặc biệt guideword `INCAPABLE`) và Fault tree đa tầng để thấy rằng cổng code (`guards.py`) chỉ chặn ghi sai chứ không tự giải quyết nút thắt vận hành (`6 ca/giờ/người`) và trần ngân sách ngày sale (`300.000đ`); cần phối hợp đồng bộ cả con số (`reviewers_on_shift = 2`), runbook thu hẹp phạm vi và monitor (`policy_fail_open_rate`, `max_review_wait_minutes`).
- **Một điều còn chưa chắc:** Với tải thực tế ngoài mock ở ngày sale lớn (nếu dồn hơn `12 ca/giờ` hoặc tỉ lệ 429 thật cao hơn `60%`), liệu việc thu hẹp `pilot_scope` theo kho trong vòng 15 phút có kịp ngăn `queue_stuck` trước khi vượt SLA 60 phút hay không, và độ trễ phản hồi khiếu nại thực tế từ hãng vận chuyển (`NV-OANH`) là bao lâu.

## DoDuyBo-2A202603591

### Phần việc phụ trách

Vận hành và pháp lý. Phụ trách Câu 1.2 (Phiếu A mục A1 - mục tiêu từ góc nhìn chị Oanh và chị Hạnh); Câu 2.4 (Phiếu B mục B4 HAZOP vòng 1, B5 checklist); Câu 2.10 phần 1 (`operations.pic`, `reviewers_on_shift`, `review_capacity_per_hour`, `max_queue_wait_minutes`); Câu 3.1/C4 (HAZOP của thẻ sự cố vòng 2); Câu 3.3 (Phiếu C mục C5, giả định môi trường); rà soát cổng `legal` trên S4; C10 risk register; C11 checklist dòng 1 và 8.

### Đóng góp cụ thể

Đã hoàn thành câu 1.2 trong Phiếu A mục A1: xác định rõ mục tiêu vận hành và đối soát từ góc nhìn của chị Oanh (Kế toán đối soát) và chị Hạnh (Trưởng ca CSKH), liên kết trực tiếp với các giới hạn thực tế trong `data/world.json` (`ops_limits`, `ops_facts`: SLA 60 phút, công suất 6 ca/giờ, trần ngân sách ngày 2.000.000đ). Có dùng trợ lý AI hỗ trợ rà soát dữ kiện và thuật ngữ.

Câu 2.4: rà soát HAZOP vòng 1 trên `issue_refund` (5 dòng kỹ thuật, có nhánh chưa thấy trên trace: approval INVALID, ghi lặp PERTURBED, policy_check INCAPABLE) và 3 dòng ngoài kỹ thuật (người duyệt, ngân sách, dữ liệu gửi hãng); đối chiếu cột "Hiện có gì ngăn" với code thật (`lab10/guards.py`, `lab10/tools.py`). Ghi nhận hai khoảng hở chuyển sang vòng 2: guard chưa kiểm trần 300.000đ/khách/ngày và 2 lỗi/hãng/ngày trong `ops_limits`; trần ngày của host chỉ tính khoản không có `approval_id`, nên một mã duyệt không hợp lệ cũng đi vòng qua trần.

Câu 2.10 phần 1: đặt `operations.pic = NV-TUNG` (người giữ công tắc trong `staff`), `reviewers_on_shift = 1` (`ops_facts.default_reviewers_on_shift`), `review_capacity_per_hour = 6` (= 1 người × 6 ca/giờ, không vượt sức thật), `max_queue_wait_minutes = 60` (= `ops_limits.review_sla_minutes`). Có dùng trợ lý AI để đối chiếu số với `data/world.json`.

Câu 3.1/C4 (thẻ S4): hoàn thiện HAZOP của thẻ (7 dòng sau khi gộp với dòng `llm.confirm → write_retry` của Huy) trên `issue_refund`, `file_carrier_fault`, LLM `policy_check` và người duyệt. Sửa các điểm sai so với dữ kiện: S4-07 không gặp lỗi LLM (chuyển người vì DAMAGED); VNX bị đình chỉ sau 10 lỗi/7 ngày, không phải 3; dòng đánh dấu "chưa thấy trên trace" thực ra đã thấy ở S4-08@11. Thêm hai dòng mới: (1) dây chuyền LLM 429 → cổng chuyển người → hàng chờ ùn (seed 11: 8 ca chuyển sau fallback, 10 ca ùn với 1 người, chờ 38 phút với 2 người; seed 22: 2 ca, 5 ca ùn với 1 người, chờ 18 phút với 2 người); (2) nhánh chưa thấy trên trace: cổng không đếm lỗi/hãng/ngày, MKD, DNB, LGX, GHSH chạm đúng trần 2/ngày, GHSH và DNB bị đình chỉ sau 3 lỗi/7 ngày. Có dùng trợ lý AI để chạy lại `evaluate("S4", "after")` trong Python (không ghi journal) và đối chiếu số.

Câu 3.3 (C5): giả định ticket tới rải đều và các thành phần bên ngoài hỏng độc lập. Trên S4, 30/41 ticket dồn vào một giờ; LLM 429 trùng đúng giờ đó; Finance hạ trần ngày sale xuống 300.000đ. Thêm 2 người trực chỉ dời giả định thành "tải không vượt 12 ca/giờ".

Rà soát `legal` trên S4: lỗi hãng oan base 27 → prepared 0 → after 0; `pii_leaks = 0` cả ba mốc; payload gửi hãng chỉ có `order_id`, `parcel_id`, `district`, `delay_days`. Ghi rõ S4 không thử PII (base cũng 0), nên chưa có bằng chứng cho cổng `pii_fields_blocked_to_third_party` trên thẻ này.

C10: thêm 2 dòng risk register (dây chuyền LLM 429 → hàng chờ, PIC Phan Trọng Hậu; trần ngân sách đổi theo ngày, PIC Bùi Gia Huy), gộp với 2 dòng của Huy. C11: checklist dòng 1 (chất lượng) và dòng 8 (con người, pháp lý; còn Chưa vì thiếu cổng 2 lỗi/hãng/ngày), gộp với dòng 5, 6, 7, 9 của Huy/Thịnh. Có dùng trợ lý AI để đối chiếu số và gộp bản của nhóm.

### Bằng chứng

Phiếu A (`templates/form-a-criteria.md`), mục A1, Câu 1.2. Phiếu B mục B4, B5 (PIC dòng 8). Phiếu C mục C4, C5 (câu 3.3), C10, C11. Số khớp report `R-S4-prepared-20261118-171006-7810a2` (1 người: 10 ca ùn, chờ 128 phút) và `R-S4-after-20261118-171006-7810a2` (2 người: 0 ca ùn, chờ 38 phút, hoàn tự động tối đa 294.000đ/ngày, 0 lỗi hãng oan, 0 PII). `config/operating_gates.json` mục `operations`, đã chốt trong snapshot vòng 1 `1c93c400`. Prepared `R-base-prepared-20261118-151443-f76021`: `ops.queue` 1 người, 6 ca/giờ, SLA 60, chờ tối đa 0 phút, `stuck = 0`, `ops.violations` rỗng; 13 tests OK.

### Exit ticket

**Một điều học được:** Cổng "an toàn" ở một tầng có thể đẩy tác hại sang tầng khác. Trên S4, cổng vòng 1 chặn đúng các đề xuất `fail_open` khi LLM trả 429 (hoàn thừa 160.000đ → 0đ, lỗi hãng oan 27 → 0), nhưng mỗi ca bị chặn lại thành một ca chờ người duyệt, đúng vào giờ cao điểm. Ngày có nhiều fallback nhất cũng là ngày hàng chờ dài nhất (seed 11: 8 ca chuyển người, chờ 128 phút với 1 người trực). Vì vậy khi làm HAZOP, phải hỏi cả "ai nhận phần việc mà cổng đẩy sang", không chỉ "cổng có chặn được không".

**Một điều còn chưa chắc:** 2 người trực (12 ca/giờ) đủ cho S4 trong mô phỏng (0 ca ùn, chờ 38 phút), nhưng mình chưa chắc nó đủ ngoài thực tế: tải ngày sale thật có thể dồn hơn 12 ca/giờ, và tỉ lệ 429 thật của nhà cung cấp LLM chưa đo được. Mình cũng chưa chắc nên chặn lỗi thứ 3 của một hãng trong ngày bằng code (`write_gate` đếm `fault_rows`) hay bằng quy trình đối soát của Oanh, vì bộ thử hôm nay chưa có ca nào vượt quá 2 lỗi/hãng/ngày.

_Bản nháp viết cùng trợ lý AI, dựa trên số liệu thật trong Phiếu C; chính thành viên đã đọc và chỉnh lại._
