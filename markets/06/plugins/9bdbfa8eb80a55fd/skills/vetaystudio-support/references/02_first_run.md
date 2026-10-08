# First run
The current application can show an account sign-in overlay, a License Key gate, or a License selection flow depending on the customer's session and entitlement state.
Customer-safe workflow:
1. Ask which screen is visible and request the exact text.
2. For a License Key screen, use the current key supplied to the customer and preserve its formatting.
3. For `Đăng nhập tài khoản để tiếp tục`, use the customer's own account; never ask for their password in chat.
4. After authorization, confirm the main workspace opens and the left navigation is usable.
5. Open `Cài đặt` only for the subsystem being configured; do not change unrelated provider or runtime settings.
Do not promise a License reset, device release, ownership transfer, or account correction. Those are administrative actions for official support.
