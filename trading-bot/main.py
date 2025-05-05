from data.fetcher import fetch_okx_ohlcv
from indicators.ema import calc_ema
from indicators.rsi import calc_rsi


def main():
    df = fetch_okx_ohlcv(timeframe="15m", limit=25)
    print(rsi)

if __name__ == "__main__":
    main()
