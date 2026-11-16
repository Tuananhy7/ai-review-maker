# scripts/ — Python script (chỉ có mô tả, chưa có code)

Mỗi file `.py` hiện chỉ chứa docstring mô tả: mục đích, input, output, các bước dự kiến, ràng buộc, trạng thái.
Khi implement, giữ nguyên docstring làm đặc tả và thêm code bên dưới.

| Script | Workflow | Việc làm |
|---|---|---|
| `uvprojx_to_compile_commands.py` | Chung | Chuyển `.uvprojx` -> `compile_commands.json`, tự cập nhật khi project đổi |
| `check_folder_structure.py` | Chung | Phát hiện thay đổi cấu trúc API/Core/Port, cảnh báo cập nhật bối cảnh |
| `callgraph_isr_task.py` | 1 | Dựng call graph luồng A, đánh dấu điểm gọi từ ISR/task |
| `check_core_port_boundary.py` | 1 | Đánh dấu hàm Core/ vi phạm ranh giới (gọi HAL/RTOS) |
| `classify_changes.py` | 2 | Phân loại thay đổi: Action 1 / Action 2 |
| `diff_headers_api.py` | 2 | So sánh header trước/sau, phát hiện breaking change API |
| `build_check_keil.py` | 2 | Gọi `UV4.exe -b` (chỉ build), trích cảnh báo armclang |

## Ràng buộc chung cho mọi script
- Chạy cục bộ, không có kết nối mạng, không gửi dữ liệu ra ngoài.
- Git chỉ đọc (không commit/push/reset/checkout).
- Không sửa file nguồn của project; chỉ ghi output vào thư mục báo cáo cục bộ.
- Thiếu input -> báo lỗi rõ ràng, không đoán.
