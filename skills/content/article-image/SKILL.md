---
name: article-image
description: Illustrate a blog paragraph with a custom header or inline image rendered in one consistent house style. Use when asked to illustrate a blog post, article, changelog entry, or essay with a header or inline image.
---

# Article Image

Generate one image from the paragraph it accompanies: read the paragraph for its concrete nouns and mood, pick (or accept) one of the house styles below, render once, and deliver a web-ready file with a descriptive filename and alt text.

Original implementation. Functional scope is inspired by the Paralect skills catalog (https://www.paralect.com/skills/article-image). Not affiliated with Paralect. No Paralect text, prompts, or code are reused here.

## Workflow

### 1. Collect inputs

Need: the paragraph (or its draft). Optional: house style override and aspect (wide 16:9 for headers, square for inline). If no style arrives, pick from the paragraph mood: technical topics lean blueprint or isometric, opinion pieces lean ink sketch or comic, product news leans desk scene or color block.

### 2. Pick a house style

One style per post; consistency across a blog matters more than novelty per image:

1. Hand drawn ink sketch: loose pen lines, crosshatch shade, paper tone.
2. Retro comic illustration: bold inks, halftone dots, limited palette.
3. Isometric illustration: clean 3D blocks on a grid, soft shadows.
4. Technical blueprint: white linework on deep blue, annotations, measurements.
5. Color block outline: flat color fields with heavy dark outlines.
6. Grainy isometric: isometric forms with film grain and muted tones.
7. Gradient grain: smooth gradient fields with grain overlay, abstract.
8. Isometric desk scene: tiny workspace diorama of the topic.

### 3. Render from the paragraph, not from keywords

Build the prompt from concrete nouns in the text (the objects, the setting, the action), never from the post title alone. Exclude: text in the image (no words, no logos, no UI screenshots), photorealistic faces, and anything the paragraph does not support. Render at the target aspect in one pass.

### 4. Verify and deliver

Check: no garbled text, style matches the house pick, readable at 800px wide and at thumbnail size, under 500KB as JPEG quality 82 or WebP. Save as `slug-style.jpg` next to the post with one line alt text describing the image for screen readers. On failure (text artifacts, wrong mood), adjust the prompt once and re-render; do not batch five variants and ask the caller to choose.

## Boundaries

Editorial illustration for articles. For brand marks, use `saas-logo`. For product UI mocks, use the `design` bucket. For share cards with headlines and meta tags, use `og-image`.
