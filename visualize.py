import json
import matplotlib.pyplot as plt

# 讀取資料
with open('expenses.json', 'r', encoding='utf-8') as f:
    expenses = json.load(f)

# 累計每個分類的金額
category_totals = {}

for item in expenses:
    category = item.get('category', '其他')
    amount = float(item.get('amount', 0))
    category_totals[category] = category_totals.get(category, 0) + amount

# 檢查是否有資料
if not category_totals:
    print("沒有可視覺化的資料")
    exit()

# 轉為圓餅圖所需資料
labels = list(category_totals.keys())
sizes = list(category_totals.values())

# 畫圖
plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Expense Categories Pie Chart')
plt.axis('equal')  # 保持圓形
plt.tight_layout()
plt.show()
