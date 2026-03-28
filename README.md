# 🏨 Hotel Review Intelligence Platform

A full-stack data-driven web application that analyzes hotel reviews to generate actionable insights for both travelers and hotel owners.
Built using **Flask, MongoDB, HTML/CSS**, and deployed on **Render with MongoDB Atlas**.

---

## 🚀 Overview

This project transforms raw, unstructured hotel review data into meaningful analytics and interactive dashboards.

It supports two core personas:

* **Travelers** → Discover hotels using search, ratings, and reviews
* **Hotel Owners** → Analyze customer feedback, trends, and behavior

The system leverages **MongoDB aggregation pipelines** to power real-time analytics such as rating trends, customer segmentation, and review insights.

---

## ✨ Key Features

### 👤 Traveler Features

* 🔍 Search hotels by city or name
* ⭐ View average ratings and review counts
* 📝 Browse detailed customer reviews
* 📊 Explore hotel-level insights

### 🧑‍💼 Owner Dashboard

* 📈 Rating trends over time (monthly analysis)
* 🧠 Customer segmentation (Promoters, Neutral, Detractors)
* 🔁 Loyalty detection (repeat customers)
* ⚠️ Low-rated review monitoring
* 🧾 Text-based insights from unstructured reviews
* 📊 Interactive charts (Chart.js)

---

## 🏗️ System Architecture

```
Flask (Backend + Templates)
        ↓
MongoDB (Hotels + Reviews Collections)
        ↓
Aggregation Pipelines (Analytics Layer)
        ↓
HTML/CSS + Chart.js (Frontend Dashboard)
        ↓
Render (Deployment) + MongoDB Atlas (Cloud DB)
```

---

## 🗃️ Database Design

### `hotels` Collection

* Hotel metadata (name, location, categories, etc.)

### `reviews` Collection

* Linked via `hotelId`
* Contains:

  * rating
  * review text
  * user info
  * timestamps

---

## ⚙️ Core Analytics Implemented

### 📈 Rating Trends

* Monthly aggregation using `$group` + `$year` + `$month`

### 🔁 Loyalty Detection

* Identifies repeat users using aggregation pipelines

### 🧠 Customer Segmentation

* Categorizes users into:

  * Promoters (≥4)
  * Neutral (≥3)
  * Detractors (<3)

### 🧾 Text-Based Insights

* Extracts signals from unstructured reviews using `$regexMatch`
* Tracks:

  * Cleanliness mentions
  * Noise complaints
  * Service feedback

---

## 🔌 Backend APIs

| Endpoint                   | Description             |
| -------------------------- | ----------------------- |
| `/hotels`                  | Search hotels           |
| `/hotel/<id>`              | Hotel details + reviews |
| `/owner/<id>`              | Owner dashboard         |
| `/api/owner/<id>/trends`   | Rating trends           |
| `/api/owner/<id>/loyalty`  | Loyal customers         |
| `/api/owner/<id>/segments` | Customer segmentation   |
| `/api/owner/<id>/insights` | Text insights           |

---

## 🧑‍💻 Tech Stack

* **Backend:** Flask, Python
* **Database:** MongoDB (Atlas)
* **Frontend:** HTML, CSS, Chart.js
* **Deployment:** Render
* **Data Processing:** MongoDB Aggregation Pipelines

---

## 📦 Project Structure

```
hotel-review-analysis/
│
├── app.py
├── config.py
├── requirements.txt
│
├── db/
│   └── mongo.py
│
├── routes/
│   ├── user_routes.py
│   └── owner_routes.py
│
├── services/
│   ├── hotel_service.py
│   └── analytics_service.py
│
├── templates/
│   ├── home.html
│   ├── hotel_list.html
│   ├── hotel_details.html
│   └── owner_dashboard.html
│
└── static/
    └── css/
```

---

## 🛠️ Local Setup

### 1. Clone the repo

```bash
git clone https://github.com/Anaghate/Hotel_Review_Analysis.git
cd hotel-review-analysis
```

### 2. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add `.env`

```env
MONGO_URI=mongodb://localhost:27017
DB_NAME=hotel_review_db
SECRET_KEY=your_secret_key
```

### 5. Run the app

```bash
python app.py
```

---

## 🌐 Deployment

* Backend deployed on **Render**
* Database hosted on **MongoDB Atlas**

Environment variables configured in Render:

```
MONGO_URI=<atlas-uri>
DB_NAME=hotel_review_db
SECRET_KEY=<secret>
```

---

## 📊 Sample Dashboard Insights

* 📉 Drop in ratings over time → operational issue detection
* 🔁 Repeat customers → loyalty tracking
* 🧾 Frequent complaints → service improvement signals
* ⭐ High-rated segments → marketing opportunities

---

## 🎯 What This Project Demonstrates

* Backend API design using Flask
* NoSQL schema modeling (MongoDB)
* Advanced aggregation pipelines
* Data-driven product thinking
* Full-stack development
* Deployment and production readiness

---

## 📌 Future Improvements

* NLP-based sentiment analysis (LLM / ML)
* Real-time filtering (AJAX)
* Authentication for hotel owners
* Map-based hotel discovery
* Review summarization using LLMs

---

## 🙌 Author

**Anagha Ghate**

---

## ⭐ If you like this project

Give it a star ⭐ — it helps a lot!
