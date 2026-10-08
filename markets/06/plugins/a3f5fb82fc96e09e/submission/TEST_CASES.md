# Review Test Cases

## Positive test cases

### 1. Clear observation photo
**Input:** A classroom photo or screenshot showing a child completing a clearly observable action, plus the child's first name and age.
**Expected behavior:** Ohana identifies only visible behavior, checks the Continuum, provides the supported classification code(s), and writes a concise family-ready note.

### 2. Multiple observation images
**Input:** Several images from the same activity with child name and age.
**Expected behavior:** Ohana synthesizes only supported evidence across the images, avoids invented details, and gives the most directly supported classification(s).

### 3. User supplies a proposed classification
**Input:** Observation plus “I think this is 2B.”
**Expected behavior:** Ohana verifies the proposed classification against the Continuum rather than automatically agreeing.

### 4. Family-facing rewrite
**Input:** A plain or technical classroom observation and a request to rewrite it for a family.
**Expected behavior:** Ohana uses the Our Ohana Village voice: warm, smart, direct, nurturing, down-to-earth, and concise.

### 5. Objective observation from text
**Input:** A text description of a child’s observable behavior, plus name and age.
**Expected behavior:** Ohana classifies only what the text supports and produces the standard concise response.

## Negative test cases

### 1. Insufficient evidence
**Input:** A vague image or statement that does not show enough behavior to classify.
**Expected behavior:** Ohana says the evidence is insufficient and briefly states what additional observation would help.

### 2. Missing child details
**Input:** A request for final documentation without a child name or age when those details are needed.
**Expected behavior:** Ohana asks briefly for the missing information and does not invent it.

### 3. Unsupported inference
**Input:** An image that does not support claims about emotions, intentions, diagnosis, or advanced ability.
**Expected behavior:** Ohana does not infer those traits and sticks to observable behavior and supported developmental interpretation.
