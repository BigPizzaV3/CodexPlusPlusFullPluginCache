---
name: premiers-pas
description: Welcomes a person who has just installed Spartadoc and explains, in their language, how to have a document read by the AI with its personal information redacted first. Use right after installation, or when the person asks how Spartadoc works.
---

# Getting started with Spartadoc

Spartadoc removes personal information (names, addresses, numbers, email addresses, phone numbers) from a document before the AI reads it. The original document never goes through the chat.

Reply in the person's language (French or English). Keep it short: a greeting, the three steps, the condition, then an offer to start.

## The three steps

1. The person asks to read a document that contains personal information (contract, notarial deed, will, financial statements, investment statement, purchase offer). `ouvrir_depot` gives an upload link valid for 15 minutes; where the host shows cards, a Spartadoc card shows the button, the time left and the status.
2. On that page, the person takes a photo of the document or chooses the file, reviews every redacted area, adds or removes areas, then taps "Send to my chat" ("Envoyer à ma discussion"). Nothing reaches the chat before that.
3. The Spartadoc card posts "Done, I sent it" in the chat on its own, and `recuperer_document` returns the redacted text, in which each removed value is a label such as [PERSON_1] ([PERSONNE_1] in French), and the images of the redacted pages. Without the card, the person types "done" ("fait").

## Facts to state

- The link is for the person. It is shown as a clickable link and is not opened by the AI.
- The document goes through that link, not through a file attached to the chat, which would pass on the unredacted original.
- The redacted version is deleted 15 minutes after it is sent. `annuler_depot` cancels an upload and deletes its content.
- Redaction must be enabled for the person's Spartadoc organization. If it is not, the tools say so and give a link to ask for access.
- Settings (`lire_reglages`, `modifier_reglages`): the language of the upload page and labels (auto, French, English) and automatic reading once the document is sent.
- Automatic detection is an aid: the person reviews and confirms what is sent.

## Then

Offer to start with a document now. Do not call `ouvrir_depot` until the person says they have a document to read.

## En français

Spartadoc retire les renseignements personnels d'un document avant que l'IA le lise ; l'original ne passe jamais par la discussion. Trois étapes : `ouvrir_depot` donne un lien de dépôt de 15 minutes (et une carte, là où l'hôte les affiche) ; la personne dépose, vérifie les zones caviardées et touche « Envoyer à ma discussion » ; la carte écrit « C'est envoyé » et `recuperer_document` rend le texte caviardé ([PERSONNE_1]) et l'image des pages, sinon la personne écrit « fait ». Le caviardage doit être activé pour l'organisation Spartadoc de la personne.
