# JSON-LD snippets

Paste-ready structured data for the four types this skill uses most. Replace the
bracketed placeholders. Keep JSON-LD in a `<script type="application/ld+json">`
block in the page head or body. It is separate from the visual HTML and is the
easiest structured-data format for machines to process (see
`../references/semantic-html.md`).

## Article

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "[Article title, matching the H1]",
  "description": "[One-sentence summary]",
  "datePublished": "[YYYY-MM-DD]",
  "dateModified": "[YYYY-MM-DD]",
  "author": {
    "@type": "Person",
    "name": "[Author name]",
    "url": "[Author profile page URL]"
  },
  "publisher": {
    "@type": "Organization",
    "name": "[Brand name]",
    "logo": {
      "@type": "ImageObject",
      "url": "[Logo URL]"
    }
  },
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "[Canonical page URL]"
  }
}
</script>
```

Keep `dateModified` truthful and in sync with real updates, not with cosmetic
edits (see `../references/recency.md`).

## Person (author profile page)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "[Author name]",
  "url": "[Author profile page URL]",
  "jobTitle": "[Role]",
  "worksFor": {
    "@type": "Organization",
    "name": "[Brand name]"
  },
  "knowsAbout": ["[Topic 1]", "[Topic 2]", "[Topic 3]"],
  "sameAs": [
    "[LinkedIn URL]",
    "[Other verifiable profile URL]"
  ]
}
</script>
```

The `sameAs` values must match the external profiles exactly. Contradictions
lower trust (see `../references/offpage-mentions.md`).

## FAQPage

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "[Question in the exact phrasing a user would prompt]?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[Answer, first sentence answers fully, entity named]"
      }
    },
    {
      "@type": "Question",
      "name": "[Second question]?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[Answer with a concrete number or range]"
      }
    }
  ]
}
</script>
```

The visible FAQ text on the page and the `text` values must match. See
`faq-block.md`.

## Product with Offer

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "[Product name]",
  "description": "[One-sentence description]",
  "brand": {
    "@type": "Brand",
    "name": "[Brand name]"
  },
  "offers": {
    "@type": "Offer",
    "price": "[Numeric price, no currency symbol]",
    "priceCurrency": "[ISO code, e.g. USD]",
    "availability": "https://schema.org/InStock",
    "url": "[Product page URL]"
  }
}
</script>
```

Keep price and currency consistent with every external surface (directories, app
stores, comparison sites), see `../references/offpage-mentions.md`.

## Validation

Validate before publishing with the Schema.org validator (validator.schema.org)
or Google's Rich Results Test. Invalid JSON-LD is often ignored entirely.
