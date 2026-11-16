# 02 — Coding standard: Barr C (Embedded C Coding Standard)

Khi đề xuất code, ưu tiên các quy tắc sau (mỗi finding ghi quy tắc Barr C liên quan vào cột "Quy tắc Barr C").

| Chủ đề | Yêu cầu |
|---|---|
| Kiểu dữ liệu | Dùng kiểu kích thước cố định từ `<stdint.h>` (`uint8_t`, `uint16_t`, `uint32_t`, ...) |
| volatile | Bắt buộc cho thanh ghi phần cứng và biến chia sẻ với ISR |
| Đệ quy | Cấm |
| Cấp phát động | Tránh; nếu cần thì chỉ ở giai đoạn khởi tạo |
| Giá trị trả về | Luôn kiểm tra |
| Buffer / bounds | Kiểm tra giới hạn trước mọi truy cập mảng/buffer |

## Ghi chú
- Số hiệu quy tắc cụ thể (ví dụ "Rule 1.3.a"): TODO — cần bản Barr C chính thức của team để trích dẫn chính xác.
  Xem `pre_requirement_skill.txt`, mục Barr C.
- Không bịa số hiệu quy tắc. Nếu chưa có tài liệu, ghi tên chủ đề (ví dụ "Barr C: fixed-width integers").
- Cấu hình `clang-tidy`/`cppcheck` cho các check liên quan: xem `08_tools.md`.
