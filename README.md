# 📄 Async Document Processing Workflow System

## 🚀 Overview

This project is a full-stack asynchronous document processing system.
Users can upload documents, track processing progress in real-time, review extracted results, edit/finalize them, and export data.

The system demonstrates a real-world architecture using background workers and event-driven updates.

---

## 🧠 Key Features

* 📤 Upload one or more documents
* ⚙️ Asynchronous background processing using Celery
* 📡 Real-time progress updates using Redis Pub/Sub
* 📊 Dashboard with document status tracking
* 🔁 Retry failed jobs
* ✏️ Edit and finalize processed results
* 📥 Export finalized data as JSON and CSV

---

## 🏗️ Tech Stack

### Frontend

* Next.js (React)
* TypeScript

### Backend

* FastAPI (Python)

### Database

* PostgreSQL

### Background Processing

* Celery

### Messaging / State

* Redis (Pub/Sub + Broker)

---

## 🧩 Architecture

```
Frontend (Next.js)
        ↓
FastAPI Backend
        ↓
PostgreSQL Database
        ↓
Celery Worker
        ↓
Redis (Broker + Pub/Sub)
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

---

### 2. Backend Setup

```
cd backend
python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt
```

Update database config in:

```
backend/app/database.py
```

Run backend:

```
uvicorn app.main:app --reload
```

---

### 3. Start Redis

```
redis-server
```

---

### 4. Start Celery Worker

```
cd backend
venv\Scripts\activate

celery -A app.tasks worker --loglevel=info
```

---

### 5. Frontend Setup

```
cd frontend
npm install
npm run dev
```

Open:

```
http://localhost:3000
```

---

## 📡 API Endpoints (Sample)

* `POST /upload` → Upload document
* `GET /documents` → List documents
* `GET /progress` → Stream progress updates
* `POST /retry/{id}` → Retry job
* `PUT /update/{id}` → Update result
* `POST /finalize/{id}` → Finalize result
* `GET /export/json` → Export JSON
* `GET /export/csv` → Export CSV

---

## 🔄 Processing Workflow

Each document follows:

* Job Queued
* Processing Started
* Parsing
* Extraction
* Result Stored
* Completed / Failed

---

## ⚠️ Assumptions

* Processing logic is simulated (no heavy AI/OCR)
* Local Redis and PostgreSQL are used
* Focus is on async workflow design

---

## ⚖️ Tradeoffs

* Simple UI (focus on backend architecture)
* Basic error handling
* No authentication implemented

---

## 🚧 Limitations

* No file storage service (local only)
* No scalability optimizations
* Minimal validation on inputs

---

## 🎥 Demo

👉 Add your demo video link here

---

## 🌐 Live Demo

👉 Add your deployed frontend URL here

---

## 📁 Sample Data

👉 Add sample files and outputs if needed

---

## 🧑‍💻 Author

Shubham Thube

---

## 📌 Notes

This project focuses on demonstrating:

* Async architecture
* Background job handling
* Real-time progress tracking
* Clean system design

---
