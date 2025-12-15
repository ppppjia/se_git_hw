# se_git_hw
軟體工程 hw2功課

# 支出追蹤器 - Assignment 2

這是一個用 Python 實作的簡單支出追蹤工具，專為兩人一組練習 Git 版本控制協作而設計。

## 功能特色
- 新增多筆支出記錄（包含日期、金額、類別，可選備註）
- 將支出資料儲存至 JSON 檔案（`expenses.json`）
- 根據類別產生圓餅圖，顯示各類別支出比例

## 專案結構
.
├── member1_input.py            # 輸入模組（Member A 負責）
├── visualize.py          # 視覺化模組（Member B 負責）
├── expenses.json         # 儲存的支出資料（首次執行後產生）
├── README.md             # 本說明文件

text## 需求環境
- Python 3.6 或以上版本
- matplotlib 套件

## 安裝步驟
1. 複製本專案到本地：
   ```bash
   git clone https://github.com/ppppjia/se_git_hw.git
   cd se_git_hw

安裝必要套件：Bashpip install matplotlib

執行方式
1. 輸入支出（輸入模組）
執行以下指令開始新增支出記錄：
Bashpython input_expense.py
程式會提示你輸入：

日期（格式 YYYY-MM-DD，按 Enter 鍵使用今天日期）
金額
類別（例如 food、transport、entertainment）
備註（可留空）

你可以一次新增多筆支出，輸入完畢後選擇 n 結束新增。
資料會自動儲存到 expenses.json。
2. 顯示圓餅圖（視覺化模組）
在輸入一些支出資料後，執行以下指令：
Bashpython visualize.py
程式會顯示一個圓餅圖，呈現各類別的支出總額與比例。
範例輸出
以下是使用範例資料產生的圓餅圖：
範例圓餅圖
(上圖顯示範例支出類別：食物 45%、交通 30%、娛樂 25%。實際圖表會依你輸入的資料而定。)
Demo 影片
完整操作示範請觀看：
https://youtu.be/你的影片連結
Git 協作說明


兩人分支已使用 command-line git merge 方式合併，Network Graph 可清楚看到合併紀錄

組員資訊

Member A：[你的名字]（GitHub: @ppppjia）
Member B：[組員名字]（GitHub: @組員帳號）
