from trading_bot.fetcher import fetch_okx_ohlcv

def main():
    df = fetch_okx_ohlcv(timeframe="15m", limit=200)
    print(df)

if __name__ == "__main__":
    main()
