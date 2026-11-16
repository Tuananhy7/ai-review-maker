# 08 — Công cụ

## Chung cho cả hai workflow

| Công cụ | Mục đích | Ghi chú |
|---|---|---|
| Shell (bash/Git Bash): `ls`, `tree`, `grep`, `rg` | Khảo sát cấu trúc, tìm symbol | |
| clangd | Điều hướng định nghĩa/tham chiếu, tìm lời gọi | Cần `compile_commands.json` |
| clang-tidy, cppcheck | Kiểm tra tĩnh, làm đầu vào bảng finding | Cần cấu hình check theo Barr C |
| Python script tự viết | Xem `scripts/README.md` | Chưa có code |

### Cấu hình check cho Barr C (cần làm)
- Kiểu số nguyên cố định
- volatile cho thanh ghi và biến dùng trong ISR
- Cấp phát động
- Đệ quy
- Kiểm tra giá trị trả về

Danh sách check cụ thể của clang-tidy/cppcheck: TODO (xem `pre_requirement_skill.txt`).

## Workflow 1
- ctags hoặc cflow (hoặc Python dựa trên clangd) dựng call graph luồng A, xác định điểm gọi từ ISR và task.
- Script đối chiếu hàm Core/ với lời gọi phần cứng/RTOS.

## Workflow 2
- Git chỉ đọc: xem `09_git_policy.md`.
- Python script phân loại thay đổi (Action 1 / Action 2).
- So sánh header trước/sau để phát hiện breaking change API.
- Keil uVision CLI: `UV4.exe -b <project>.uvprojx -t <target>` (chỉ build).

## Về compile_commands.json
Keil MDK không sinh `compile_commands.json` trực tiếp. Dự định dùng `scripts/uvprojx_to_compile_commands.py`
để chuyển từ `.uvprojx` và tự cập nhật khi project thay đổi.
