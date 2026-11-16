# 06 — Checklist rà soát

## A. FreeRTOS
- [ ] API gọi trong ISR phải có hậu tố `FromISR`; kiểm tra `portYIELD_FROM_ISR` / `xHigherPriorityTaskWoken`.
- [ ] Priority của ISR không cao hơn `configMAX_SYSCALL_INTERRUPT_PRIORITY` khi gọi API RTOS.
- [ ] Priority inversion: mutex (có priority inheritance) dùng bảo vệ tài nguyên; semaphore dùng đồng bộ/báo hiệu. Không dùng nhầm.
- [ ] Stack size của task đủ (kiểm tra high-water mark, `uxTaskGetStackHighWaterMark`).
- [ ] Không block trong critical section; không gọi API blocking từ ISR.
- [ ] Timeout của mọi lệnh blocking có xử lý khi hết hạn.

## B. Concurrency
- [ ] Biến chia sẻ ISR <-> task: `volatile` + bảo vệ thích hợp (critical section/atomic/queue).
- [ ] Truy cập không nguyên tử trên biến > 32 bit hoặc cấu trúc.
- [ ] Race condition giữa task và interrupt; thứ tự ghi/đọc; memory barrier nếu cần.
- [ ] Thời gian trong critical section ngắn, có giới hạn.

## C. Bộ nhớ
- [ ] Không cấp phát động sau khởi tạo.
- [ ] Mọi buffer có kích thước, kiểm tra bounds trước ghi/đọc.
- [ ] Ownership rõ ràng: ai cấp, ai giải phóng, ai chỉ đọc.
- [ ] Không trả con trỏ tới biến cục bộ / buffer có vòng đời ngắn.
- [ ] Không đệ quy; stack usage có thể chặn trên.
- [ ] Alignment cho DMA và cấu trúc đóng gói (packed).

## D. Bảo mật, OTA, rollback, power
- [ ] Khóa/key (DLMS security: authentication, encryption) không nằm trong log, không hard-code lộ.
- [ ] Kiểm tra độ dài/định dạng dữ liệu nhận từ kênh giao tiếp (chống tràn buffer, frame giả).
- [ ] Tương thích OTA: thay đổi layout bộ nhớ, bootloader, cấu hình lưu trữ có ảnh hưởng nâng cấp?
- [ ] Rollback: có đường lui khi cập nhật lỗi; dữ liệu cấu hình có migrate được?
- [ ] Power: mất điện giữa chừng khi ghi Flash/EEPROM; low-power mode ảnh hưởng timer/UART.

## E. Keil MDK / ARM Compiler
- [ ] Phân biệt armcc và armclang; `__attribute__` và `__weak` theo cú pháp armclang.
- [ ] Scatter file (không phải linker script GCC): vùng RAM/Flash, section đặc biệt.
- [ ] Target/Options trong `.uvprojx`: optimization level, define, include path, C/C++ standard.
- [ ] Thay đổi ảnh hưởng build: cảnh báo, kích thước ROM/RAM.

## F. Tương thích API (common module)
- [ ] Chữ ký hàm, kiểu, macro, enum công khai trong API/ có thay đổi?
- [ ] Thay đổi ABI/kích thước struct công khai?
- [ ] Nếu breaking: ghi rõ, đề xuất đường chuyển đổi (deprecate trước, wrapper tương thích).
