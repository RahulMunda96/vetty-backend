Vetty Internship – Cryptocurrency Market Backend API

A fully functional FastAPI backend that fetches real-time cryptocurrency data from the CoinGecko API, secured with JWT Authentication, supporting pagination, coin categories, multi-currency market data, Docker support, and unit tests.

📑 Table of Contents

Features

Tech Stack

Project Structure

Local Installation

Running the Server

Authentication

API Endpoints

Pagination Rules

Docker Setup

Running Tests

Future Improvements

Author

⭐ Features

🔐 JWT Authentication for protected routes

📊 Live Crypto Market Data from CoinGecko

🌍 Prices available in INR and CAD

📂 List coins, categories, and specific coin details

📄 Built-in Pagination

📘 Auto-generated Swagger Docs (/docs)

🐳 Dockerfile included

🧪 Unit Tests using PyTest

🛠 Tech Stack
Component	Technology
Framework	FastAPI
Server	Uvicorn
External API	CoinGecko
Auth	JWT (PyJWT)
HTTP Client	HTTPX
Virtualization	Docker
Testing	PyTest
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

💻 Local Installation
1️⃣ Clone the repository
git clone https://github.com/RahulMunda96/vetty-backend.git
cd vetty-backend

2️⃣ Create virtual environment
python -m venv venv

3️⃣ Activate (Windows)
.\venv\Scripts\activate

4️⃣ Install dependencies
pip install -r requirements.txt

▶️ Running the Server

Start the API:

python -m uvicorn app.main:app --reload


Open Swagger docs:

👉 http://127.0.0.1:8000/docs

🔐 Authentication
Get a token

POST /token using form-data:

username: admin
password: admin123


Response:

{
  "access_token": "<your_token>",
  "token_type": "bearer"
}


Use token with:

Authorization: Bearer <your_token>

📡 API Endpoints
Public
Method	Endpoint	Description
GET	/health	Health check
GET	/version	API version
POST	/token	Get JWT token
Protected (requires token)
Method	Endpoint	Description
GET	/coins	List coins (paginated)
GET	/categories	List categories
GET	/coins/markets	Market data in INR/CAD
GET	/coins/{coin_id}	Get specific coin
📄 Pagination Rules

Default:

page_num = 1
per_page = 10


Example:

/coins?page_num=2&per_page=20

🐳 Docker Setup
Build Image
docker build -t python_api .

Run Container
docker run -p 8000:8000 python_api


Open:

👉 http://127.0.0.1:8000/docs
