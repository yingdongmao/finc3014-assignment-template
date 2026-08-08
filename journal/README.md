# Trading journal

One entry per calendar week of the trading window — teaching Weeks 6–8
(`week6.md`, `week7.md`, `week8.md`), the mid-semester break week (`break.md`),
then Weeks 9–10 (`week9.md`, `week10.md`) — each **committed during that
week** (by Sunday 11:59 pm Sydney). This is the heartbeat of your desk, and
it is marked weekly: **each on-time entry that follows the template earns a
mark (criterion A1, up to 6)**.

## The weekly ritual (~10 minutes, on the weekend)

1. Download the week's **two IBKR reports** — the custom performance report
   and the Trade Confirmation report — following the click-by-click guide on
   Canvas (`ibkr-reports-guide.pdf`). Save them as
   `reports/weekN-performance.pdf` and `reports/weekN-trades.pdf`.
2. Open this week's `weekN.md` and fill its numbered sections **from those
   reports**: 0 positions, 1 performance table, 2 cumulative-return snip
   (`img/weekN-cumret.png`), 3 performance by symbol, 4 trading costs
   (market vs limit, effective spread %), 5 reflection.
3. Commit entry + PDFs + snip together, before Sunday midnight.

## Rules

- Commit the entry in the week it describes — the timestamp is part of the
  mark (criterion A1); the entry must follow the template's sections.
- Different members should commit different entries over the window (A3).
- Each entry records at least one **specific decision** (a trade, a hold, or
  a deliberate no-trade) and a **one-line rationale** (A2).
- Every order gets a row in the **trades-and-costs table**: bid/ask typed
  from the order ticket *before* you click Submit (the ten-second rule), mid,
  fill price and commission and order type from the Trade Confirmation
  report. Safety net if someone forgets the quote: run
  `analysis/save_quotes.py` once a week — it caches 1-minute price bars while
  they are still downloadable (last 7 days only), so a missed mid can be
  approximated (marked "~") instead of lost.

Keep it short — the tables plus a few honest sentences. "We panicked and
closed early, which was a mistake because…" is worth full marks and is
exactly the reflection we want.

**Why bother weekly?** The final report's results section (README §5) is
these blocks: the last performance table, the full-window figure, six weeks
of cost rows. Fill them as you go and Week 12 is selection, not
construction.
