# Formatting reference for WAHA messages

WAHA forwards `text` to WhatsApp unchanged, so WhatsApp native formatting applies. Verified against WhatsApp formatting docs and GREEN-API formatting reference.

## Marks

| Rendered | Type this | Notes |
| --- | --- | --- |
| *Italic* | `_Italic_` | Underscores around the span, use sparingly |
| **Bold** | `*bold*` | Asterisks around the span, max two short spans per message |
| ~~Strike~~ | `~strike~` | Tildes, corrections only |
| Monospace block | Triple backticks around the block | Codes, tokens, exact strings to copy |
| `Inline code` | Single backticks around the span | Short codes inside a sentence |
| Quoted line | `> text` at line start | Context or quoted reply |
| Bulleted list | `- item` or `* item` per line | Choice lists, one option per line |
| Numbered list | `1. item` per line | Steps in order |

To show a literal mark character, double it without spaces (for example, doubled underscores to show an underscore instead of starting italics).

## Control characters in JSON payloads

Inside the `text` string of the WAHA request:

- `\n` line break between blocks, use blank line (`\n\n`) between sections
- Keep lines short, phones wrap around 35 to 40 characters
- Quotes inside JSON strings need escaping (`\"`)

## WAHA-specific fields that affect rendering

- `linkPreview: false` suppresses automatic link previews when the preview is wrong or noisy
- `linkPreview: true` plus `linkPreviewHighQuality: true` enables a full preview when the link card matters
- Captions on `POST /api/sendImage` follow the same marks, keep them to two lines plus one ask
- Mentions in groups require both `@<number>` in the text and the matching entry in `mentions`
- Images send best as JPEG (`image/jpeg`); convert before sending, WAHA has no image convert flag (voice and video do have a `convert` option)

## Anti-patterns

- Bold whole paragraphs (renders as shouting, nothing stands out)
- More than one ask per message (pick the single next step)
- Walls of text over 6 lines without a break (split into two messages with a pause)
- Links without telling the reader what opens (label every link)
