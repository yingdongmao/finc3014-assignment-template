# Week 6 — trading journal

**Dates covered:** _(fill in)_
**Entry author:** _(your name + GitHub handle)_

## Market context (2–3 sentences)
> What was happening in the markets you care about this week?

## Decisions this week
> At least one specific decision and its one-line rationale. Add a row per decision.

| Decision (trade / hold / no-trade) | Instrument | Rationale (one line) |
|---|---|---|
|  |  |  |

## Trades and costs this week — one row per fill
> **The ten-second rule: type Bid / Ask into this row _before_ you click
> Submit** (read them off the order ticket; a "Delayed" quote still counts as
> your decision-time reference). Typing the two numbers _is_ the record — a
> screenshot is optional extra evidence, not a requirement. Mid = (Bid + Ask) / 2.
> Fill price and commission: Client Portal → **Orders & Trades**, after the fill.
> Forgot the quote? Don't invent it: put "~" in the Bid / Ask cell and
> reconstruct an approximate Mid from the cached 1-minute bars
> (`analysis/save_quotes.py` — run it within 7 days of the trade). No fills
> this week? Write "no fills" and keep the section.

| Date & time | Instrument | Buy/Sell, qty | Order type | Bid / Ask at order | Mid | Fill price | Commission | Cost vs mid (bp) |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |

> **Cost vs mid (bp)** = 10,000 × (Fill - Mid) / Mid for a buy; 10,000 × (Mid - Fill) / Mid
> for a sell. Positive: you paid the half-spread (market orders usually do).
> Negative: price improvement — e.g. your resting limit order filled inside the
> spread. This is the _effective half-spread_; doubled, it is the effective spread
> you compare with the quoted spread (Ask - Bid). These rows are the raw inputs
> for your execution-cost analysis (report §5.3, criterion C9) — collect them
> live, not in Week 11.

## Positions at end of week
> Copy straight off Client Portal → **Portfolio**, which shows exactly these
> columns; cash and total value (Net Liquidation Value) are on the account summary.

| Instrument | Qty | Avg cost | Last price | Market value | Unrealised P&L |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

**Cash:** _(fill in)_ · **Total value (NLV):** _(fill in)_ · **Benchmark since window start:** _(fill in)_

## Reflection (optional but encouraged)
> What surprised you? What would you do differently next week?
