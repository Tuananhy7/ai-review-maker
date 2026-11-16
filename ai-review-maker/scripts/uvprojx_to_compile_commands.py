"""
uvprojx_to_compile_commands.py  — CHỈ MÔ TẢ, CHƯA CÓ CODE

Mục đích
    Chuyển file project Keil (.uvprojx) sang compile_commands.json để clangd, clang-tidy, cppcheck dùng được.
    Tự động cập nhật khi project thay đổi.

Input
    - Đường dẫn .uvprojx
    - Tên target (ví dụ lấy từ Target/Options trong uVision)
    - Thư mục workspace (gốc để tính đường dẫn tương đối)

Output
    - compile_commands.json (đường dẫn ghi: TODO, xem pre_requirement_skill.txt)

Các bước dự kiến
    1. Parse XML của .uvprojx.
    2. Với target được chọn, trích: danh sách file nguồn (Groups/Files), IncludePath, Define,
       cấu hình compiler (armclang/armcc), C/C++ standard, optimization level.
    3. Với mỗi file .c/.cpp, sinh một entry: directory, file, arguments (hoặc command).
    4. Chuyển cờ ARM Compiler sang dạng clangd hiểu được (cờ không tương thích thì bỏ hoặc thay thế,
       ghi lại danh sách cờ đã bỏ).
    5. Ghi compile_commands.json.
    6. Chế độ tự cập nhật: so sánh hash/mtime của .uvprojx với lần chạy trước, chỉ sinh lại khi đổi.

Ràng buộc
    - Chỉ đọc .uvprojx, không sửa project.
    - Chạy cục bộ.

Câu hỏi còn mở (xem pre_requirement_skill.txt)
    - Có nhiều target không? Target nào là chuẩn để review?
    - Phiên bản Keil MDK và ARM Compiler (5 hay 6)?
    - Cách kích hoạt tự cập nhật (hook, task VS Code, chạy tay)?

Trạng thái: chưa implement.
"""
