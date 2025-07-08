# strategy.py

def detect_volume_signal(df):
    if len(df) < 7:
        return None  # Not enough data

    latest = df.iloc[-1]
    historical = df.iloc[:-1]

    vol_mean = historical['Volume'].mean()
    vol_std = historical['Volume'].std()
    threshold = vol_mean + 3 * vol_std

    if latest['Volume'] > threshold:
        # Determine direction
        price_now = latest['Close']
        price_30min_ago = df.iloc[-7]['Close']

        if price_now > price_30min_ago:
            return 'SELL'
        else:
            return 'BUY'

    return None
