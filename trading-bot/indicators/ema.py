import pandas as pd

def calc_ema(df: pd.DataFrame, period: int = 14, column: str = 'close') -> pd.Series:
    ema = df[column].ewm(span=period, adjust=False).mean()
    return ema