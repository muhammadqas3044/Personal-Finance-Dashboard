# 💰 Personal Finance Dashboard (FastAPI + HTML/CSS)

A simple **Personal Finance Dashboard** where you can add, view, and delete your income and expense transactions.  
Built with **FastAPI (backend)** and **HTML/CSS/JS (frontend)**.

---

## 🚀 Features
- ✅ Add income and expense transactions  
- ✅ View all transactions in a table  
- ✅ See live **income, expense, and balance summary**  
- ✅ Automatic **pie chart visualization** using Chart.js  
- ✅ Delete transactions with one click  
- ✅ Real-time updates (no page refresh needed)

---

## 📖 Setup Instructions (Simple English)

**1. Project Setup**
- Put the index.html file inside the frontend folder
- Put the main.py file inside the backend folder. 
**2. Run the Backend**
- Open your terminal
- Switch to the backend folder: cd .\backend\
- Create a virtual environment
- Activate the environment. 
**3. Install FastAPI & Uvicorn**
- pip install fastapi uvicorn.
**4. Start the Server**
- uvicorn main:app --reload 
**5. Run the Frontend**
- Go to the frontend folder
- Open index.html in your browser (or use VSCode Live Server)
- You can now add, view, and delete transactions in the dashboard 

---

## 🛠 Tech Stack
- **Backend:** FastAPI (Python)
- **Frontend:** HTML, CSS, Vanilla JS
- **Visualization:** Chart.js
- **Server:** Uvicorn

---

## 📝 Future Improvements
- Add edit transaction feature
- Store data in a database (SQLite/PostgreSQL) for persistence
- Add filter/search transactions by type (income/expense)
- Add user authentication (login system)
