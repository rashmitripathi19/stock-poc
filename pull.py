import yfinance as yf
from pathlib import Path
SYMBOLS = ["MSFT"]
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

def fetch(symbol: str, start: str = "2020-01-01", end: str = "2026-01-01"):
    print(f"Fetching data for {symbol} from {start} to {end}")
    df = yf.download(symbol, start=start, end=end, auto_adjust=True)
    if(df.empty):
        print(f"No data found for {symbol} from {start} to {end}")
        return
    out = DATA_DIR / f"{symbol}.csv"
    df.to_csv(DATA_DIR / f"{symbol}.csv")
    df.to_csv(out)
    print(f" Saved {len(df)} rows of data for {symbol} to {out}")
def main():
    for symbol in SYMBOLS:
        try:
            fetch(symbol)
        except Exception as e:
            print(f"Error fetching data for {symbol}: {e}")
if __name__ == "__main__":
    main()