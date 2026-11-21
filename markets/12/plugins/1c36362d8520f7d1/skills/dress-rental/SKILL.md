---
name: dress-rental
description: 드레스 대여, 대여 상품, 재고, 견적, 대여 가능 날짜, 대여 주문, 대여 문의, 대여 리뷰, 배송 조회에 사용한다. Use for WeddingFlow rental products, availability, quotes, orders, inquiries, and reviews. Payment approval is not available here.
---

# WeddingFlow dress rental

Answer in Korean. Prices, stock, and booking dates must come from the MCP tools. Never claim a date is available or a payment succeeded unless the tool result says so.

## Read

| Intent | Tool |
| --- | --- |
| Product list | `get_api_v1_rental_product` |
| List filters such as concepts | `get_api_v1_rental_product_meta` |
| One product | `get_api_v1_rental_product_by_product_id` |
| Quote | `get_api_v1_rental_product_by_product_id_quote` |
| Availability | `get_api_v1_rental_availability` |
| Booked date ranges | `get_api_v1_rental_booked_ranges` |
| Operating settings | `get_api_v1_rental_settings` |
| Reviews and summary | `get_api_v1_rental_product_by_product_id_review`, `get_api_v1_rental_product_by_product_id_review_summary` |
| Restock alert status | `get_api_v1_rental_product_by_product_id_restock_alert`, `get_api_v1_rental_restock_alert` |
| My orders | `get_api_v1_rental_order`, `get_api_v1_rental_order_by_order_id` |
| Tracking | `get_api_v1_rental_order_by_order_id_tracking` |
| My inquiries | `get_api_v1_rental_inquiry`, `get_api_v1_rental_inquiry_by_inquiry_id`, `get_api_v1_rental_inquiry_by_inquiry_id_answer` |
| My reviews | `get_api_v1_rental_review`, `get_api_v1_rental_review_by_review_id`, `get_api_v1_rental_review_writable` |

Product search uses `query.search` and `query.concept`. Availability needs `productId`, `pickupDate`, `returnDate`, and `quantity`. Check settings for pickup place, hours, delivery fee, and min/max rental days before suggesting dates. Keep list sizes at 20 or below.

## Write

Confirm every field, then call the tool once. Do not retry a failed POST. This connection cannot approve payment, cancel, refund, or change an order.

Order, `post_api_v1_rental_order` body:

- `productId`, `pickupDate`, `returnDate` (`YYYY-MM-DD`), `quantity`
- `customerName`, `phone`
- `deliveryType`: `visit` unless the user chooses delivery
- `address`, `addressDetail` when delivery needs them

Check availability and the quote before creating an order. Tell the user that payment still has to be finished in WeddingFlow.

Inquiry, `post_api_v1_rental_inquiry` body: `phone`, `title`, `content`, and optional `customerName`, `orderNumber`.

Review, `post_api_v1_rental_order_by_order_id_review`: `rating` from 1 to 5, `content` of at least 10 characters, optional `images` as URL strings. Check writable orders first. The order id goes in `path_params`.
