import json
from datetime import datetime

DATA_FILE = "expenses.json"


def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def add_expense():
    expenses = load_data()
    while True:
        date = input("日期 (YYYY-MM-DD，留空用今天): ") or datetime.today().strftime("%Y-%m-%d")
        amount = float(input("金額: "))
        category = input("類別 (例如 food/transport/entertainment): ")
        notes = input("備註 (可留空): ")

        expenses.append({
            "date": date,
            "amount": amount,
            "category": category,
            "notes": notes
        })
        print("已新增！")

        if input("繼續新增？(y/n): ").lower() != "y":
            break

    save_data(expenses)
    print("所有支出已儲存。")


if __name__ == "__main__":
    add_expense()