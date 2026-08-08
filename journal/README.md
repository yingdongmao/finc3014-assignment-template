# Trading journal

One entry per calendar week of the trading window — teaching Weeks 6–8
(`week6.md`, `week7.md`, `week8.md`), the mid-semester break week (`break.md`),
then Weeks 9–10 (`week9.md`, `week10.md`) — each **committed during that
week**. This is the heartbeat of your desk: a short, honest record of what you
did and *why*.

- Commit the entry in the week it describes — the timestamp is part of the mark
  (criterion A1).
- Different members should commit different entries over the window (A3).
- Each entry must record at least one **specific decision** (a trade, a hold,
  or a deliberate no-trade) and a **one-line rationale** (A2).
- Every fill also gets a row in the **trades-and-costs table**: bid/ask typed
  from the order ticket *before* you click Submit (the ten-second rule), mid,
  fill price, commission. These rows are the raw inputs for your execution-cost
  analysis (report §5.3, criterion C9). Safety net if someone forgets: run
  `analysis/save_quotes.py` once a week — it caches 1-minute price bars while
  they are still downloadable (last 7 days only), so a missed mid can be
  approximated (marked "~") instead of lost.

Use the structure already in each `weekN.md` file. Keep it short — half a page
is plenty. Honesty beats polish: "we panicked and closed early, which was a
mistake because…" is worth full marks and is exactly the reflection we want.
