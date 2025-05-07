from core.fetcher import okx
from src.strategy.ema_rsi import EMARSIStrategy
from src.utils.risk import RiskManager

def main():
    # Initialize components
    exchange = OKXExchange(
        symbol="BTC/USDT:USDT",
        timeframe="15m"
    )
    
    strategy = EMARSIStrategy(
        ema_short=9,
        ema_long=21,
        rsi_period=14,
        rsi_lower=30,
        rsi_upper=70
    )
    
    risk_manager = RiskManager(
        risk_percent=1.0,
        rr_ratio=1.5
    )
    
    # Main trading loop
    while True:
        try:
            # Fetch latest data
            data = exchange.fetch_ohlcv(limit=100)
            
            # Generate signals
            signal = strategy.generate_signal(data)
            
            if signal:
                # Calculate position size & risk
                entry, sl, tp = risk_manager.calculate_levels(
                    signal.direction,
                    data
                )
                
                # Execute trade
                exchange.create_order(
                    direction=signal.direction,
                    size=signal.size,
                    sl=sl,
                    tp=tp
                )
                
        except Exception as e:
            print(f"Error: {e}")
            continue

if __name__ == "__main__":
    main()
