# Compliance reference for WAHA sends

WAHA uses a real WhatsApp session, so there is no Meta template review. The risk is account restriction instead. Rules below come from the WAHA "How to Avoid Blocking" guide.

## The core rule

Reply, do not cold blast. The bot should answer messages it receives. Outreach to strangers at volume reads as spam and gets reported, restricted, or banned.

If the contact never talked to you, get opt-in on another channel first (for example, an SMS with a `https://wa.me/<number>?text=Hi` link so they open the chat themselves).

## Send behavior

1. `POST /api/sendSeen` for the chat before processing.
2. `POST /api/startTyping`, wait a random interval scaled to message length.
3. `POST /api/stopTyping`, then `POST /api/sendText`.
4. Never use fixed delays. Randomize gaps (for example, 30 to 60 seconds between first touches), group contacts by area code, and send in packages with rest windows instead of 24/7 blasting.
5. First touch to a new contact: one short message, no links, no media, no follow-ups without consent.

## Content rules

- Only send what the recipient asked for or agreed to. One topic per message.
- Avoid banned words, deceptive urgency, and sensitive or inappropriate content.
- Links must be HTTPS and reputable. Never reuse domains already flagged as spam on WhatsApp.
- Profile must look human: picture, name, and status set before any outreach.
- Every promotional or recurring message needs a visible opt-out (`Reply STOP to opt out`) and you must honor it immediately.

## Restriction signals

- Error `463`: reachout timelock (too many new contacts). Pause outreach to new contacts. Do not restart, logout, or re-pair; it lifts on its own.
- Error `475` with `CAPPED`: per-cycle quota on new contacts. Slow down, watch `FIRST_WARNING` and `SECOND_WARNING`, wait for the cycle reset. Restarting does not help.
- A few spam reports (single digits) can end a number. Reports hurt more than volume.

## Pre-send checklist

- [ ] Recipient opted in or already in conversation
- [ ] First touch is short, no link, no media
- [ ] One ask, opt-out line present for promo or recurring sends
- [ ] Links are HTTPS, labeled, reputable
- [ ] Human pacing planned (seen, typing, random gaps, rest windows)
- [ ] Sender profile has picture, name, status
