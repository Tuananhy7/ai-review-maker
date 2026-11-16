# 05 — Workflow 2: Review code trên nhánh hiện tại

**Trigger:** Người dùng yêu cầu review code đã implement trên nhánh hiện tại.

## Các bước
1. **Xác định before và after**
   - before = commit gốc nhánh được checkout ra: `git merge-base HEAD <base>`
   - after = HEAD
   - `<base>` (main/develop/...) chưa biết -> hỏi người dùng (xem `pre_requirement_skill.txt`).
2. **Đọc git diff** theo từng commit, từng file, folder, module:
   - `git log --name-status <before>..HEAD`
   - `git diff -M --stat <before>..HEAD`
   - `git diff -M <before>..HEAD -- <folder>`
3. **Phân loại thay đổi** (có thể dùng `scripts/classify_changes.py`):
   - **Action 1:** code thay đổi trong một folder mẹ.
   - **Action 2:** logic chuyển qua lại giữa folder mẹ và con; nhận diện qua file bị xóa ở nơi này và thêm ở nơi khác (dùng `-M` để theo dõi rename/move).
4. **So sánh header trước/sau** để phát hiện thay đổi API và breaking change (`scripts/diff_headers_api.py`).
5. **Rà soát** theo Barr C, FreeRTOS, concurrency, bộ nhớ, tương thích API (xem `06_review_checklists.md`).
6. **Xác nhận bằng build** (tùy chọn): `scripts/build_check_keil.py` -> `UV4.exe -b <project>.uvprojx -t <target>`. Chỉ build, không sửa gì. Dùng kết quả để xác nhận cảnh báo armclang.
7. **Trình bày** theo `07_output_format.md`.

## Lưu ý
- Git chỉ đọc (xem `09_git_policy.md`).
- Mỗi finding nên truy được về commit/file cụ thể.
- Nếu logic chuyển Core <-> Port, kiểm tra ranh giới có bị vi phạm sau khi chuyển.
