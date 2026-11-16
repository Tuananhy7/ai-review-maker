"""
diff_headers_api.py  — CHỈ MÔ TẢ, CHƯA CÓ CODE  (Workflow 2)

Mục đích
    So sánh header trước (before) và sau (after) để phát hiện thay đổi API và breaking change.

Input
    - before, after (commit)
    - Danh sách header công khai (thường trong API/) — TODO xác nhận
    - compile_commands.json (tùy chọn, để parse bằng clang)

Output
    - Danh sách thay đổi: hàm thêm/xóa/đổi chữ ký, kiểu/struct/enum/macro đổi, kích thước struct công khai
    - Phân loại: tương thích ngược / breaking
    - Cảnh báo header Core/Port bị lộ ra API công khai

Các bước dự kiến
    1. Lấy nội dung header ở before và after bằng git show (chỉ đọc).
    2. Trích khai báo công khai (ưu tiên AST của clang; phương án tối thiểu: regex).
    3. So sánh theo ký hiệu: tên, chữ ký, kiểu, giá trị enum, định nghĩa macro, bố cục struct.
    4. Phân loại breaking (xóa/đổi chữ ký/đổi thứ tự/đổi kích thước/đổi giá trị enum).

Ràng buộc
    - Git chỉ đọc. Không checkout hai phiên bản ra working tree.
    - Chạy cục bộ.

Trạng thái: chưa implement.
"""
