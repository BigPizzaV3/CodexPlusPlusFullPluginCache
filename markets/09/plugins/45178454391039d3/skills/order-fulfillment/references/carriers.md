# Carriers and fulfillment centers

How each carrier connects to Zid, who moves order statuses, where its report
lives, and how its statuses map to Zid's. Carriers rename and add statuses:
match by meaning with the status map, and use the per-carrier names as examples.

## Status map

| Carrier event, by meaning | Zid status | Note |
| --- | --- | --- |
| Picking, packing or allocation started for a paid order | `preparing` | |
| Label created, booked, packed, waiting drop-off, ready for pickup | `ready` | The handoff to the carrier |
| Picked up, at a hub or service center, in transit, out for delivery | `indelivery` | The carrier holds the parcel |
| Failed attempt while the carrier still holds the parcel | `indelivery` | Exception |
| Delivered, proof of delivery | `delivered` | Needs a final success event |
| Cancelled before pickup, confirmed by the merchant | `cancelled` | |
| Returning, returned, refused, damaged, lost, customs hold | last true status | Exception: the merchant handles the return or claim |

## Zid Ship (direct shipping)

- Couriers include SPL, SMSA, J&T, iMile, Aramex and RedBox, with no separate
  courier contract. The service runs on the store's wallet balance.
- Moving an order to `ready` sends the request to the courier, which returns the
  waybill and tracking; integrated shipping needs the pickup location
  (`inventoryAddressId`). The courier moves the order to `indelivery` at pickup
  and to `delivered` at delivery.
- Read shipments, tracking, cash collected and label charges with the
  `zid_shipping` tools.

## Courier apps

| Carrier | Connection and who moves statuses | Report and statuses |
| --- | --- | --- |
| RedBox | Zid Ship or its own app. A pickup request is created when the order moves to `ready` (جاهز); under five parcels, the merchant drops them at a locker. | Portal → Shipments; the full status list is behind the info icon next to Status. `R-waiting`, `R-deposited`, `In-Transit-R` and `Returned` describe a return shipment and leave the original order `delivered`. |
| OTO | OTO → Sales Channels → Zid. OTO pulls orders according to the Zid-to-OTO status mapping the merchant set in OTO; that mapping decides which Zid status sends an order. | `pending`, `shipmentProcessing` → `preparing`; `readyForPickup` → `ready`; `pickedUpFromWarehouse`, `shipped`, `receivedAtWarehouse`, `inTransit`, `deliveryAttempts`, `inProgress`, `outForDelivery` → `indelivery`; `delivered` → `delivered`; `canceled` → `cancelled` once confirmed; `deliveryFailure`, `undelivered`, `refusedDelivery`, `returning`, `returned`, `damaged`, `lost` → exception. |
| Torod | Zid App Market → Shipping and Storage → Torod. Torod picks up orders while they are in `new`, so move orders to `preparing` after Torod has them; Orders → Sync Orders pulls missed ones. | Shipments → Export File exports every shipment in the current list. Cash: Settings → Wallet → COD (`Under Review`, `Cash Collected`, `Transferred`). `Ready For Pickup` → `ready`; `In Transit` → `indelivery`; `Failed Attempt` → `indelivery`, exception; `Failed Delivery` (being returned) → exception; `Delivered` → `delivered`; `Cancelled` → `cancelled` once confirmed. |
| AJEX | AJEX lists Zid among the platforms that push orders to it. | `Pending pickup`, `order packed` → `ready`; `Picked up`, hub, gateway and service-center statuses, `Out for Delivery`, `order handover` → `indelivery`; `Shipment Delivered`, `Image proof of delivery`, `Signature proof of delivery` → `delivered`; `Pickup Failed`, `Delivery Failed`, customs holds, `Start RTO`, `Complete RTO` and other returns → exception. Its API reports carry `waybillNumber` and `finalStatus`. |
| Aramex | Zid Ship, or the merchant's own account. | Tracking → Advanced Tracking → search by shipment number or reference → export CSV. `Created` → `ready`; `Collected`, any `In Transit` event, `Out for Delivery` → `indelivery`; `Delivered` → `delivered`. |
| SPL (Saudi Post) | Zid Ship, or the merchant's own account. | Portal → Shipment Reports → filter → export to Excel. `Draft`, `Pending Payment` → no change; `Waiting Drop off`, `Ready For Pick-Up` → `ready`; `Distributing` → `indelivery`; `Delivered` → `delivered`. |
| SMSA, J&T, iMile | Zid Ship, or the merchant's own account. | Map their event text with the status map. |

## Fulfillment centers

| Center | Connection | Status writeback |
| --- | --- | --- |
| Storage Station | Connects from its dashboard (Integrations → Zid). Orders and waybills go to the warehouse automatically. | Sends the status and waybill back to the store. |
| Cloud Shelf, Salasa, AyMakan | Connect with Zid from their side; orders flow to the center. | Not documented: reconcile from the center's report. |

## Tracking links

Use the link the carrier returns with the shipment; Zid Ship has no tracking
link of its own. Where only a number is available, these public pages take it in
the URL:

- SMSA: `https://smsaexpress.com/en/gb/track-shipment?track=<number>`
- SPL: `https://splonline.com.sa/en/tracktrace?tid=<number>`

AJEX, Torod, RedBox, iMile and Salasa have tracking pages where the customer
types the number.
