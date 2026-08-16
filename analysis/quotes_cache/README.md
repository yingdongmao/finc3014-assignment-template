Cached 1-minute price bars live here, one CSV per symbol.

Created by `analysis/save_quotes.py` — run it once a week during the trading
window (free intraday data is only downloadable for the last 7 days) and
commit the cache with that week's journal entry. It is the safety net for a
fill whose bid/ask nobody typed into the journal at order time: use the
cached bar at the fill's minute as an approximate mid and mark it "~".
