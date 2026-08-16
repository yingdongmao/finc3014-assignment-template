# FINC3014 — The Client Mandate

> **This repository _is_ your submission — and this README is your report to
> your client.** Write it so that an intelligent non-specialist with a large
> sum at stake can follow every claim. The repo is private to your group and
> the teaching team. Commit early and often: your commit history is how
> contribution is evidenced.

---

## How to use this template (read once, then delete this block)

0. **Check the setup**: this repo was stamped from the course template by
   the teaching team — **Private**, in the unit's GitHub organisation
   (`finc3014-s2-2026/group-NN`). Confirm **Settings → Collaborators** lists
   every member; if a teammate is missing (usually a mistyped username on
   the Canvas survey), tell your tutor and we re-send the invitation.
1. **Fill in the group table** below, then **every member commits their own
   row of [`CONTRIBUTIONS.md`](CONTRIBUTIONS.md)** — from their own account.
   That is your minimum footprint (brief, Section 5): sign it by mid-window
   (Sun 27 Sep) and again before the freeze.
2. **Write your Client Mandate** (Section 1 below) before the window opens.
3. Each trading week, open that week's file in [`journal/`](journal/)
   (`week6.md` … `week10.md`, plus `break.md`) and fill its numbered sections
   from the week's **two IBKR reports** — the custom performance report and
   the Trade Confirmation report (click-by-click download guide on Canvas:
   `ibkr-reports-guide.pdf`). Commit entry, report PDFs, and chart snip
   during the week it describes — each on-time week earns a mark (A1).
4. Run the provided notebook
   [`analysis/analysis.ipynb`](analysis/analysis.ipynb) — **no code to
   write**: replace `analysis/returns.csv` with your window's daily-returns
   export (reports guide, Section 5), open the notebook in Google Colab,
   **Run all**, and reconcile its numbers against the IBKR report (rubric
   B). Then **File → Download → Download .ipynb** and commit the executed
   notebook — outputs visible — back over `analysis/analysis.ipynb`, so the
   marker sees your results without re-running it. Keep `trades.csv` as your
   trade-log evidence. During the trading
   window, run `analysis/save_quotes.py` once a week — it caches the
   1-minute bars that back-fill any journal quote you missed (see
   [`journal/`](journal/)).
5. Write the report **in this README**, in the sections below (delete the
   prompts as you go).
6. Document your AI use in [`ai-log/ai-log.md`](ai-log/ai-log.md).
7. Before the freeze, fill in [`CHECKLIST.md`](CHECKLIST.md) — for every
   rubric criterion, point to where in this repo you satisfied it.
8. _(Optional Quant Track — no marks attached, see brief §10)_ put your
   algorithm in [`quant/`](quant/).

**Marking is criterion-based** (see `CHECKLIST.md`): base marks are
present/absent; the six analysis criteria carry a second mark against a
published quality anchor. If you complete the checklist honestly, you can see
your own mark before we do. New to GitHub or Markdown? Read
`github-guide.pdf` on Canvas first.

---

## Group

| Field | Value |
|---|---|
| Group name | _e.g. Desk 12_ |
| Client | _e.g. Dr Chen (The Protector)_ |
| Risk aversion (A) | _e.g. 8_ |
| Track | Core / Core + Quant *(delete one)* |
| Benchmark | _e.g. SPY (S&P 500 ETF)_ |

| Member | SID | GitHub handle |
|---|---|---|
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |

> No fixed roles: rotate the desk's jobs — trading, the weekly journal
> ritual, the notebook, repo care — so over the window everyone touches each
> of them (brief, Section 4; the journal's A3 criterion checks the rotation).

## Tool stack *(rubric D4)*

- **Languages / notebooks:** _e.g. Python 3.11, Jupyter_
- **Libraries:** _e.g. pandas, numpy, matplotlib_
- **Data sources:** _e.g. IBKR, yfinance, Refinitiv_
- **AI tools:** _e.g. ChatGPT, Claude, GitHub Copilot_ — usage documented in [`ai-log/`](ai-log/ai-log.md)

---

# 1. Client Mandate *(C3)*

> Half a page, written before the window opens (brief, Section 2). State:
> **(i)** who the client is — a sentence of story; **(ii)** their
> **risk-aversion coefficient A** (2–10); **(iii)** a measurable objective;
> **(iv)** at least one hard constraint you honour all window; **(v)** why
> the benchmark above is the right yardstick for *this* client.
>
> Everything below is addressed to this client. Performance is judged by
> their certainty-equivalent return CE = r̄ − ½Aσ² (notebook, B3), not raw
> P&L.

# 2. Strategy

### 2.1 Hypothesis *(C1)*
> One sentence, testable. e.g. "We expected post-earnings-announcement drift in
> US large-cap technology stocks over the trading window."

### 2.2 Market(s) and instruments *(C2)*
> The specific markets/instruments you traded. Must reconcile with your trade log.

### 2.3 Capital and position sizing *(C4)*
> How much capital, and the rule you used to size each position — consistent
> with the mandate's constraints.

### 2.4 Benchmark and rationale *(C5)*
> Name a benchmark consistent with the mandate and asset class, and say in
> one sentence why it is the right comparison.

# 3. Trading risks *(C6)*
> At least two **distinct** risks. For each: the channel by which it hits your
> P&L, and a citation. *Quality anchor (+1): size each risk — an estimated
> magnitude or probability, not just a name.* Example structure:
>
> - **Liquidity risk** — wide spreads on our small-cap names raised our
>   effective spread above the quoted spread when we exited; ~40 bp round-trip
>   on ~30% of the book (see Analysis §6). *(Cite: e.g. Amihud 2002.)*
> - **...**

# 4. Execution
> Summarise how you traded. Link to the live journal: [`journal/`](journal/).
> The full trade log lives in [`analysis/trades.csv`](analysis/trades.csv).

# 5. Results

### 5.1 Performance vs benchmark *(C12 — numbers must match the notebook)*
> Drop in the cumulative-return chart from the notebook and your metric table
> (portfolio vs benchmark). The client's CE line is criterion B3. Example:
>
> | Metric | Portfolio | Benchmark |
> |---|---|---|
> | Total return | | |
> | Volatility | | |
> | Sharpe ratio | | |
> | **Client CE = r̄ − ½Aσ² (A = _)** | | |
> | Max drawdown | | |

### 5.2 Performance attribution *(C7, C8)*
> Decompose total return into ≥2 buckets. The buckets must sum to your total
> return. *Quality anchors (+1 each): buckets chosen to test your hypothesis
> (e.g. thesis trades vs. other trades); and for the largest
> contributor/detractor, separate design from luck — would it recur on a
> re-run?*

### 5.3 Execution costs *(C9)*
> Report your cost metrics — these come from your **journal's weekly cost
> tables** (section 4 of each entry: effective spread %, market vs limit) and
> [`analysis/trades.csv`](analysis/trades.csv), not from the notebook — and
> name your **highest-cost trade** with one factual driver. *Quality anchor
> (+1): express it in basis points and compare it to a stated yardstick (e.g.
> the quoted half-spread).*

# 6. Reflection *(C10)*
> - **One concrete change** you'd make next time, tied to a specific result above.
> - **Expected out-of-sample behaviour** of this strategy, with one reason.
> - *Quality anchor (+1): make the change testable — state the direction and
>   expected size of its effect.*

---

*Replace the prompts above with your own content. Keep the section headings so
the marker (and your `CHECKLIST.md`) can map to the rubric.*
