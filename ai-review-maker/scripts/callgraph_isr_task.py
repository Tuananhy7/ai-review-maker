"""
callgraph_isr_task.py  — CHỈ MÔ TẢ, CHƯA CÓ CODE  (Workflow 1)

Mục đích
    Dựng call graph của luồng A và xác định các điểm được gọi từ ISR và từ task.

Input
    - Tên hàm điểm vào của luồng A (hoặc danh sách)
    - compile_commands.json (từ uvprojx_to_compile_commands.py) để dùng với clangd
    - Danh sách mẫu nhận diện ISR (ví dụ hậu tố _IRQHandler, hàm callback HAL) — TODO xác nhận quy ước đặt tên
    - Danh sách mẫu nhận diện task entry (hàm truyền vào xTaskCreate) — TODO

Output
    - Call graph (văn bản/JSON, tùy chọn DOT/Mermaid)
    - Với mỗi hàm: ngữ cảnh gọi (ISR / task / cả hai / không rõ)
    - Cảnh báo: hàm gọi được từ cả ISR và task mà không có bảo vệ rõ ràng; API RTOS không có FromISR trong ngữ cảnh ISR

Các bước dự kiến
    1. Dùng clangd (hoặc ctags/cflow làm phương án dự phòng) để lấy quan hệ gọi hàm.
    2. Truy ngược từ ISR và task entry để gán ngữ cảnh gọi cho từng hàm.
    3. Xử lý con trỏ hàm/callback: đánh dấu "không xác định tĩnh", liệt kê để người dùng xác nhận.
    4. Xuất kết quả.

Ràng buộc
    - Chỉ đọc source. Chạy cục bộ.
    - Kết quả là đầu vào cho bảng finding, không thay thế việc đọc code.

Trạng thái: chưa implement.
"""
