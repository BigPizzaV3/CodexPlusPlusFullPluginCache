<catalog_brief>
name: ReducedPriceWishlist
full_name: Discount on Wishlist Items
description: Notify users about price drops on products added to the wishlist.
variant: omnichannel
</catalog_brief>

<trigger_instruction>
<brief>
Brief:
This is a trigger for reducing the price of a product from the wishlist. The main goal is to stimulate the client to purchase the product that he added to his favorites by motivating him with a discount that appeared on this product. Communication is carried out by sending up to 3 messages to different channels.
</brief>

<start_trigger>
It should start for discount wishlist segment once a day (any day of week) starting from tomorrow at 09:00, but no more than once a week for the specific contact.
</start_trigger>

<generation_plan>
The main flow should follow:
Start by sending a web push
Next step, send an email
Wait 24 hours
Send SMS, only when this channel and a valid message are available in the selected Reteno account
End of script
</generation_plan>
</trigger_instruction>
