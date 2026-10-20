# Readability reference for WAHA messages

Phone screens punish long text. These patterns keep messages scannable.

## Structure

1. Point first: the news, date, amount, or ask in line one.
2. Blank line, then at most three short supporting lines.
3. Blank line, then the single next step (link, reply keyword, or choice).
4. Opt-out line for promo or recurring sends.

## Patterns

**Notification:**

```text
Hi Andi, *order A-1042* has shipped.

Track it here: https://example.com/t/A-1042

Reply HELP if you need support.
```

**Reminder:**

```text
Reminder: *dental checkup tomorrow at 10:00*.

Reply:
1. YES to confirm
2. RESCHEDULE for a new time
```

**Short promo (opt-in list only):**

```text
*Weekend deal for members:* 20% off all coffee beans until Sunday.

Shop: https://example.com/weekend

Reply STOP to opt out.
```

**Group mention:**

```text
Hi team, standup moved to *09:30* today. @628111111111 please share the board link.
```

with `mentions: ["628111111111@c.us"]`.

## Rules

- One message, one idea, one ask.
- Keep the opener under 200 characters.
- Break after 4 to 6 lines; continue in a second message only after a reply.
- Numbers, dates, and names in bold; context in plain text.
- Label every link with what opens behind it.
- Read it on a narrow screen before sending: if you scroll, shorten it.
