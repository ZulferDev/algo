import ccxt
import pandas as pd
from datetime import datetime

def fetch_okx_ohlcv(symbol="BTC/USDT:USDT", timeframe="1m", limit=100):
    okx = ccxt.okx({
        'options': {
            'defaultType': 'swap'
        }
    })

    raw_ohlcv = okx.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)

    df = pd.DataFrame(raw_ohlcv, columns=[
        'timestamp', 'open', 'high', 'low', 'close', 'volume'
    ])

    # Convert timestamp to datetime
    df['datetime'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('datetime', inplace=True)

    return df
