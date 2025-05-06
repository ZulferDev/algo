def calculate_tp_sl_from_atr(entry_price: float, atr: float, direction: str, sl_multiplier: float = 1.5, rr_ratio: float = 1.5, rounded: int = 2) -> tuple[float, float]:
    sl_distance = atr * sl_multiplier
    tp_distance = sl_distance * rr_ratio

    if direction == 'long':
        sl_price = entry_price - sl_distance
        tp_price = entry_price + tp_distance
    elif direction == 'short':
        sl_price = entry_price + sl_distance
        tp_price = entry_price - tp_distance
    else:
        raise ValueError("Direction harus 'long' atau 'short'")

    return round(tp_price, rounded), round(sl_price, rounded)
