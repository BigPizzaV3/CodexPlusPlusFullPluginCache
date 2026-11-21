# Business Profile: every operation

Generated from the tools' own descriptions. "Tool" is the platform tool that runs the operation on grouped connections (operation=<name>, params=<arguments>); on connections that list every operation as its own tool, call the operation name directly.

## Read (changes nothing)

| Operation | Tool | Use it when |
|---|---|---|
| `gbp_insights` | business_profile_read | Asks how customers find and act on their Google Business Profile: views, calls, direction requests and website clicks. |
| `gbp_list_locations` | business_profile_read | Wants the business locations of their connected Google Business Profile accounts. |
| `gbp_list_posts` | business_profile_read | Wants the published posts of a Google Business Profile location. |
| `gbp_location_details` | business_profile_read | Wants all details of one Google Business Profile location. |
| `gbp_reviews` | business_profile_read | Wants the Google reviews of a business location and whether each one was answered. |
| `gbp_search_categories` | business_profile_read | Needs Google Business Profile category IDs by name. |
| `gbp_search_keywords` | business_profile_read | Asks which searches people used before finding their Google Business Profile on Search and Maps. |
| `gbp_verification_options` | business_profile_read | Asks which verification methods Google offers for a Business Profile listing. |
| `list_business_profile_photos` | business_profile_read | Wants the photos on a Google Business Profile location. |

## Add (preview, then confirm)

| Operation | Tool | Use it when |
|---|---|---|
| `connect_business_profile` | google_ads_create | Wants to connect a Google Business Profile so its listing, posts and reviews can be managed. |
| `gbp_create_location` | business_profile_create | Wants to create a new Google Business Profile listing. |
| `gbp_upload_photo` | business_profile_create | Wants to add photos to their Google Business Profile. |
| `gbp_upload_video` | business_profile_create | Wants to add a video to their Google Business Profile. |
| `google_ads_add_location_assets` | business_profile_create | Wants to attach Google Business Profile location assets (address, map pin, directions) to Google Ads campaigns. |

## Change, pause or delete (preview, then confirm)

| Operation | Tool | Use it when |
|---|---|---|
| `gbp_complete_verification` | business_profile_edit | Has a Google Business Profile verification code and wants to submit it. |
| `gbp_create_post` | business_profile_edit | Wants to publish an update post on their Google Business Profile. |
| `gbp_delete_post` | business_profile_edit | Wants to permanently delete a Google Business Profile post. |
| `gbp_manage_services` | business_profile_edit | Wants to read or change the services list on a Google Business Profile. |
| `gbp_reply_review` | business_profile_edit | Wants to write or update a public reply to a Google review. |
| `gbp_social_links` | business_profile_edit | Wants to read or set the social media links of a Google Business Profile. |
| `gbp_start_verification` | business_profile_edit | Wants to start a Google Business Profile verification method. |
| `gbp_update_location` | business_profile_edit | Wants to change their Google Business Profile listing: name, hours, phone, website, description, categories or service areas. |
| `gbp_update_photo_category` | business_profile_edit | Wants to change the category of a photo already on their Google Business Profile. |
| `gbp_update_post` | business_profile_edit | Wants to edit a published Google Business Profile post. |
