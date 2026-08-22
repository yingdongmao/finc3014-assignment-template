# Self-Assessment Checklist — required

For **every** criterion below, write where in this repo you satisfied it
(file, section, cell, or figure). The marker returns this same table ticked.

- A criterion is **met** if the item is present and free of a *conceptual*
  error. Minor slips are ignored. **If in doubt, the mark is awarded.**
- Six criteria are **tiered "1+1"** (C6–C10, D2): the first mark for the item
  being present, the second only if it meets the published **quality anchor**
  (shown in *italics* in the row; full list in the brief, Section 9). The
  anchor list is closed — no other quality judgment enters the marking.
- To query a returned mark: point to the location where the criterion is
  satisfied. If it's there, the mark is restored — no negotiation.

Mark the **Self** column with `x` when you believe you've met the criterion
(for tiered rows: `x` = base mark, `xx` = base + quality anchor).
Leave the **Marker** column blank.

---

## Component A — Live Trading Journal (10 marks)

| # | Criterion | Pts | Where in our repo | Self | Marker |
|---|---|---|---|---|---|
| A1 | A dated entry following the week template's sections, committed **on time** in each of the six trading weeks — **on time = pushed by 11:59 pm on that week's Sunday** (Git timestamp; a late entry scores 0 for that week, no exceptions) | 6 |  |  |  |
| A2 | Every entry records ≥1 specific decision + a one-line rationale | 2 |  |  |  |
| A3 | Journal commits from ≥3 different members' Git identities | 2 |  |  |  |

## Component B — Run and Reconcile the Analysis Notebook (11 marks)

| # | Criterion | Pts | Where in our repo | Self | Marker |
|---|---|---|---|---|---|
| B1 | Notebook runs top-to-bottom from a fresh kernel (Colab "Run all"), reading `returns.csv` | 3 |  |  |  |
| B2 | `returns.csv` holds OUR window's daily portfolio + benchmark returns from the IBKR CSV export (not the example data) | 1 |  |  |  |
| B3 | Notebook's `A` parameter set to our mandate's A, so CE = r̄ − ½Aσ² is computed for OUR client (annualisation stated) | 2 |  |  |  |
| B4 | Reconciliation table filled: each computed metric beside IBKR's reported value, each gap explained in one line | 2 |  |  |  |
| B5 | Labelled cumulative-return chart, portfolio vs benchmark (legend + axes) | 2 |  |  |  |
| B6 | The README's performance numbers/figures are the notebook's outputs (execution-cost figures are exempt — they come from the journal + `trades.csv`) | 1 |  |  |  |

## Component C — The Client Report (README) (19 marks)

| # | Criterion | Pts | Where in our repo | Self | Marker |
|---|---|---|---|---|---|
| C1 | One-sentence testable hypothesis | 1 |  |  |  |
| C2 | Specific market(s)/instruments, reconcilable with trade log | 1 |  |  |  |
| C3 | Client Mandate: persona, risk-aversion A, measurable objective, ≥1 hard constraint | 2 |  |  |  |
| C4 | Capital + position-sizing rule | 1 |  |  |  |
| C5 | Named benchmark consistent with the mandate's asset class *and* the client's risk preference (A), with the rationale linking the two | 1 |  |  |  |
| C6 | ≥2 distinct risks, each with channel to P&L + citation — *anchor: risks are sized (magnitude or probability)* | 1+1 |  |  |  |
| C7 | Return decomposed into ≥2 buckets, quantified, reconciling to total — *anchor: buckets test the hypothesis* | 1+1 |  |  |  |
| C8 | Largest contributor + detractor identified, each linked to a decision — *anchor: separates design from luck* | 1+1 |  |  |  |
| C9 | Highest-cost trade named + one factual cost driver — *anchor: in bps, vs a stated yardstick* | 1+1 |  |  |  |
| C10 | One concrete change tied to a result + expected out-of-sample behaviour — *anchor: change is testable (direction + expected size)* | 1+1 |  |  |  |
| C11 | README structured (headings, links) and renders cleanly on GitHub | 1 |  |  |  |
| C12 | Headline README results match the notebook outputs | 2 |  |  |  |

## Component D — AI Co-Pilot Log (6 marks)

| # | Criterion | Pts | Where in our repo | Self | Marker |
|---|---|---|---|---|---|
| D1 | ≥3 distinct AI interactions documented (prompt + output summary) | 2 |  |  |  |
| D2 | ≥2 of them critically evaluated with the group's verdict — *anchor: names the independent check performed* | 1+1 |  |  |  |
| D3 | ≥1 caught AI error/limitation — or a stated verification method | 1 |  |  |  |
| D4 | Full tool stack listed in the README | 1 |  |  |  |

## Component E — Peer Repo Review (4 marks)

| # | Criterion | Pts | Where | Self | Marker |
|---|---|---|---|---|---|
| E1 | Reflection essay (~1 page) on the assigned repo, on time: what they did differently, the idea we'd steal, what we'd change | 2 | *(submitted on Canvas)* |  |  |
| E2 | We ran their notebook (Colab) and report whether it reproduced their README numbers, + ≥1 quantitative desk comparison | 2 | *(submitted on Canvas)* |  |  |

**Core Track total: ___ / 50**

---

## Quant Track — optional (no marks; self-check only)

If your group opted in, use this list to check `quant/` is complete.
**Nothing here carries marks either way** (brief, Section 10) — the track is
for the skill, the showcase, and the portfolio piece.

- [ ] `quant/strategy.py` committed and runs/backtests
- [ ] `quant/backtest-report.md` states strategy logic + parameters
- [ ] Backtest reports Sharpe, max drawdown, benchmark comparison
- [ ] Paper-traded live on IBKR (trades in log) — or documented why backtest-only
- [ ] Critical reflection on overfitting / look-ahead bias / cost realism

---

## Individual footprint — check before the freeze (affects your ICF, not the group mark)

Every member, individually (brief, Section 5):

- [ ] I have ≥1 substantive commit from **my own** GitHub account
- [ ] I signed my own `CONTRIBUTIONS.md` row when the repo arrived (by Sun 30 Aug)
- [ ] I committed my own `CONTRIBUTIONS.md` row by mid-window (Sun 27 Sep)
- [ ] I committed my final `CONTRIBUTIONS.md` signature in the last week
- [ ] My commits show my correct GitHub identity (avatar visible in History)
