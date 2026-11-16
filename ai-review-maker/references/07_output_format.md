# 07 — Quy ước đầu ra

## Thứ tự trình bày
1. **Summary** ngắn, tối đa 3 câu: tổng số finding theo mức độ, rủi ro lớn nhất, phạm vi ảnh hưởng.
2. **Bảng finding**
3. **Bảng refactor** (riêng, sau bảng finding, nếu có nhiều mục)

## Bảng finding

Mỗi finding là một dòng, các cột:

| # | Mức độ | File / Hàm | Vấn đề | Quy tắc Barr C | Đề xuất sửa |
|---|---|---|---|---|---|

Mức độ: `critical`, `major`, `minor`.

- critical: có thể gây hỏng dữ liệu, treo/reset thiết bị, lỗ hổng bảo mật, mất khả năng OTA/rollback.
- major: sai thiết kế ảnh hưởng ổn định/bảo trì, vi phạm ranh giới Core/Port, breaking change API không khai báo.
- minor: vi phạm style/quy tắc nhỏ, rủi ro thấp.

(Định nghĩa 3 mức trên là đề xuất của skill; xem `pre_requirement_skill.txt` để xác nhận với team.)

## Bảng refactor

| # | Hạng mục | Phạm vi ảnh hưởng (folder/file/API) | Tương thích ngược? | Trade-off | Ghi chú |
|---|---|---|---|---|---|

## Ví dụ khung

> **Summary:** 7 finding (1 critical, 3 major, 3 minor). Rủi ro lớn nhất: ISR gọi API RTOS không có hậu tố FromISR trong luồng nhận frame. Ảnh hưởng Core/ và Port/ của module HDLC.

| # | Mức độ | File / Hàm | Vấn đề | Quy tắc Barr C | Đề xuất sửa |
|---|---|---|---|---|---|
| 1 | critical | `Port/uart_port.c` / `uart_rx_isr` | ... | ... | ... |

## Nguyên tắc
- Cột "Quy tắc Barr C" ghi "N/A" nếu finding không thuộc Barr C (ví dụ lỗi thiết kế RTOS); không bịa số hiệu.
- Mọi đề xuất kèm lý do; nêu trade-off khi có nhiều hướng.
- Output lưu cục bộ, không đưa ra ngoài nhóm (xem `10_operating_constraints.md`).
