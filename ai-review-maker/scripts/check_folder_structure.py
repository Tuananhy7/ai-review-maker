"""
check_folder_structure.py  — CHỈ MÔ TẢ, CHƯA CÓ CODE

Mục đích
    Phát hiện thay đổi cấu trúc folder API/ Core/ Port/ so với snapshot đã lưu,
    và cảnh báo người dùng cần cập nhật bối cảnh (references/03_folder_structure_api_core_port.md).

Input
    - Gốc workspace
    - Danh sách folder cần theo dõi (mặc định: API, Core, Port và các folder con)
    - File snapshot cũ: scripts/.cache/folder_snapshot.json

Output
    - Báo cáo: folder/file mới, bị xóa, bị đổi tên/di chuyển so với snapshot
    - Mã thoát khác 0 nếu có thay đổi (để dùng trong hook/kiểm tra)
    - Tùy chọn: ghi snapshot mới sau khi người dùng xác nhận đã cập nhật bối cảnh

Các bước dự kiến
    1. Duyệt cây thư mục theo danh sách theo dõi (bỏ qua build output, .git, thư viện bên thứ ba).
    2. Tạo snapshot (đường dẫn tương đối, loại file, có thể kèm hash nội dung).
    3. So sánh với snapshot cũ.
    4. In cảnh báo: "Cấu trúc đã thay đổi — hãy cập nhật bối cảnh" kèm danh sách khác biệt.

Ràng buộc
    - Chỉ đọc cây thư mục; chỉ ghi snapshot khi được yêu cầu rõ.
    - Chạy cục bộ.

Câu hỏi còn mở
    - Tên folder thực tế của dự án (API/Core/Port có đúng chữ hoa/thường như vậy không)?
    - Folder nào cần loại trừ?

Trạng thái: chưa implement.
"""
