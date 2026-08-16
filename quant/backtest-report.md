# Quant Track — backtest report (optional — no marks attached)

Delete the prompts as you fill each section. This track carries no marks
(brief, Section 10): it exists for the skill, the cohort showcase, and your
portfolio.

## Strategy logic and parameters *(self-check)*
> What is the idea? What signal, what universe, what position sizing, what risk
> controls? List the key parameters and their values.

## Backtest results *(self-check)*
> Report over your test window:

| Metric | Strategy | Benchmark |
|---|---|---|
| Total return | | |
| Sharpe ratio | | |
| Max drawdown | | |
| Alpha vs benchmark | | |

> Paste the QuantConnect equity-curve screenshot here.

## Live deployment *(self-check)*
> Did you paper-trade this on IBKR during the window? If yes, point to the
> trades in `analysis/trades.csv`. If backtest-only, say why (e.g. needed
> intraday data the paper account doesn't stream).

## Critical reflection *(self-check)*
> - **Overfitting:** how many parameters did you tune, and on what data? Did you
>   hold out any period?
> - **Look-ahead bias:** does any signal use information not available at
>   decision time?
> - **Transaction-cost realism:** what fee/slippage model did you use? How
>   sensitive are your results to it?
