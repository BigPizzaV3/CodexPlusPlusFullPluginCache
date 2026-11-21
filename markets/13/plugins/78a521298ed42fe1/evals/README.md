# ChatGPT tool evaluation corpus

`eval_corpus.json` is the machine-readable source of truth for the fixed-date
golden prompts. `evaluate_corpus.py` validates the corpus and can score
caller-supplied, externally recorded ChatGPT traces without making network
calls. Tests under `tests/` load the same JSON file rather than maintaining a
second copy of the fixtures.

The tool sequence is intentionally exact. Activation, missed activation, and
sequence-match results are also reported separately for each fixture category
so that the 30/30/20/20 category balance remains visible in aggregate results.
