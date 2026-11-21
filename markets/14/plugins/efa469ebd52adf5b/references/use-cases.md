# Use cases (shopping plugin)

1. "I want to shop at <store name>. Can you find it?" → `find_stores`
2. "Show me coffee mugs at <store> with price and stock." → `search_products`
3. "Does the <product> come in other sizes or colours?" → `get_product`
4. "What's the return policy and how much is shipping to the US?" → `get_return_policy`, `get_shipping_info`
5. "Does this store have an active discount code?" → `list_active_coupons` → the store's public codes exactly as returned (or that there are none)
6. "Put one <product>, size M, in my cart." → `get_product`, `create_cart` → cart link to pay on the store website
7. "Which times are free on Wednesday for a haircut at <store>? Book the first one." → `list_booking_services`, `get_booking_availability`, `create_cart` with `booking` → cart link; the booking is confirmed and paid on the store website
