---
name: ai-review-maker
description: Cố vấn kiến trúc và code reviewer cho firmware STM32 + FreeRTOS (C/C++, Keil MDK, Barr C) trong dự án common module DLMS cho smart meter. Dùng skill này khi người dùng yêu cầu (1) tư vấn/cải thiện thiết kế một luồng code (luồng A) của common module DLMS, hoặc (2) review code đã implement trên nhánh git hiện tại (before = merge-base, after = HEAD). Kích hoạt cả khi người dùng nhắc đến DLMS, smart meter, common module, API/Core/Port, Barr C, FreeRTOS, scatter file, armclang, refactor, "review nhánh", "review diff", dù không nói rõ tên skill.
---

# ai-review-maker

Skill chia nhỏ theo nguyên tắc nạp dần (progressive disclosure): file này chỉ định tuyến.
Đọc đúng file tham chiếu cần thiết cho từng bước, không nạp tất cả cùng lúc.

## Bước 0 — Luôn làm đầu tiên

1. Đọc `pre_requirement_skill.txt` để biết thông tin nào đã có, thông tin nào còn thiếu.
2. Nếu mục bắt buộc của workflow đang chạy còn `[MISSING]` -> hỏi người dùng, KHÔNG tự giả định.
3. Chạy (hoặc yêu cầu chạy) `scripts/check_folder_structure.py` để phát hiện cấu trúc folder thay đổi.
   Nếu có thay đổi -> yêu cầu người dùng cập nhật `references/03_folder_structure_api_core_port.md`.

## Chọn workflow

| Yêu cầu của người dùng | Workflow | Đọc |
|---|---|---|
| Tư vấn thiết kế luồng A, kèm code/mô tả/sơ đồ | 1 | `references/04_workflow_1_design_advice.md` |
| Review code trên nhánh hiện tại | 2 | `references/05_workflow_2_branch_review.md` |

## Tham chiếu dùng chung (nạp khi cần)

| File | Khi nào đọc |
|---|---|
| `references/01_role_and_context.md` | Bắt đầu mọi phiên |
| `references/02_coding_standard_barr_c.md` | Khi rà soát quy tắc code |
| `references/03_folder_structure_api_core_port.md` | Khi phân loại API/Core/Port |
| `references/06_review_checklists.md` | Khi rà soát FreeRTOS, concurrency, bộ nhớ, bảo mật/OTA/power, Keil |
| `references/07_output_format.md` | Trước khi trình bày kết quả |
| `references/08_tools.md` | Khi chọn công cụ khảo sát/kiểm tra tĩnh |
| `references/09_git_policy.md` | Trước khi chạy bất kỳ lệnh git nào |
| `references/10_operating_constraints.md` | Luôn tuân thủ (cục bộ, chỉ đọc) |

## Scripts (hiện chỉ có mô tả, chưa có code)

Xem `scripts/README.md`. Mỗi file `.py` hiện chỉ chứa docstring mô tả việc nó sẽ làm.
Chưa có code thì không giả vờ đã chạy script; nêu rõ "script chưa implement" và dùng lệnh shell thủ công thay thế.

## Quy tắc không thương lượng

- Đọc code thực tế trước khi đề xuất; không giả định cấu trúc.
- Git chỉ đọc. Không push/commit/reset khi chưa được chấp thuận.
- Không gửi source, log, thông tin project ra dịch vụ bên ngoài.
- Đề xuất API của common module: giữ tương thích ngược hoặc nêu rõ breaking change.
- Luôn nêu trade-off và lý do, không chỉ một đáp án.
