# Etsy operation index

Verified 2026-10-04: 105 direct tools from MakeBox's Etsy manifest.
Use this index to find the exact named tool, then inspect its live schema. This is not permission to call a tool.
Private shop/user identity is server-bound; public reads may still expose those IDs. The full input snapshot is in [schemas](etsy-tool-schemas.json).
An empty body is still required when shown by the input schema. `token_scopes` handles the token server-side; never supply it.

| Tool | Operation / method | Required top-level inputs | Required body fields | Scopes |
| --- | --- | --- | --- | --- |
| `etsy_consolidate_shop_return_policies` | [consolidateShopReturnPolicies](https://developers.etsy.com/documentation/reference/#operation/consolidateShopReturnPolicies) / POST | `body`, `confirm` | `source_return_policy_id`, `destination_return_policy_id` | shops_w |
| `etsy_create_draft_listing` | [createDraftListing](https://developers.etsy.com/documentation/reference/#operation/createDraftListing) / POST | `body`, `confirm` | `quantity`, `title`, `description`, `price`, `who_made`, `when_made`, `taxonomy_id` | listings_w |
| `etsy_create_listing_translation` | [createListingTranslation](https://developers.etsy.com/documentation/reference/#operation/createListingTranslation) / POST | `listing_id`, `language`, `body`, `confirm` | `title`, `description` | listings_w |
| `etsy_create_receipt_shipment` | [createReceiptShipment](https://developers.etsy.com/documentation/reference/#operation/createReceiptShipment) / POST | `receipt_id`, `body`, `confirm` |  | transactions_w |
| `etsy_create_shop_readiness_state_definition` | [createShopReadinessStateDefinition](https://developers.etsy.com/documentation/reference/#operation/createShopReadinessStateDefinition) / POST | `body`, `confirm` | `readiness_state`, `min_processing_time`, `max_processing_time` | shops_w |
| `etsy_create_shop_return_policy` | [createShopReturnPolicy](https://developers.etsy.com/documentation/reference/#operation/createShopReturnPolicy) / POST | `body`, `confirm` | `accepts_returns`, `accepts_exchanges` | shops_w |
| `etsy_create_shop_section` | [createShopSection](https://developers.etsy.com/documentation/reference/#operation/createShopSection) / POST | `body`, `confirm` | `title` | shops_w |
| `etsy_create_shop_shipping_profile` | [createShopShippingProfile](https://developers.etsy.com/documentation/reference/#operation/createShopShippingProfile) / POST | `body`, `confirm` | `title`, `origin_country_iso`, `primary_cost`, `secondary_cost` | shops_w |
| `etsy_create_shop_shipping_profile_destination` | [createShopShippingProfileDestination](https://developers.etsy.com/documentation/reference/#operation/createShopShippingProfileDestination) / POST | `shipping_profile_id`, `body`, `confirm` | `primary_cost`, `secondary_cost` | shops_w |
| `etsy_create_shop_shipping_profile_upgrade` | [createShopShippingProfileUpgrade](https://developers.etsy.com/documentation/reference/#operation/createShopShippingProfileUpgrade) / POST | `shipping_profile_id`, `body`, `confirm` | `type`, `upgrade_name`, `price`, `secondary_price` | shops_w |
| `etsy_delete_listing` | [deleteListing](https://developers.etsy.com/documentation/reference/#operation/deleteListing) / DELETE | `listing_id`, `confirm`, `expected_title` |  | listings_d |
| `etsy_delete_listing_file` | [deleteListingFile](https://developers.etsy.com/documentation/reference/#operation/deleteListingFile) / DELETE | `listing_id`, `listing_file_id`, `confirm` |  | listings_w |
| `etsy_delete_listing_image` | [deleteListingImage](https://developers.etsy.com/documentation/reference/#operation/deleteListingImage) / DELETE | `listing_id`, `listing_image_id`, `confirm` |  | listings_w |
| `etsy_delete_listing_personalization` | [deleteListingPersonalization](https://developers.etsy.com/documentation/reference/#operation/deleteListingPersonalization) / DELETE | `listing_id`, `confirm` |  | listings_w |
| `etsy_delete_listing_property` | [deleteListingProperty](https://developers.etsy.com/documentation/reference/#operation/deleteListingProperty) / DELETE | `listing_id`, `property_id`, `confirm` |  | listings_w |
| `etsy_delete_listing_video` | [deleteListingVideo](https://developers.etsy.com/documentation/reference/#operation/deleteListingVideo) / DELETE | `listing_id`, `video_id`, `confirm` |  | listings_w |
| `etsy_delete_shop_readiness_state_definition` | [deleteShopReadinessStateDefinition](https://developers.etsy.com/documentation/reference/#operation/deleteShopReadinessStateDefinition) / DELETE | `readiness_state_definition_id`, `confirm` |  | shops_w |
| `etsy_delete_shop_return_policy` | [deleteShopReturnPolicy](https://developers.etsy.com/documentation/reference/#operation/deleteShopReturnPolicy) / DELETE | `return_policy_id`, `confirm` |  | shops_w |
| `etsy_delete_shop_section` | [deleteShopSection](https://developers.etsy.com/documentation/reference/#operation/deleteShopSection) / DELETE | `shop_section_id`, `confirm` |  | shops_w |
| `etsy_delete_shop_shipping_profile` | [deleteShopShippingProfile](https://developers.etsy.com/documentation/reference/#operation/deleteShopShippingProfile) / DELETE | `shipping_profile_id`, `confirm` |  | shops_w |
| `etsy_delete_shop_shipping_profile_destination` | [deleteShopShippingProfileDestination](https://developers.etsy.com/documentation/reference/#operation/deleteShopShippingProfileDestination) / DELETE | `shipping_profile_id`, `shipping_profile_destination_id`, `confirm` |  | shops_w |
| `etsy_delete_shop_shipping_profile_upgrade` | [deleteShopShippingProfileUpgrade](https://developers.etsy.com/documentation/reference/#operation/deleteShopShippingProfileUpgrade) / DELETE | `shipping_profile_id`, `upgrade_id`, `confirm` |  | shops_w |
| `etsy_delete_user_address` | [deleteUserAddress](https://developers.etsy.com/documentation/reference/#operation/deleteUserAddress) / DELETE | `user_address_id`, `confirm` |  | address_r |
| `etsy_find_all_active_listings_by_shop` | [findAllActiveListingsByShop](https://developers.etsy.com/documentation/reference/#operation/findAllActiveListingsByShop) / GET | `shop_id` |  |  |
| `etsy_find_all_listings_active` | [findAllListingsActive](https://developers.etsy.com/documentation/reference/#operation/findAllListingsActive) / GET |  |  |  |
| `etsy_find_shops` | [findShops](https://developers.etsy.com/documentation/reference/#operation/findShops) / GET | `shop_name` |  |  |
| `etsy_get_all_listing_files` | [getAllListingFiles](https://developers.etsy.com/documentation/reference/#operation/getAllListingFiles) / GET | `listing_id` |  | listings_r |
| `etsy_get_buyer_taxonomy_nodes` | [getBuyerTaxonomyNodes](https://developers.etsy.com/documentation/reference/#operation/getBuyerTaxonomyNodes) / GET |  |  |  |
| `etsy_get_featured_listings_by_shop` | [getFeaturedListingsByShop](https://developers.etsy.com/documentation/reference/#operation/getFeaturedListingsByShop) / GET | `shop_id` |  |  |
| `etsy_get_holiday_preferences` | [getHolidayPreferences](https://developers.etsy.com/documentation/reference/#operation/getHolidayPreferences) / GET |  |  | shops_r |
| `etsy_get_listing` | [getListing](https://developers.etsy.com/documentation/reference/#operation/getListing) / GET | `listing_id` |  |  |
| `etsy_get_listing_file` | [getListingFile](https://developers.etsy.com/documentation/reference/#operation/getListingFile) / GET | `listing_id`, `listing_file_id` |  | listings_r |
| `etsy_get_listing_image` | [getListingImage](https://developers.etsy.com/documentation/reference/#operation/getListingImage) / GET | `listing_id`, `listing_image_id` |  |  |
| `etsy_get_listing_images` | [getListingImages](https://developers.etsy.com/documentation/reference/#operation/getListingImages) / GET | `listing_id` |  |  |
| `etsy_get_listing_inventory` | [getListingInventory](https://developers.etsy.com/documentation/reference/#operation/getListingInventory) / GET | `listing_id` |  | listings_r |
| `etsy_get_listing_offering` | [getListingOffering](https://developers.etsy.com/documentation/reference/#operation/getListingOffering) / GET | `listing_id`, `product_id`, `product_offering_id` |  |  |
| `etsy_get_listing_personalization` | [getListingPersonalization](https://developers.etsy.com/documentation/reference/#operation/getListingPersonalization) / GET | `listing_id` |  |  |
| `etsy_get_listing_product` | [getListingProduct](https://developers.etsy.com/documentation/reference/#operation/getListingProduct) / GET | `listing_id`, `product_id` |  | listings_r |
| `etsy_get_listing_properties` | [getListingProperties](https://developers.etsy.com/documentation/reference/#operation/getListingProperties) / GET | `shop_id`, `listing_id` |  |  |
| `etsy_get_listing_property` | [getListingProperty](https://developers.etsy.com/documentation/reference/#operation/getListingProperty) / GET | `listing_id`, `property_id` |  |  |
| `etsy_get_listing_translation` | [getListingTranslation](https://developers.etsy.com/documentation/reference/#operation/getListingTranslation) / GET | `shop_id`, `listing_id`, `language` |  |  |
| `etsy_get_listing_variation_images` | [getListingVariationImages](https://developers.etsy.com/documentation/reference/#operation/getListingVariationImages) / GET | `shop_id`, `listing_id` |  |  |
| `etsy_get_listing_video` | [getListingVideo](https://developers.etsy.com/documentation/reference/#operation/getListingVideo) / GET | `video_id`, `listing_id` |  |  |
| `etsy_get_listing_videos` | [getListingVideos](https://developers.etsy.com/documentation/reference/#operation/getListingVideos) / GET | `listing_id` |  |  |
| `etsy_get_listings_by_listing_ids` | [getListingsByListingIds](https://developers.etsy.com/documentation/reference/#operation/getListingsByListingIds) / GET | `listing_ids` |  |  |
| `etsy_get_listings_by_shop` | [getListingsByShop](https://developers.etsy.com/documentation/reference/#operation/getListingsByShop) / GET |  |  | listings_r |
| `etsy_get_listings_by_shop_receipt` | [getListingsByShopReceipt](https://developers.etsy.com/documentation/reference/#operation/getListingsByShopReceipt) / GET | `receipt_id` |  | transactions_r |
| `etsy_get_listings_by_shop_return_policy` | [getListingsByShopReturnPolicy](https://developers.etsy.com/documentation/reference/#operation/getListingsByShopReturnPolicy) / GET | `return_policy_id` |  | listings_r |
| `etsy_get_listings_by_shop_section_id` | [getListingsByShopSectionId](https://developers.etsy.com/documentation/reference/#operation/getListingsByShopSectionId) / GET | `shop_id`, `shop_section_ids` |  |  |
| `etsy_get_listings_inventory_by_listing_ids` | [getListingsInventoryByListingIds](https://developers.etsy.com/documentation/reference/#operation/getListingsInventoryByListingIds) / GET | `listing_ids` |  | listings_r |
| `etsy_get_listings_shipping_by_listing_ids` | [getListingsShippingByListingIds](https://developers.etsy.com/documentation/reference/#operation/getListingsShippingByListingIds) / GET | `listing_ids` |  | shops_r |
| `etsy_get_me` | [getMe](https://developers.etsy.com/documentation/reference/#operation/getMe) / GET |  |  | shops_r |
| `etsy_get_payment_account_ledger_entry_payments` | [getPaymentAccountLedgerEntryPayments](https://developers.etsy.com/documentation/reference/#operation/getPaymentAccountLedgerEntryPayments) / GET | `ledger_entry_ids` |  | transactions_r |
| `etsy_get_payments` | [getPayments](https://developers.etsy.com/documentation/reference/#operation/getPayments) / GET | `payment_ids` |  | transactions_r |
| `etsy_get_properties_by_buyer_taxonomy_id` | [getPropertiesByBuyerTaxonomyId](https://developers.etsy.com/documentation/reference/#operation/getPropertiesByBuyerTaxonomyId) / GET | `taxonomy_id` |  |  |
| `etsy_get_properties_by_taxonomy_id` | [getPropertiesByTaxonomyId](https://developers.etsy.com/documentation/reference/#operation/getPropertiesByTaxonomyId) / GET | `taxonomy_id` |  |  |
| `etsy_get_reviews_by_listing` | [getReviewsByListing](https://developers.etsy.com/documentation/reference/#operation/getReviewsByListing) / GET | `listing_id` |  |  |
| `etsy_get_reviews_by_shop` | [getReviewsByShop](https://developers.etsy.com/documentation/reference/#operation/getReviewsByShop) / GET | `shop_id` |  |  |
| `etsy_get_seller_taxonomy_nodes` | [getSellerTaxonomyNodes](https://developers.etsy.com/documentation/reference/#operation/getSellerTaxonomyNodes) / GET |  |  |  |
| `etsy_get_shipping_carriers` | [getShippingCarriers](https://developers.etsy.com/documentation/reference/#operation/getShippingCarriers) / GET | `origin_country_iso` |  |  |
| `etsy_get_shop` | [getShop](https://developers.etsy.com/documentation/reference/#operation/getShop) / GET | `shop_id` |  |  |
| `etsy_get_shop_by_owner_user_id` | [getShopByOwnerUserId](https://developers.etsy.com/documentation/reference/#operation/getShopByOwnerUserId) / GET | `user_id` |  |  |
| `etsy_get_shop_payment_account_ledger_entries` | [getShopPaymentAccountLedgerEntries](https://developers.etsy.com/documentation/reference/#operation/getShopPaymentAccountLedgerEntries) / GET | `min_created`, `max_created` |  | transactions_r |
| `etsy_get_shop_payment_account_ledger_entry` | [getShopPaymentAccountLedgerEntry](https://developers.etsy.com/documentation/reference/#operation/getShopPaymentAccountLedgerEntry) / GET | `ledger_entry_id` |  | transactions_r |
| `etsy_get_shop_payment_by_receipt_id` | [getShopPaymentByReceiptId](https://developers.etsy.com/documentation/reference/#operation/getShopPaymentByReceiptId) / GET | `receipt_id` |  | transactions_r |
| `etsy_get_shop_production_partners` | [getShopProductionPartners](https://developers.etsy.com/documentation/reference/#operation/getShopProductionPartners) / GET |  |  | shops_r |
| `etsy_get_shop_readiness_state_definition` | [getShopReadinessStateDefinition](https://developers.etsy.com/documentation/reference/#operation/getShopReadinessStateDefinition) / GET | `readiness_state_definition_id` |  | shops_r |
| `etsy_get_shop_readiness_state_definitions` | [getShopReadinessStateDefinitions](https://developers.etsy.com/documentation/reference/#operation/getShopReadinessStateDefinitions) / GET |  |  | shops_r |
| `etsy_get_shop_receipt` | [getShopReceipt](https://developers.etsy.com/documentation/reference/#operation/getShopReceipt) / GET | `receipt_id` |  | transactions_r |
| `etsy_get_shop_receipt_transaction` | [getShopReceiptTransaction](https://developers.etsy.com/documentation/reference/#operation/getShopReceiptTransaction) / GET | `transaction_id` |  | transactions_r |
| `etsy_get_shop_receipt_transactions_by_listing` | [getShopReceiptTransactionsByListing](https://developers.etsy.com/documentation/reference/#operation/getShopReceiptTransactionsByListing) / GET | `listing_id` |  | transactions_r |
| `etsy_get_shop_receipt_transactions_by_receipt` | [getShopReceiptTransactionsByReceipt](https://developers.etsy.com/documentation/reference/#operation/getShopReceiptTransactionsByReceipt) / GET | `receipt_id` |  | transactions_r |
| `etsy_get_shop_receipt_transactions_by_shop` | [getShopReceiptTransactionsByShop](https://developers.etsy.com/documentation/reference/#operation/getShopReceiptTransactionsByShop) / GET |  |  | transactions_r |
| `etsy_get_shop_receipts` | [getShopReceipts](https://developers.etsy.com/documentation/reference/#operation/getShopReceipts) / GET |  |  | transactions_r |
| `etsy_get_shop_return_policies` | [getShopReturnPolicies](https://developers.etsy.com/documentation/reference/#operation/getShopReturnPolicies) / GET | `shop_id` |  |  |
| `etsy_get_shop_return_policy` | [getShopReturnPolicy](https://developers.etsy.com/documentation/reference/#operation/getShopReturnPolicy) / GET | `shop_id`, `return_policy_id` |  |  |
| `etsy_get_shop_section` | [getShopSection](https://developers.etsy.com/documentation/reference/#operation/getShopSection) / GET | `shop_id`, `shop_section_id` |  |  |
| `etsy_get_shop_sections` | [getShopSections](https://developers.etsy.com/documentation/reference/#operation/getShopSections) / GET | `shop_id` |  |  |
| `etsy_get_shop_shipping_profile` | [getShopShippingProfile](https://developers.etsy.com/documentation/reference/#operation/getShopShippingProfile) / GET | `shipping_profile_id` |  | shops_r |
| `etsy_get_shop_shipping_profile_destinations_by_shipping_profile` | [getShopShippingProfileDestinationsByShippingProfile](https://developers.etsy.com/documentation/reference/#operation/getShopShippingProfileDestinationsByShippingProfile) / GET | `shipping_profile_id` |  | shops_r |
| `etsy_get_shop_shipping_profile_upgrades` | [getShopShippingProfileUpgrades](https://developers.etsy.com/documentation/reference/#operation/getShopShippingProfileUpgrades) / GET | `shipping_profile_id` |  | shops_r |
| `etsy_get_shop_shipping_profiles` | [getShopShippingProfiles](https://developers.etsy.com/documentation/reference/#operation/getShopShippingProfiles) / GET |  |  | shops_r |
| `etsy_get_user` | [getUser](https://developers.etsy.com/documentation/reference/#operation/getUser) / GET |  |  | email_r |
| `etsy_get_user_address` | [getUserAddress](https://developers.etsy.com/documentation/reference/#operation/getUserAddress) / GET | `user_address_id` |  | address_r |
| `etsy_get_user_addresses` | [getUserAddresses](https://developers.etsy.com/documentation/reference/#operation/getUserAddresses) / GET |  |  | address_r |
| `etsy_ping` | [ping](https://developers.etsy.com/documentation/reference/#operation/ping) / GET |  |  |  |
| `etsy_token_scopes` | [tokenScopes](https://developers.etsy.com/documentation/reference/#operation/tokenScopes) / POST |  |  |  |
| `etsy_update_holiday_preferences` | [updateHolidayPreferences](https://developers.etsy.com/documentation/reference/#operation/updateHolidayPreferences) / PUT | `holiday_id`, `body`, `confirm` | `is_working` | shops_w |
| `etsy_update_listing` | [updateListing](https://developers.etsy.com/documentation/reference/#operation/updateListing) / PATCH | `listing_id`, `body`, `confirm` |  | listings_w |
| `etsy_update_listing_inventory` | [updateListingInventory](https://developers.etsy.com/documentation/reference/#operation/updateListingInventory) / PUT | `listing_id`, `body`, `confirm` | `products` | listings_w |
| `etsy_update_listing_personalization` | [updateListingPersonalization](https://developers.etsy.com/documentation/reference/#operation/updateListingPersonalization) / POST | `listing_id`, `body`, `confirm` | `personalization_questions` | listings_w |
| `etsy_update_listing_property` | [updateListingProperty](https://developers.etsy.com/documentation/reference/#operation/updateListingProperty) / PUT | `listing_id`, `property_id`, `body`, `confirm` | `value_ids`, `values` | listings_w |
| `etsy_update_listing_translation` | [updateListingTranslation](https://developers.etsy.com/documentation/reference/#operation/updateListingTranslation) / PUT | `listing_id`, `language`, `body`, `confirm` | `title`, `description` | listings_w |
| `etsy_update_shop` | [updateShop](https://developers.etsy.com/documentation/reference/#operation/updateShop) / PUT | `body`, `confirm` |  | shops_r, shops_w |
| `etsy_update_shop_readiness_state_definition` | [updateShopReadinessStateDefinition](https://developers.etsy.com/documentation/reference/#operation/updateShopReadinessStateDefinition) / PUT | `readiness_state_definition_id`, `body`, `confirm` |  | shops_w |
| `etsy_update_shop_receipt` | [updateShopReceipt](https://developers.etsy.com/documentation/reference/#operation/updateShopReceipt) / PUT | `receipt_id`, `body`, `confirm` |  | transactions_w |
| `etsy_update_shop_return_policy` | [updateShopReturnPolicy](https://developers.etsy.com/documentation/reference/#operation/updateShopReturnPolicy) / PUT | `return_policy_id`, `body`, `confirm` | `accepts_returns`, `accepts_exchanges` | shops_w |
| `etsy_update_shop_section` | [updateShopSection](https://developers.etsy.com/documentation/reference/#operation/updateShopSection) / PUT | `shop_section_id`, `body`, `confirm` | `title` | shops_w |
| `etsy_update_shop_shipping_profile` | [updateShopShippingProfile](https://developers.etsy.com/documentation/reference/#operation/updateShopShippingProfile) / PUT | `shipping_profile_id`, `body`, `confirm` |  | shops_w |
| `etsy_update_shop_shipping_profile_destination` | [updateShopShippingProfileDestination](https://developers.etsy.com/documentation/reference/#operation/updateShopShippingProfileDestination) / PUT | `shipping_profile_id`, `shipping_profile_destination_id`, `body`, `confirm` |  | shops_w |
| `etsy_update_shop_shipping_profile_upgrade` | [updateShopShippingProfileUpgrade](https://developers.etsy.com/documentation/reference/#operation/updateShopShippingProfileUpgrade) / PUT | `shipping_profile_id`, `upgrade_id`, `body`, `confirm` |  | shops_w |
| `etsy_update_variation_images` | [updateVariationImages](https://developers.etsy.com/documentation/reference/#operation/updateVariationImages) / POST | `listing_id`, `body`, `confirm` | `variation_images` | listings_w |
| `etsy_upload_listing_file` | [uploadListingFile](https://developers.etsy.com/documentation/reference/#operation/uploadListingFile) / POST | `listing_id`, `body`, `confirm` |  | listings_w |
| `etsy_upload_listing_image` | [uploadListingImage](https://developers.etsy.com/documentation/reference/#operation/uploadListingImage) / POST | `listing_id`, `body`, `confirm` |  | listings_w |
| `etsy_upload_listing_video` | [uploadListingVideo](https://developers.etsy.com/documentation/reference/#operation/uploadListingVideo) / POST | `listing_id`, `body`, `confirm` |  | listings_w |

## Known upstream boundaries

`etsy_get_listing_property` is documented as under development/501: use `etsy_get_listing_properties`.
`etsy_get_listing_video` may return an empty result: use `etsy_get_listing_videos`.
Inventory/personalization replacement and media uploads require domain checks beyond schema validity.
Readback after accepted writes is mandatory before claiming verified state. No automatic retries of uncertain writes.
