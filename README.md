Vetty Internship – Cryptocurrency Market API (FastAPI + CoinGecko)

A backend API built using FastAPI that fetches live cryptocurrency data from the CoinGecko API.
This project implements authentication, pagination, multiple pricing currencies, category filtering, Docker support, and automated API documentation.

🚀 Features
✔ User Authentication

JWT-based secure login (/token)

Protected routes require Authorization Header

✔ Cryptocurrency Data Endpoints

List all coins (paginated)

List categories

Get coin markets in INR and CAD

Get specific coin details

✔ Advanced API Features

Pagination (page_num, per_page)

Swagger UI (automatic documentation)

Health Check (/health)

Version Info (/version)

Fully async using HTTPX & FastAPI

✔ Deployment Ready

Dockerfile included

Can run locally or in container

Clean project structure

📂 Project Structure
vetty-backend/
│── app/
│   ├── main.py
│   ├── auth.py
│   ├── coingecko_client.py
│── tests/
│   ├── test_main.py
│── requirements.txt
│── Dockerfile
│── README.md

🔐 Authentication
Request Token

POST /token
Use form-data:

username: admin
password: admin123

Use token for protected routes

Swagger → Click Authorize → enter:

Bearer <your_token>

🔧 Installation & Running (Local Setup)
1️⃣ Clone repository
git clone https://github.com/RahulMunda96/vetty-backend.git
cd vetty-backend

2️⃣ Create and activate virtual environment
python -m venv venv

# Windows
.\venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Start FastAPI server
python -m uvicorn app.main:app --reload

5️⃣ Open API documentation

Swagger UI:

👉 http://127.0.0.1:8000/docs

🐳 Run with Docker
1️⃣ Build Docker image
docker build -t vetty-backend .

2️⃣ Run container
docker run -p 8000:8000 vetty-backend


Open in browser:

👉 http://127.0.0.1:8000/docs

📡 Available Endpoints
🔓 Public
Method	Endpoint	Description
GET	/health	Check API status
GET	/version	Version info
POST	/token	Get JWT token
🔐 Protected (Requires Token)
Method	Endpoint	Description
GET	/coins	Paginated list of coins
GET	/categories	List categories (paginated)
GET	/coins/markets	Prices in INR or CAD
GET	/coins/{coin_id}	Specific coin details
📘 Pagination Rules

Default:

page_num = 1
per_page = 10


Can override:

/coins?page_num=2&per_page=20

🧪 Unit Testing

Run:

pytest
