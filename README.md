# 🧠 GenAI-Powered SQL Query Generator for E-Commerce Data

This project uses **Generative AI (via OpenRouter API)** to convert human-like questions into **SQL queries** and fetch insights from an e-commerce database.

---

## 🚀 Features

✅ Ask questions in plain English  
✅ Get instant SQL queries from a GenAI model (Mistral-7B-Instruct)  
✅ Connects to SQLite database with ad metrics and product sales  
✅ Clean JSON responses suitable for dashboards or API chaining  
✅ Fully functional Flask backend

---

## 🗃️ Dataset Tables Used

1. `ad_sales(date, item_id, ad_sales, impressions, ad_spend, clicks, units_sold)`  
2. `eligibility(eligibility_datetime_utc, item_id, eligibility, message)`  
3. `total_sales(date, item_id, total_sales, total_units_ordered)`

---

## 🧪 Sample Questions You Can Ask

- What is the total sales for item 3?  
- Which item had the highest number of units sold?  
- Show me the items with the highest ROAS.  
- Which product has the highest CPC (Cost per Click)?

---

## 🖥️ Tech Stack

- **Python 3**
- **Flask**
- **SQLite**
- **OpenRouter API** (using `mistralai/mistral-7b-instruct`)
- **Postman** for testing

---

## 📂 How to Run Locally

1. Clone this repo:
   ```bash
   git clone https://github.com/Saran818/GenAi_Ecommerce.git
   cd GenAi_Ecommerce
## 📽️ Demo Video + Project Files

🎥 [Click here to watch the demo and download all files](https://drive.google.com/file/d/1-MjcGHE0OhHAA3FfChAfgeQfLV3FWtqk/view?usp=drive_link)

This Google Drive contains:
- Demo video presentation 🎬
- CSV input files 📊
- SQLite database 📁
- Final working `app.py` code 💻
