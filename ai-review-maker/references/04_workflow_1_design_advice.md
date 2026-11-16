# 04 — Workflow 1: Tư vấn thiết kế common module DLMS từ luồng A

**Trigger:** Người dùng gửi yêu cầu tư vấn cải thiện thiết kế luồng A, kèm code, mô tả hoặc sơ đồ.

## Input cần có
- Code luồng A
- Cây thư mục API/ Core/ Port/
- Use case DLMS
- MCU
- Phiên bản FreeRTOS và Keil MDK
- Ràng buộc RAM/Flash và tương thích

Thiếu mục nào -> hỏi (một câu hỏi gộp, liệt kê mục thiếu). Không tự giả định.

## Các bước
1. **Nạp overview và cây thư mục.** Thiếu thì hỏi.
2. **Đọc code luồng A:** hàm, state, buffer, ownership, điểm gọi từ ISR hoặc task.
   - Dựng call graph (ctags/cflow hoặc `scripts/callgraph_isr_task.py`).
3. **Phân loại** từng hàm/file: API/ (ổn định), Core/ (logic DLMS, không phụ thuộc phần cứng), Port/ (HAL, RTOS, scatter file).
   - Chạy `scripts/check_core_port_boundary.py` để đánh dấu hàm vi phạm ranh giới.
4. **Rà soát** theo Barr C, FreeRTOS, concurrency, bộ nhớ, bảo mật, OTA, power (xem `06_review_checklists.md`).
5. **Đề xuất refactor** kèm trade-off; ghi rõ tương thích ngược hay breaking change.
6. **Trình bày** theo `07_output_format.md`: summary tối đa 3 câu, bảng finding, bảng refactor nếu có nhiều mục.

## Công cụ riêng của workflow này
- ctags / cflow (hoặc Python dựa trên clangd) cho call graph.
- Script đối chiếu hàm Core/ với lời gọi phần cứng/RTOS.
- Không cần git diff; chỉ dùng `git log` khi cần lịch sử của luồng A.

## Lưu ý DLMS
Use case DLMS cụ thể (COSEM objects, association, security suite, HDLC/Wrapper, ...) phải do người dùng cung cấp.
Không suy đoán use case.
