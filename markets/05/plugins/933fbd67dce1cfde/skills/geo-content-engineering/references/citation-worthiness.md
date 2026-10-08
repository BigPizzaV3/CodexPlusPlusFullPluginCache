# Citation-worthiness

Fact density and proprietary data that push a model to cite you during grounding.

## The mechanic: grounding

To avoid hallucinating, a model looks for support in the retrieved material:
concrete numbers, conditions, checkable statements. High-density content gets
extracted and attached to a direct citation. Content with no evidentiary value
gets paraphrased or ignored.

## Rules

1. **Concrete numbers over vague claims.** Name metrics, percentages, ranges,
   prices, and technical parameters. "Much faster" is worthless; "42 percent
   lower load time" is quotable.

2. **Hard-to-reproduce proprietary data.** Use your own market tests, internal
   analyses, and documented case studies. Data that exists nowhere else makes
   your page the only possible source.

3. **Text anchors for multimedia.** Models extract text. Duplicate the key
   statement of any chart, calculator, or interactive element in the body text:
   "The calculator shows a saving of X percent." Without a text anchor, the
   related block loses its meaning on extraction (see `chunking.md`).

## Connection to off-page

Grounding does not rely only on your page. It also draws on external sources that
write about the brand. The off-page side of this mechanic is in
`offpage-mentions.md`.
