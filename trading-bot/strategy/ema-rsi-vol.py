import pandas as pd

def ema_valid(df: pd.DataFrame, short_period: int = 9, long_period: int = 21) -> str:
    ema_short = df[f'EMA_{short_period}'].iloc[-1]
    ema_long = df[f'EMA_{long_period}'].iloc[-1]

    if ema_short > ema_long:
        return 'long'
    elif ema_short < ema_long:
        return 'short'
    else:
        return 'none'

def rsi_valid(df: pd.DataFrame, period: int = 14, lower: float = 30, upper: float = 70) -> bool:

    rsi_value = df[f'RSI_{period}'].iloc[-1]
    return lower < rsi_value < upper

def vol_valid(df: pd.DataFrame) -> bool:
    last_vol = df['volume'].iloc[-1]
    ema_vol = df['ema_vol'].iloc[-1]
    return last_vol >= ema_vol
