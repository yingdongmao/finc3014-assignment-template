# Week 8 — trading journal

**Dates covered:** _(fill in)_
**Entry author:** _(your name + GitHub handle)_

## Market context (2–3 sentences)
> What was happening in the markets you care about this week?

## Decisions this week
> At least one specific decision and its one-line rationale (criterion A2).
> A deliberate no-trade is a decision — say why. Add a row per decision.

| Decision (trade / hold / no-trade) | Instrument | Rationale (one line) |
|---|---|---|
|  |  |  |

## 0. Positions at end of week
> Copy from this week's performance report, _Open Position Summary_ page
> (`reports/week8-performance.pdf` — the download guide is on Canvas).
> Cash is a row too.

| Symbol | Description | Quantity | Close price | Value | Cost basis | Unrealised P&L |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

**Total value (NLV):** _(fill in)_

## 1. Performance (window so far)
> From the _Risk Measures Benchmark Comparison_ page (portfolio and benchmark
> columns) and the last row of the _Cumulative_ table. Copy the numbers as
> printed. The benchmark column is your mandate benchmark (criterion C5).
> _Return this week_ = window-so-far cumulative minus last week's entry.

| Metric | Portfolio | Benchmark |
|---|---|---|
| Cumulative return (window so far) |  |  |
| Return this week |  |  |
| Standard deviation |  |  |
| Sharpe ratio |  |  |
| Sortino ratio |  |  |
| Max drawdown |  |  |

## 2. Cumulative return vs benchmark
> Snip the _Cumulative_ chart from the performance report (Win+Shift+S /
> Cmd+Shift+4), save it as `img/week8-cumret.png`, and it renders below.
> One sentence: what does the gap between the two lines say this week?

![Cumulative return vs benchmark](img/week8-cumret.png)

## 3. Performance by symbol
> From _Performance by Symbol_ and the _Portfolio Heat Map_. Name the biggest
> contributor and the biggest detractor, one line each on _why_ — link to a
> decision above if you can (this feeds criterion C8).

| Symbol | Avg weight | Return | Contribution |
|---|---|---|---|
|  |  |  |  |

**Biggest contributor:** _(symbol — why)_
**Biggest detractor:** _(symbol — why)_

## 4. Trading costs: market vs limit orders
> One row per order, from the _Trade Confirmation_ report
> (`reports/week8-trades.pdf`): use the order's **Total** line when it filled
> in parts; **Order type** is the report's MKT / LMT column. **Bid / Ask at
> order** is the ten-second rule — type them _before_ you click Submit
> (missed it? reconstruct an approximate mid via `analysis/save_quotes.py`
> and mark it "~"). Mid = (Bid + Ask) / 2.

| Date & time | Symbol | Buy/Sell, qty | Order type | Bid / Ask at order | Mid | Fill price | Commission | Effective spread (%) |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |

> **Effective spread (%)** = 2 × (Fill - Mid) / Mid × 100 for a buy;
> 2 × (Mid - Fill) / Mid × 100 for a sell. Positive: you paid to cross the
> spread (market orders usually do). Negative: price improvement — your
> resting limit order was paid for waiting. No fills this week? Write
> "no fills" — the empty confirmation report is the evidence.

**Average effective spread — market orders:** _(fill in)_ % ·
**limit orders:** _(fill in)_ %
> Expect the limit-order number to be lower, often negative. If it is not,
> that is worth a sentence in the reflection.

## 5. Reflection (optional but encouraged)
> What surprised you? What would you do differently next week? If your limit
> orders did not beat your market orders on cost — why not?
