# 10 — Ràng buộc vận hành

1. **Xử lý cục bộ:** mọi lệnh terminal được phép chạy, nhưng toàn bộ xử lý giữ ở máy cục bộ.
2. **Không gửi ra ngoài:** không gửi source, log, thông tin project tới dịch vụ bên ngoài.
3. **Git chỉ đọc:** xem `09_git_policy.md`.
4. **Output lưu cục bộ:** bảng finding, script, báo cáo lưu cục bộ, không đưa ra ngoài phạm vi nhóm.
5. **Build chỉ để xác nhận:** `UV4.exe -b` không được sửa project.
6. **Không giả định:** thiếu input -> hỏi.

## Nơi lưu output (đề xuất, cần xác nhận)
`<workspace>/.ai-review/reports/` (nên thêm vào `.gitignore`). Xem `pre_requirement_skill.txt`.
