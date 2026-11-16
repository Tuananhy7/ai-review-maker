# 09 — Chính sách Git

## Chỉ đọc
Được phép (không thay đổi repo):
- `git merge-base HEAD <base>`
- `git log --name-status <before>..HEAD`
- `git diff -M --stat`
- `git diff -M <before>..HEAD -- <folder>`
- `git show`, `git status`, `git branch` (liệt kê), `git rev-parse`

KHÔNG được phép nếu chưa được người dùng chấp thuận rõ ràng:
- `git push`, `git commit`, `git reset`, `git checkout` (đổi nhánh/ghi đè file), `git rebase`, `git merge`,
  `git stash`, `git clean`, `git cherry-pick`, tạo/xóa tag hoặc branch

## Xác định before/after
- before = `git merge-base HEAD <base>`; `<base>` do người dùng cung cấp (xem `pre_requirement_skill.txt`).
- after = HEAD.

## Theo dõi di chuyển file
Dùng `-M` (phát hiện rename). Ngưỡng tương đồng (ví dụ `-M60%`) nên xác nhận với người dùng nếu kết quả không rõ.

## Khi cần thay đổi repo
Dừng lại, nêu lệnh định chạy và lý do, chờ người dùng chấp thuận.
