"""
FINC3014 Quant Track (OPTIONAL) — algorithmic strategy starter.

This is a minimal QuantConnect LEAN algorithm: a moving-average crossover on a
single equity. It is a STARTING POINT, not a target — change the universe, the
signal, the sizing, and the risk controls to express your own idea.

How to run it
-------------
1. Create a free account at https://www.quantconnect.com and open a new
   Python algorithm, OR install the LEAN CLI locally.
2. Paste this file in, set the dates/cash, and click Backtest.
3. Record Sharpe, max drawdown, and the benchmark comparison in
   backtest-report.md (criteria Q2, Q3).
4. (Ideal) deploy to paper-trade on IBKR during the trading window so the
   trades appear in your IBKR log (criterion Q4).

Suggested (NOT required) target: positive alpha vs benchmark, Sharpe >= 1.0,
max drawdown <= 20%, realistic transaction costs. Beating it is not the point;
understanding WHY your strategy works or fails is.
"""

from AlgorithmImports import *  # provided by the QuantConnect/LEAN runtime


class MovingAverageCrossover(QCAlgorithm):

    def Initialize(self):
        # --- Backtest window & capital (match your assignment window) ---------
        self.SetStartDate(2026, 9, 7)
        self.SetEndDate(2026, 10, 16)
        self.SetCash(1_000_000)

        # --- Universe: start with one liquid name; extend to your own ---------
        self.symbol = self.AddEquity("SPY", Resolution.Daily).Symbol

        # --- Signal: fast vs slow simple moving average -----------------------
        self.fast = self.SMA(self.symbol, 10, Resolution.Daily)
        self.slow = self.SMA(self.symbol, 30, Resolution.Daily)

        # Warm up so the indicators are ready before we trade.
        self.SetWarmUp(30)

        # Realistic-ish costs: LEAN's default fee/slippage models are on by
        # default. Document any changes in backtest-report.md (criterion Q5).

    def OnData(self, data: Slice):
        if self.IsWarmingUp or not (self.fast.IsReady and self.slow.IsReady):
            return

        invested = self.Portfolio[self.symbol].Invested

        # Go long when the fast MA crosses above the slow MA; flat otherwise.
        if self.fast.Current.Value > self.slow.Current.Value and not invested:
            self.SetHoldings(self.symbol, 1.0)   # TODO: your position-sizing rule
            self.Debug(f"{self.Time} LONG {self.symbol}")
        elif self.fast.Current.Value < self.slow.Current.Value and invested:
            self.Liquidate(self.symbol)
            self.Debug(f"{self.Time} FLAT {self.symbol}")

        # TODO: add a risk control (e.g. stop-loss, max drawdown guard, position cap).
