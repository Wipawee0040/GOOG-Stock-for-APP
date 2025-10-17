import pandas as pd
import yfinance as yf
import os

# print("Pandas version:", pd.__version__)
# print("yfinance version:", yf.__version__)


# 1) ดาวน์โหลดราคา GOOGL (รายวัน) ช่วง 2020-01-01 ถึง 2025-10-01
data = yf.download("GOOG", start="2020-01-01", end="2025-10-01",progress=False)

# 2) จัดรูปคอลัมน์ (กัน MultiIndex)
if isinstance(data.columns, pd.MultiIndex):
    data.columns = ['_'.join([c for c in col if c]) for col in data.columns.to_flat_index()]

print("Columns หลัง flatten:", data.columns.tolist())

# 3) หา column "Close" อัตโนมัติ (รองรับทั้ง 'Close' หรือ 'Close_GOOG')
close_col = [c for c in data.columns if 'Close' in c][0]
print("ใช้คอลัมน์นี้ในการคำนวณ:", close_col)

# 4) เตรียมข้อมูลคำนวณ
close = pd.to_numeric(data[close_col], errors='coerce').ffill()

# 5) MA แบบไม่มี NaN ตั้งแต่แถวแรก (expanding → rolling เมื่อครบหน้าต่าง)
data['MA20']  = close.rolling(window=20,  min_periods=1).mean()
data['MA50']  = close.rolling(window=50,  min_periods=1).mean()
data['MA200'] = close.rolling(window=200, min_periods=1).mean()

# 6) ผลตอบแทนรายวัน (แถวแรก = 0)
data = data.reset_index()
data['DailyReturn'] = data[close_col].pct_change().fillna(0.0)

# 7) บันทึกไฟล์ CSV
save_path = r"D:\Back up\Project สมัครงาน\GOOG_2020_2025.csv"
os.makedirs(os.path.dirname(save_path), exist_ok=True)
data.to_csv(save_path, index=False)

print("✅ บันทึกไฟล์เรียบร้อยที่:")
print(save_path)