# 03 — Cấu trúc folder: API / Core / Port

> TRẠNG THÁI: CHƯA CÓ cây thư mục thực tế. Điền vào đây khi người dùng cung cấp.
> Cấu trúc có thể thay đổi; nếu script phát hiện khác biệt -> yêu cầu cập nhật file này.

## Phân loại theo vai trò

| Folder | Vai trò | Ràng buộc |
|---|---|---|
| `API/` | Giao diện công khai của common module | Ổn định; thay đổi phải tương thích ngược hoặc ghi rõ breaking change |
| `Core/` | Logic DLMS, protocol, state machine | KHÔNG phụ thuộc phần cứng/RTOS (không HAL, không FreeRTOS API trực tiếp) |
| `Port/` | HAL, driver, RTOS port, scatter file, cấu hình FreeRTOS port | Platform-specific; mọi phụ thuộc phần cứng/RTOS nằm ở đây |

## Cây thư mục hiện tại (cần người dùng cung cấp)

```
<TODO: dán output của `tree -L 3` hoặc của scripts/check_folder_structure.py>
```

## Snapshot để so sánh
- Ngày snapshot: <TODO>
- Commit tại thời điểm snapshot: <TODO>
- File snapshot do script sinh: `scripts/.cache/folder_snapshot.json` (chưa có)

## Dấu hiệu vi phạm ranh giới Core/Port
- Hàm trong `Core/` gọi HAL (`HAL_*`, `LL_*`), thanh ghi, hoặc FreeRTOS API (`xTaskCreate`, `xQueue*`, `vTaskDelay`, ...).
- `Core/` include header của `Port/` hoặc header vendor (`stm32*.h`).
- `API/` lộ kiểu dữ liệu platform-specific.
