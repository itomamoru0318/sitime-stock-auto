
import requests
import pandas as pd
from datetime import datetime

# === 設定 ===
SYMBOL = "TSE:6779"
URL = "https://scanner.tradingview.com/japan/scan"

payload = {
    "symbols": {"tickers": [SYMBOL], "query": {"types": []}},
    "columns": ["open", "high", "low", "close", "volume"]
}

# === データ取得 ===
res = requests.post(URL, json=payload, timeout=10)
res.raise_for_status()
data = res.json()["data"][0]["d"]

open_p, high, low, close, volume = data

today = datetime.now().strftime("%Y-%m-%d")

df = pd.DataFrame([{
    "Date": today,
    "Open": open_p,
    "High": high,
    "Low": low,
    "Close": close,
    "Volume": volume
}])

# === CSV保存（リポジトリに上書き） ===
csv_path = "ndk_stock.csv"
df.to_csv(csv_path, index=False)

print("CSV generated:")
print(df)
