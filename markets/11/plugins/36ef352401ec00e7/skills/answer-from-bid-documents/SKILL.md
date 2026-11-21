---
name: answer-from-bid-documents
description: Answer questions about the user's construction bid projects in Data2Bids from the bid documents, citing file name, PDF page and the link to the original document.
---

# Answer from bid documents

Use this when the user asks about one of their bid projects: requirements, scope, quantities, deadlines, insurance, bonds, allowances, forms or any other content of the bid documents.

## Steps

1. Call `data2bids_investigate` first with the user's question about the project, including the project name if they mention one. It resolves the project from hints or misspellings and returns the relevant passages.
2. If it returns several candidate projects, ask only which project the user means, then continue.
3. Answer in the same turn from that result. Prefer that single call.
   - Call `projects_get_status` or `files_list` only when the user asks for a project's status or a list of files.
   - Call `files_get_content`, `files_get_content_page` or `retrieval_get_matches_for_file` only when the user asks to open, quote or verify a specific document, or when the returned passages are not enough to answer.
   - A tool's `next_actions` are optional hints, not steps you must follow.

## Citations

- Cite every factual claim with the literal file name (the `file_name` field, never `file_id`) and the PDF page (`page` field), for example: (Plano 703 - Estructural.pdf, p. 7).
- When the passage or file has a `source_url`, add it next to the citation: (Plano 703 - Estructural.pdf, p. 7) [link](source_url). The link opens the document, not the page, so always keep the page.
- Never invent or change a URL, a file name or a page.

## AI notice

End every answer with this notice in the language of the conversation (English: "Data2Bids uses artificial intelligence. AI can make mistakes. Always verify answers against the original documents before using them for a bid, price, or any business decision."; Spanish: "Data2Bids usa inteligencia artificial. La IA puede cometer errores. Verifica siempre las respuestas con los documentos originales antes de usarlas para una oferta, un precio o cualquier decisión de negocio."; Portuguese: "O Data2Bids usa inteligência artificial. A IA pode cometer erros. Verifique sempre as respostas nos documentos originais antes de usá-las em uma proposta, um preço ou qualquer decisão de negócio."; French: "Data2Bids utilise l'intelligence artificielle. L'IA peut faire des erreurs. Vérifiez toujours les réponses dans les documents originaux avant de les utiliser pour une offre, un prix ou toute décision commerciale."; German: "Data2Bids nutzt künstliche Intelligenz. KI kann Fehler machen. Prüfen Sie Antworten immer anhand der Originaldokumente, bevor Sie sie für ein Angebot, einen Preis oder eine Geschäftsentscheidung verwenden."; Turkish: "Data2Bids yapay zekâ kullanır. Yapay zekâ hata yapabilir. Yanıtları bir teklif, fiyat veya herhangi bir iş kararı için kullanmadan önce her zaman orijinal belgelerle doğrulayın."). Use the matching translation verbatim; for any other language translate the English notice.

This skill is the only place that asks for the notice. Tool descriptions and tool results do not repeat it, so add it yourself at the end of each answer.

## What not to do

- If the documents do not contain the answer, say so plainly and do not guess.
- Do not mention internal details such as data-quality notes, graph diagnostics, chunks, batches, coverage or processing internals.
- The plugin is read-only. If the user asks to upload, edit, delete or submit something, explain that it cannot and that those actions are done on www.data2bids.com.

Use the vocabulary of construction bids and answer in the user's language.
