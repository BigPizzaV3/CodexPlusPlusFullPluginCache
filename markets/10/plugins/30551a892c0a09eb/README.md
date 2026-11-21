# Turnpoint — code, as a story

A source-linked code flowchart for JavaScript, TypeScript, JSX and TSX.

Ask: “Use Turnpoint to draw this code change in simple terms.” The code-story skill analyzes supplied source and renders the interactive view. No API key or sign-in required.

Website: https://turnpoint-code.netlify.app
Support: arjun@knoy.app
Publisher: ARJUN AVTANI

For local analysis: `node scripts/analyze.cjs examples/checkout.json story.turnpoint.json`. Open the story in the website’s saved-story input. No network request is made by the local parser.

This is a static source map, not a runtime trace. It does not replace the host’s built-in diff panel.
