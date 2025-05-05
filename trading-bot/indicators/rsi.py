import pandas as pd

def calc_rsi(df: pd.DataFrame, period: int = 14, column: str = 'close') -> pd.Series:
    """
    Menghitung Relative Strength Index (RSI) dari kolom harga (default: 'close').

    :param df: DataFrame yang memiliki kolom harga
    :param period: Periode RSI (default: 14)
    :param column: Kolom yang dipakai untuk hitungan RSI
    :return: Series RSI
    """
    delta = df[column].diff()

    gain = delta.where(delta > 0, 0.0)
    loss = -delta.where(delta < 0, 0.0)

    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    return rsi
