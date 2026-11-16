"""
classify_changes.py  — CHỈ MÔ TẢ, CHƯA CÓ CODE  (Workflow 2)

Mục đích
    Phân loại thay đổi giữa before (merge-base) và after (HEAD):
      Action 1: code thay đổi trong một folder mẹ.
      Action 2: logic chuyển qua lại giữa folder mẹ và con
                (file bị xóa ở nơi này và thêm ở nơi khác).

Input
    - Nhánh base (<base>), để tính before = git merge-base HEAD <base>
    - Danh sách folder mẹ/con cần phân loại (API, Core, Port và con của chúng)

Output
    - Danh sách theo commit và theo file: loại action, folder nguồn/đích, trạng thái (A/M/D/R)
    - Danh sách cặp file được xác định là di chuyển (kèm độ tương đồng)
    - Chỉ ra file đổi vị trí vượt ranh giới Core <-> Port để review kỹ hơn

Các bước dự kiến
    1. Chạy chỉ đọc: git merge-base, git log --name-status <before>..HEAD, git diff -M --stat.
    2. Parse trạng thái file: A, M, D, R<score>.
    3. Gom theo folder mẹ. File M/A/D trong một folder mẹ -> Action 1.
    4. File R giữa hai folder, hoặc cặp D + A có nội dung tương tự (ngoài rename git phát hiện) -> Action 2.
    5. Xuất báo cáo.

Ràng buộc
    - Git chỉ đọc. Tuyệt đối không commit/push/reset/checkout.
    - Chạy cục bộ.

Câu hỏi còn mở
    - Ngưỡng tương đồng cho rename (mặc định của git là 50%)?
    - Định nghĩa "folder mẹ" và "folder con" cụ thể của dự án.

Trạng thái: chưa implement.
"""
