#!/usr/bin/env python3
"""Weekly quote cache — the "forgot to record the quote" safety net.

Free 1-minute price data can only be downloaded for the LAST 7 DAYS, so run
this once a week during the trading window (any member, ~30 seconds):

    pip install yfinance curl_cffi    # one-time
    python save_quotes.py             # symbols read from trades.csv
    python save_quotes.py AAPL MSFT   # ...or listed explicitly

It appends 1-minute bars to quotes_cache/<SYMBOL>.csv — COMMIT the cache with
your weekly journal entry (the commit timestamp is what makes it evidence).

If a fill's bid/ask was not typed into the journal at order time, use the
cached bar at the fill's minute as an approximate mid (journal row and
trades.csv `mid_at_order`), and mark it "~". A trade-price mid is only a
proxy: it can be off by up to the half-spread — that is the bid-ask bounce
from the lectures — so the live-typed quote always beats it.
"""

import csv
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CACHE = HERE / "quotes_cache"
TRADES = HERE / "trades.csv"


def symbols_from_trades():
    if not TRADES.exists():
        return []
    try:
        with open(TRADES, newline="", encoding="utf-8-sig") as f:
            return sorted({(row.get("symbol") or "").strip().upper()
                           for row in csv.DictReader(f)} - {""})
    except Exception as e:
        print(f"warning: could not read {TRADES.name} ({e})", file=sys.stderr)
        return []


def main():
    try:
        import yfinance as yf
        import pandas as pd
    except ImportError:
        sys.exit("yfinance is not installed - run:  pip install yfinance curl_cffi")

    symbols = sorted(set(s.upper() for s in sys.argv[1:]) | set(symbols_from_trades()))
    if not symbols:
        sys.exit("no symbols: none in trades.csv yet - pass them explicitly, "
                 "e.g.  python save_quotes.py AAPL MSFT")

    CACHE.mkdir(exist_ok=True)
    for sym in symbols:
        try:
            bars = yf.download(sym, period="7d", interval="1m",
                               progress=False, auto_adjust=False)
        except Exception as e:
            print(f"[FAIL] {sym}: download error ({e}) - try again later", file=sys.stderr)
            continue
        if bars is None or bars.empty:
            print(f"[warn] {sym}: no data returned (wrong symbol?)", file=sys.stderr)
            continue
        if isinstance(bars.columns, pd.MultiIndex):
            bars.columns = bars.columns.get_level_values(0)
        bars = bars[["Open", "High", "Low", "Close", "Volume"]]
        bars.index.name = "datetime"

        path = CACHE / f"{sym}.csv"
        if path.exists():
            old = pd.read_csv(path, index_col="datetime", parse_dates=["datetime"])
            bars = pd.concat([old, bars])
            bars = bars[~bars.index.duplicated(keep="last")].sort_index()
        bars.to_csv(path)
        print(f"[ok]   {sym}: cache now {len(bars)} minute-bars "
              f"({bars.index.min()} .. {bars.index.max()})")

    print("\nDone. Now COMMIT quotes_cache/ with this week's journal entry.")


if __name__ == "__main__":
    main()
