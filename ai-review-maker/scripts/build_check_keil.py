"""
build_check_keil.py  — CHỈ MÔ TẢ, CHƯA CÓ CODE  (Workflow 2)

Mục đích
    Chạy build bằng Keil uVision CLI để xác nhận cảnh báo/lỗi của armclang.
    Lệnh chỉ build, không sửa gì: UV4.exe -b <project>.uvprojx -t <target>

Input
    - Đường dẫn UV4.exe
    - Đường dẫn .uvprojx
    - Tên target
    - Đường dẫn log build

Output
    - Mã thoát và log build
    - Danh sách cảnh báo/lỗi đã trích (file, dòng, mã cảnh báo, nội dung)
    - Kích thước ROM/RAM nếu đọc được từ log/map

Các bước dự kiến
    1. Kiểm tra UV4.exe và .uvprojx tồn tại; thiếu thì báo rõ.
    2. Chạy UV4.exe -b với tham số log.
    3. Phân tích log, gom cảnh báo theo loại.
    4. Đối chiếu cảnh báo với bảng finding (nếu trùng file/hàm).

Ràng buộc
    - Chỉ build. Không sửa .uvprojx, không flash/download.
    - Lưu ý: build có thể ghi file vào thư mục Objects/Listings; thống nhất vị trí (xem pre_requirement_skill.txt).
    - Chạy cục bộ.

Trạng thái: chưa implement.
"""
