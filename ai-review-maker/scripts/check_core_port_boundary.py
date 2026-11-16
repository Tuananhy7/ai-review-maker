"""
check_core_port_boundary.py  — CHỈ MÔ TẢ, CHƯA CÓ CODE  (Workflow 1)

Mục đích
    Đối chiếu các hàm nằm trong Core/ với lời gọi phần cứng hoặc RTOS.
    Hàm vi phạm ranh giới Core/Port được đánh dấu.

Input
    - Gốc workspace; đường dẫn folder Core/
    - Danh sách mẫu "phần cứng": HAL_*, LL_*, thanh ghi/đường dẫn include stm32*.h, CMSIS, ...
    - Danh sách mẫu "RTOS": xTask*, xQueue*, xSemaphore*, vTaskDelay, taskENTER_CRITICAL, ...
    - Danh sách ngoại lệ (allowlist) do người dùng xác nhận

Output
    - Bảng/JSON: file, hàm, dòng, loại vi phạm (HW/RTOS/include), symbol vi phạm
    - Có thể dùng trực tiếp làm đầu vào cho bảng finding (mức độ đề xuất: major)

Các bước dự kiến
    1. Quét #include trong Core/ tìm header Port/ hoặc header vendor.
    2. Dùng clangd/AST (hoặc regex mức tối thiểu) tìm lời gọi và truy cập thanh ghi trong hàm của Core/.
    3. So khớp với danh sách mẫu; bỏ qua ngoại lệ.
    4. Xuất báo cáo.

Ràng buộc
    - Chỉ đọc source. Chạy cục bộ.
    - Regex có thể false positive; kết quả cần người review xác nhận.

Câu hỏi còn mở
    - Core/ có được phép dùng lớp trừu tượng OS (ví dụ osal_*) không? Danh sách đó là gì?

Trạng thái: chưa implement.
"""
