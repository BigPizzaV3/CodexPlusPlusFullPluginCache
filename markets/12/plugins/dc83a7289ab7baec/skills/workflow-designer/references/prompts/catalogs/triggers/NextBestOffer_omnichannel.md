<catalog_brief>
name: NextBestOffer
full_name: Next Best Offer
description: Recommend complementary or frequently bought together products.
variant: omnichannel
</catalog_brief>

<trigger_instruction>
<brief>
Brief:
This is a next best offer trigger. The main goal is to recommend additional products that can complement the purchased ones or that are often purchased together with the purchased ones. Communication is carried out by sending up to 3 messages to different channels.
</brief>

<start_trigger>
It should start for next best offer segment once an hour starting from tomorrow, but no more than once a week for the specific contact.
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
