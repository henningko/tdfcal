# Tour de France 2026 calendar

ICS calendar for all 21 stages of the [Tour de France 2026](https://www.procyclingstats.com/race/tour-de-france/2026)
(4–26 July). Each event is an all-day entry titled `[TdF] <start> - <finish>` with:

- ⛰️ on mountain stages, 👑 on the queen stage, ⏱️ on time trials (`(TTT)` / `(ITT)`)
- the finish town as the location
- the categorised climbs and a link to ProCyclingStats in the description

## Subscribe (auto-updating)

Point your calendar app at this URL and it stays in sync:

```
https://raw.githubusercontent.com/henningko/tdfcal/main/tdf2026.ics
```

- **Apple Calendar (macOS/iOS)** — open
  `webcal://raw.githubusercontent.com/henningko/tdfcal/main/tdf2026.ics`
  (swapping `https` for `webcal` opens the subscribe dialog directly), or on macOS use
  *File → New Calendar Subscription* and paste the `https://` URL.
- **Google Calendar** (web only) — *Other calendars* → **＋** → *From URL* → paste the `https://` URL.
- **Outlook** — *Add calendar → Subscribe from web* → paste the `https://` URL.

Subscribed calendars are read-only and refresh roughly every 12 hours.

## Import once (no updates)

Prefer a one-time copy? Download [`tdf2026.ics`](tdf2026.ics) and open it, or import individual
stages from the [`stages/`](stages/) folder. Imported events won't update if the route changes.

## Regenerating

The calendar is generated from stage data in [`generate.py`](generate.py):

```sh
python3 generate.py
```

This writes `tdf2026.ics` (combined) and one file per stage under `stages/`. After editing,
commit and push — subscribers pick up the change on their next refresh.

> Climb categories for 2026 are not all officially confirmed; where unconfirmed, each climb is
> assigned the category it traditionally carries.
