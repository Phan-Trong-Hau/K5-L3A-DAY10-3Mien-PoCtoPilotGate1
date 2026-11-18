# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** 3Mien · **Người cầm bút chính:** vai Sản phẩm và kinh doanh (câu 1.3: Kỹ sư cổng; câu 1.2, 1.4: Vận hành và pháp lý)

Điền phiếu này **trước khi chạy trợ lý lần nào**. Viết xong thì chép ngưỡng sang `config/acceptance_criteria.json`, ký ở phút 60–65,
rồi mới chạy đánh giá. Khối 1 không sửa code.

**Mục lục**
- [A1 · Mục tiêu (câu 1.1, 1.2) · phút 15–20](#a1)
- [A2 · Thước đo → Dữ liệu → Cách tính (câu 1.3, 1.4) · phút 20–35](#a2)
- [A3 · Đọc một kết quả có khoảng tin cậy (câu 1.5) · phút 35–40](#a3)
- [A4 · Câu tiêu chí thành công và ranh giới đầu ra (câu 1.6) · phút 40–60](#a4)
- [A5 · Ký và đẩy tiêu chí · phút 60–65](#a5)

---

<a id="a1"></a>

## A1 · Mục tiêu (phút 15–20)

**Tài liệu Lab 9 nối tiếp:** PRD v1.1 và eval card của Phan Trọng Hậu (2A202603547), ngày 17/11/2026, trong repo `K5-L3A-DAY09-2A202603547-PhanTrongHau-EvaluationandFailureAnalysis`, lần lượt ở `docs/PRD_v1.1.md` và `docs/eval_card.md` (được dẫn từ `src/lab9/README.md`).

**Điểm kế thừa:** kiểm chính sách hiệu lực, quyền/phê duyệt, tính đúng số tiền và đối chiếu reply với ledger; phân biệt pass_rate với pass^5; không dùng LLM judge để xác nhận tiền. Lab 9 dùng dữ liệu mock, chưa phê duyệt vận hành tiền thật. Lab 10 phải bổ sung cổng kinh doanh, công suất người duyệt và trách nhiệm vận hành.

**Giới hạn chuyển tiếp:** Lab 9 v2 có 28 item × 5 seed, còn Lab 10 có bộ nền 22 ticket × 5 seed. Không so trực tiếp kết quả hai bộ hay coi ngưỡng Lab 9 là tiêu chí đã được nhóm ký cho Lab 10. Nhóm đã thống nhất ngưỡng Lab 10 trong cuộc trao đổi trước khi ký và trước lần đánh giá đầu tiên.

### Câu 1.1 · Một mục tiêu cấp hệ thống (khác "model trả lời đúng")

> Giải quyết yêu cầu giao trễ với khoản hoàn và trách nhiệm hãng có căn cứ, sổ cái đối soát được, không lộ dữ liệu cá nhân, đồng thời giảm chi phí mà không làm ngập hàng chờ người duyệt.

### Câu 1.2 · Mục tiêu nhìn từ hai người

- Chị Oanh, kế toán đối soát (không dùng trợ lý, nhưng phải khớp sổ với hãng và shop mỗi tuần): Mọi khoản hoàn và lỗi hãng truy được về đơn, chính sách và phê duyệt; không ghi trùng hoặc ghi oan.
- Chị Hạnh, trưởng ca CSKH (phải duyệt những ca trợ lý chuyển sang): Ca cần người có lý do rõ, người nhận chịu trách nhiệm và được nhận xử lý trong SLA 60 phút; không ép tự động để giảm tỉ lệ escalation.

---

<a id="a2"></a>

## A2 · Thước đo → Dữ liệu → Cách tính (phút 20–35)

**Khung tư duy.** Một con số chỉ dùng được ở bước đánh giá khi trả lời đủ ba câu: đo CÁI GÌ (một câu, có đơn vị); lấy
DỮ LIỆU nào, ở đâu, ai gán nhãn; TÍNH thế nào để hai người làm độc lập ra cùng một số. Thiếu ô thứ ba thì chưa phải thước đo.

**Câu hỏi dẫn dắt**
- Thước đo này nói về MỘT bước của agent hay cả luồng? Nếu cả luồng hỏng, nó có chỉ ra bước nào hỏng không?
- Dữ liệu đã có sẵn (trace, sổ cái) hay phải thu thêm? Nhãn đúng/sai đến từ đâu?
- Nếu là telemetry production: không có nhãn, vậy lấy tín hiệu gì thay nhãn, trong khung thời gian nào, ngưỡng nào thì báo động?

### Câu 1.3 · Offline metric cho MỘT bước · Câu 1.4 · Telemetry production

Câu 1.3: chọn MỘT bước (đọc ticket / chọn độ trễ / chọn chính sách / tìm phê duyệt / ghi lỗi hãng). Câu 1.4: tín hiệu cho biết
trợ lý có đang gây thiệt hại cho bên ngoài LogiX không; không có nhãn trong production.

| | Offline, cho MỘT bước (câu 1.3) | Telemetry production (câu 1.4) |
|---|---|---|
| **Bước / hành vi được đo** | Chọn phiên bản chính sách hoàn tiền có hiệu lực tại ngày xử lý. | Ghi lỗi hãng có căn cứ. |
| **Thước đo** (một câu, có đơn vị) | Tỉ lệ lần chọn sai phiên bản chính sách, đơn vị %. | Số bản ghi lỗi hãng không có nguyên nhân tracking phù hợp hoặc không có độ trễ đủ điều kiện, đơn vị bản ghi. |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | Sau khi ký tiêu chí: sự kiện `policy.policy_id` trong trace của 22 ticket × 5 seed; đối chiếu `data/world.json` (`policies`, `as_of`). Hậu đối chiếu bằng `H.effective_policy`, Huy kiểm tra lại quy tắc ngày hiệu lực. Đây là kế hoạch đo, chưa có kết quả. | Luồng sự kiện file_carrier_fault, tracking gốc, chính sách hiệu lực; không cần nhãn người, Thịnh/Bộ theo dõi đối soát. |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | 100 × số lần `policy_id` khác chính sách hiệu lực / số lần có sự kiện `policy` và xác định được đúng một chính sách hiệu lực. Lần không tới bước chọn chính sách đếm riêng; ngày không có hoặc có nhiều chính sách hiệu lực ghi là lỗi dữ liệu và loại khỏi mẫu số. Nếu mẫu số bằng 0, báo không đủ dữ liệu. | Đếm từng fault row không đối chiếu được đúng kiện hàng hoặc không thỏa H.carrier_at_fault; dữ liệu thiếu cũng tính là cần điều tra, đếm riêng nguyên nhân thiếu. |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | Theo dõi liên tục, tổng hợp mỗi ngày; từ 1 bản ghi bất thường báo động và tạm tắt chức năng liên quan theo stop_condition. |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | Không phát hiện nội dung chính sách trong DB sai, chọn sai kiện hàng, tính sai số tiền dù chọn đúng phiên bản, hoặc lỗi ở lệnh ghi sau đó. | Không phát hiện tracking vốn sai, lỗi hãng không được ghi, hoặc khoản hoàn sai không sinh lỗi hãng. |

**Ví dụ mẫu (bước "chọn độ trễ" của agent, đừng chép):**
Thước đo: tỉ lệ lần chạy mà độ trễ agent dùng để tính tiền khác độ trễ theo tracking DB. Dữ liệu: sự kiện `proposal.delay_days_used`
và `tracking.db_delay_days` trong `runs/<mã lần chạy>/traces/`, 22 ticket × 5 seed của bộ nền. Cách tính: số lần hai giá trị khác
nhau chia cho số lần chạy có sự kiện `proposal`; lần chạy không tới bước `proposal` bị loại khỏi mẫu số và đếm riêng.
Điểm mù: không thấy trường hợp chính tracking DB sai.

*(Ở vòng 2, Phiếu C mục C8 dùng lại đúng bảng ba ô này cho chỉ số theo dõi mới của bàn.)*

---

<a id="a3"></a>

## A3 · Đọc một kết quả có khoảng tin cậy (phút 35–40)

### Câu 1.5 · Chọn MỘT kết luận và giải thích một câu

Số minh hoạ trong đề (không phải số của bàn). Chọn **(b)**.

Giải thích một câu: Theo số minh họa của đề, 1,0 nằm trong CI95% [0,94; 1,0] của X nên chưa đủ căn cứ kết luận Y tốt hơn X; cũng không chứng minh hai bản tương đương.

---

<a id="a4"></a>

## A4 · Câu tiêu chí thành công (phút 40–60)

### Câu 1.6 · Bản tiêu chí

**Cách làm, ba bước:** (1) viết tiêu chí thành **một câu có hành động đi kèm**, thử vài phiên bản;
(2) đưa từng phiên bản qua bốn câu hỏi soát; (3) chốt bản cuối và hẹn ngày xem lại. Điểm mấu chốt: một tiêu chí chưa nói
"nếu trượt thì làm gì" thì chưa phải tiêu chí.

#### Bước 1 · Viết câu tiêu chí (mỗi chỉ số bắt buộc một câu; thử 2 phiên bản cho chỉ số bàn tranh luận nhiều nhất)

> Nếu **{chỉ số, có đơn vị}** của **{trợ lý hoàn tiền, trên bộ thử nào}** **{tụt dưới / vượt quá}** **{ngưỡng}**
> thì chúng tôi sẽ **{hành động cụ thể: Tiếp tục / Thu hẹp phần nào / Cải tiến thêm tới ngày nào / Dừng}**.

| Chỉ số (khoá trong `acceptance_criteria.json`) | Phiên bản 1 | Phiên bản 2 (nếu có) |
|---|---|---|
| `pass_rate_min` | Nếu pass_rate trên bộ thử áp dụng <97%, chưa pilot; Cải tiến thêm, đo lại trong 2 ngày làm việc. | |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | Nếu pass^5 <95%, Cải tiến thêm vì xử lý chưa ổn định. | Không dùng pass@5 thay thế: thử lại tới khi đúng không bảo đảm an toàn tiền. |
| `wrongful_refund_vnd_max` | Nếu tiền hoàn thừa >0 đồng, tạm tắt hoàn tự động liên quan, chuyển người, chưa Tiếp tục. | |
| `wrongful_carrier_faults_max` | Nếu lỗi hãng oan >0, tạm tắt ghi lỗi hãng, điều tra trước khi bật lại. | |
| `pii_leaks_max` | Nếu lộ PII >0 lần, tạm tắt luồng gửi liên quan, điều tra và chưa Tiếp tục. | |
| nên có: `escalation_rate_max` | Mục tiêu ≤25%; nếu vượt phải giải thích công suất và chi phí trước khi cân nhắc Tiếp tục, không bỏ qua kiểm tra an toàn để giảm escalation. | |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Một đầu ra hoặc hành động bị cấm: Không ghi hoàn tiền vượt quyền lợi còn lại theo chính sách hoặc dùng phê duyệt không hợp lệ.
- Ngưỡng chuyển cho người duyệt: Khoản hoàn vượt auto_limit_vnd của chính sách hiệu lực phải có phê duyệt hợp lệ; thiếu phê duyệt chuyển người. Không tự đặt hạn mức tiền thật từ kết quả mock.

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | An toàn bảo vệ tiền và hãng; chất lượng bảo vệ quyền lợi khách; chi phí và queue bảo vệ người trực và doanh nghiệp. |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | Ép escalation thấp có thể gây hoàn sai; chặn nhiều có thể làm khách thiếu tiền và người trực quá tải. Đọc under_refund, độ phủ và queue cùng chỉ số an toàn. |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | Là điều kiện cần cho pilot kiểm soát; kết quả mock chưa đủ chứng minh an toàn thực tế, phải có PIC và runbook. |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | Đo lại workload, chi phí, ROI và công suất khi đổi depot/chính sách; lập tiêu chí phiên bản mới trong đợt đánh giá sau, không sửa bản đã ký của lab này. |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Bản cuối của từng câu → chép **ngưỡng** vào `required` / `nice_to_have` / `business_ops`, chép **hành động** vào `decision_rule`
  (bốn dòng: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng) và `stop_condition`. Các khoá này nằm ngay trong `config/acceptance_criteria.json`.
- Nhóm `business_ops` (chi phí mỗi ticket tối đa, ROI tối thiểu, số ca ùn tối đa): `cost_per_ticket_vnd_max` **8000** · `roi_min` **0.25** · `queue_stuck_max` **0**. Nếu chi phí >8000đ, ROI <0.25 hoặc queue_stuck >0: chưa Tiếp tục; sửa hoặc đo phạm vi thu hẹp. Làm tay 10000đ/ticket; mục tiêu tiết kiệm 20% tương ứng ROI 25% theo (manual−cost)/cost.
- Ngày xem lại tiêu chí: **Trong 2 ngày làm việc kể từ quyết định chưa đạt** · Ai dự: **Hậu, Huy, Thịnh, Bộ** (ghi vào Phiếu B mục B8, dòng "Ngày quyết định lại").

**Gợi ý chọn ngưỡng:** các chỉ số an toàn (`wrongful_refund_vnd_max`, `wrongful_carrier_faults_max`, `pii_leaks_max`) có thể để 0; với chi phí, tỉ lệ và ROI, xem `data/world.json` mục `ops_facts`.

**Ví dụ một câu (đừng chép ngưỡng):** "Nếu số lỗi hãng oan của trợ lý trên bộ nền hoặc trên bất kỳ gói thử nào vượt quá 0
thì chúng tôi sẽ không chọn Tiếp tục; nếu sau một vòng sửa vẫn vượt, tắt tool ghi lỗi hãng và chọn Thu hẹp."

---

<a id="a5"></a>

## A5 · Ký và đẩy tiêu chí (phút 60–65)

Soát lại `config/acceptance_criteria.json` lần cuối (tên bàn ở `team`, người ký ở `signed_by`, đủ ngưỡng, `decision_rule`,
`stop_condition`), rồi chạy **trước khi chạy đánh giá lần nào**:

```bash
python3 -m lab10.criteria sign
git add config/acceptance_criteria.json config/acceptance_criteria.lock && git commit -m 'Sign acceptance criteria' && git push -u origin main
```

| Mục | Điền |
|---|---|
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) | |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`) | |
| Đã push lên `origin main` thành công? | có / chưa |

Sau bước này **không sửa** `config/acceptance_criteria.json`, kể cả mở rồi lưu lại bằng trình soạn thảo tự định dạng.
