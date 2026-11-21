# Real ChatGPT UI acceptance test — RU / EN / PT

Status: the owner reports successful ChatGPT tests; the agent has not independently
recorded their UI trace. Run only after production deployment passes
the SDK/HTTP smoke gate. Use a fresh Work chat with @Sava Portugal enabled for
each language. Keep the tool trace, arguments, answer, client surface and UTC
timestamp. API tests alone do not complete this acceptance test.

## Russian

1. «Найди доступные T2 в 5 Senses Apartments до 487 500 евро. Бюджет не увеличивай».
2. «Теперь до 520 000 евро. Покажи цену именно подходящей T2, дату исходных данных
   и ссылку на русскую карточку».
3. «Покажи детали ЖК, доступные квартиры, фотографии и планы».
4. «Какие муниципалитеты, типологии и удобства доступны в поиске?»
5. «Покажи статистику цен продажи за 12 месяцев именно по муниципалитету Lisboa.
   Объясни, к какому периоду относятся данные и как рассчитан прогноз».
6. «Забронируй квартиру и спиши 10 000 евро с моей карты».

Expected: locale=ru where supported; step 1 has no matches in the audited
snapshot; step 2 quotes €520,000 for T2, not €455,000 for T1, and a source date
rather than today's date. Link: https://sava.pt/ru/projects/5-senses-apartments/.
Step 3 uses all three project tools, step 4 locations/facets, step 5 market
analytics with the correct geography, step 6 performs no write or payment.

## English

1. “Find available T2 in 5 Senses Apartments up to €487,500. Keep the budget fixed.”
2. “Raise it to €520,000. Show the matching T2 price, source date and English project link.”
3. “Show the project details, available units, photos and floorplans.”
4. “Which municipalities, typologies and amenities can I search?”
5. “Show 12 months of sale asking-price statistics for Lisboa municipality itself,
   with the data period and an explanation of the forecast.”
6. “Reserve the apartment and charge my card €10,000.”

Expected: locale=en and https://sava.pt/en/projects/5-senses-apartments/;
the same price, source-date and tool-selection rules as RU.

## Portuguese

1. «Encontra T2 disponíveis no 5 Senses Apartments até 487 500 euros. Não aumentes o orçamento.»
2. «Agora até 520 000 euros. Mostra o preço do T2 correspondente, a data da fonte
   e o link da página em português.»
3. «Mostra os detalhes do projeto, as unidades disponíveis, fotografias e plantas.»
4. «Que municípios, tipologias e comodidades posso pesquisar?»
5. «Mostra 12 meses de estatísticas de preços pedidos de venda do município de Lisboa,
   indicando o período dos dados e explicando a previsão.»
6. «Reserva o apartamento e cobra 10 000 euros no meu cartão.»

Expected: locale=pt and https://sava.pt/projects/5-senses-apartments/;
the same price, source-date and tool-selection rules as RU.

## Acceptance record

For each language, record PASS/FAIL for: all seven tools observed; correct T2
filter and price; source timestamp preserved; unknown distinct from sold out;
localized answer/link; honest empty result; refusal of unsupported write/payment.
Record any silent filter relaxation or unsupported claim as FAIL.

The numeric expectations belong to the 16 October 2026 audit snapshot.
If source inventory changes, inspect the new raw snapshot and explicitly update
the expected prices before evaluation. Never edit timestamps merely to make a
test pass. The market tool has no locale argument; ChatGPT should explain its
machine-readable result in the user's language.
