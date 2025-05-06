def calc_size(balance: float, risk_percent: float, entry_price: float, stop_loss_price: float, rounded: int = 6) -> float:
    risk_amount = balance * (risk_percent / 100)
    sl_distance = abs(entry_price - stop_loss_price)

    if sl_distance == 0:
        raise ValueError("Jarak stop loss tidak boleh 0")

    position_size = risk_amount / sl_distance
    return round(position_size, rounded)  # bulatkan ke 6 desimal untuk precision
