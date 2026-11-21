# VanReceipts plugin privacy (draft)

This is a draft for the owner to publish. It describes the VanReceipts plugin that drafts an estimate, quote, or invoice, and that stores a before and after slider. It does not describe a different product.

Contact: support@vanreceipts.app

The address above is the contact already printed on the vanreceipts.app template pages. The canonical facts sheet does not list an email row.

## What this plugin is

VanReceipts checks the price lines you send and computes the total. It can also keep two photos so a slider and a share link work. There is no account. The plugin does not read the books kept in the iPhone app.

## What we collect

Document fields you choose to print: business name, client name, optional contact or address text you typed, dates, and the lines. We use them to check the sources and compute the total, then return them to the chat. We do not store the document.

For a slider: the two photos, whether the after photo is a concept, the time we stored them, and a random delete token. We give the delete link to the uploader once. The photo store keeps a hash of that token, not the token itself. We use the photos to show the slider and the hash to check a delete.

A counter stores only the tool name, the trade, the document kind, and the day. It does not store names, lines, totals, photos, or the text of the chat.

## What we do not collect

Card numbers, bank details, or pay links. Device location. We remove location metadata from photos on upload. A photo where a person is the subject should not be uploaded.

## How long we keep it

Document contents are not kept after the reply is sent.

Slider photos are kept until you open the delete link, or for 30 days, whichever comes first. After that the files are deleted. The share link is a long random id. Someone who does not have the link cannot list the photos.

The counter is a short operational log of tool name, trade, document kind, and day.

## Who receives it

The chat host sends the tool request to the VanReceipts server so the check, the total, or the slider can be returned to you. Photo files are stored with Vercel Blob when that storage is configured. The blob name is the same random id. We do not sell this information, and we do not use it to pitch a plan.

## Your choices

Open the delete link to remove the photos before 30 days. Email support@vanreceipts.app to ask about the counter or a slider that the delete link did not clear.

## Published copy

The published version is https://vanreceipts.app/plugin-privacy (`legal/plugin-privacy.html`). Use that URL in both directory listings. Change both files together.
