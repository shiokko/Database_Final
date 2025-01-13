# DBMS Project

### About Backend
Using `Flask`. <br />
The server loading on address `0.0.0.0`, which means all localhost address. <br />
And the port is `8080`. <br />


### About Database 
`create_table.sql` is the raw SQL commands to create seven tables of the project.(for backup) <br />
`project.db` is the created Database. <br />
Enter the Database by using the command `sqlite3 project.db`.

# 政大周邊餐廳隨機選擇系統

![Banner](https://via.placeholder.com/800x200.png?text=%E6%94%BF%E5%A4%A7%E9%A4%90%E5%BB%B3%E9%9A%A8%E6%A9%9F%E6%8E%A8%E8%96%A6%E7%B3%BB%E7%B5%B1)

## 專案簡介
身為政治大學的學生，常常在用餐時間不知道吃什麼。因此，我們設計了一個隨機餐廳推薦系統，幫助用戶快速決定用餐地點。本系統還提供評分、搜尋、黑名單等功能，讓使用者打造屬於自己的美食筆記。

---

## 系統功能
1. **隨機餐廳功能**：
   - 一鍵隨機推薦附近的餐廳。
   - 支援 Google Maps 導航。
2. **搜尋餐廳功能**：
   - 輸入關鍵字或選擇分類篩選餐廳。
3. **評分系統功能**：
   - 用戶可對餐廳留下評分與評論。
4. **歷史紀錄功能**：
   - 查看曾經評分過的所有餐廳。
5. **黑名單功能**：
   - 將不喜歡的餐廳加入黑名單，避免再次推薦。

---

## ER 模型
以下是本系統使用的 ER 模型，為資料庫設計提供基礎結構。

![ER-Model](https://via.placeholder.com/800x400.png?text=ER+Model+Placeholder)

---

## 系統架構
- **前端**：HTML、CSS、JavaScript
- **後端**：Flask (Python)
- **資料庫**：SQLite

---

## 安裝與使用
1. **環境需求**：
   - Python 3.9+
   - pip

2. **專案下載**：
   ```bash
   git clone https://github.com/your-repo/random-restaurant-selector.git
   cd random-restaurant-selector
