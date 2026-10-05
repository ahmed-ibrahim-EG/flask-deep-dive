# 🧪 Flask Fundamentals Lab & Deep Dive

A focused, hands-on laboratory project designed to review, reinforce, and dissect the foundational mechanics of web servers and RESTful APIs using **Flask (Python)**. 

> **Purpose:** This repository serves as a practical sandbox to dive deeper into the low-level lifecycle of HTTP requests, routing mechanisms, request contexts, and response structures in Flask.

---

## 🎯 Learning Objectives & Deep Concepts

This project explores what happens beneath the surface when building APIs:

* **Dynamic Routing & URL Parameter Extraction:** Understanding how the decorator `@app.route('/books/<int:book_id>')` interacts with Werkzeug's regex matching engine, parsing type-casted parameters (`<int>`), and injecting them into view functions via named arguments (`**kwargs`).
* **Request Context (`request` object):** Inspecting incoming HTTP requests and extracting query parameters using `request.args.get()` with safe defaults and automated type conversions.
* **Response Serialization & Headers:** Differentiating between raw text responses and JSON payloads generated via `jsonify()`, while explicitly controlling HTTP Status Codes (`200 OK` vs. `404 Not Found`).
* **Clean In-Memory Filtering:** Applying idiomatic Python list comprehensions and iterator lookups (`next()`) for efficient resource retrieval.

---

## 🛠️ API Reference

| Method | Endpoint | Description | Query Parameters | Expected Status |
| :--- | :--- | :--- | :--- | :--- |
| `GET` | `/` | Health check & server ping | None | `200 OK` |
| `GET` | `/books` | Retrieve entire book dataset | None | `200 OK` |
| `GET` | `/books?min_price=<val>` | Filter books with price $\ge$ `min_price` | `min_price` (float) | `200 OK` |
| `GET` | `/books/<int:book_id>` | Fetch a specific book by ID | None | `200 OK` or `404 Not Found` |

---

## 🔬 Quick Curl Verification

Test the behavior directly via terminal:

```bash
# 1. Base ping
curl -i http://127.0.0.1:5000/

# 2. Retrieve all resources
curl http://127.0.0.1:5000/books

# 3. Apply query parameter filtering
curl "http://127.0.0.1:5000/books?min_price=100"

# 4. Successful dynamic route query
curl -i http://127.0.0.1:5000/books/2

# 5. Fallback on non-existent resource (404 check)
curl -i http://127.0.0.1:5000/books/999
```

---

## 🚀 Setup & Execution

1. **Clone this lab:**
   ```bash
   git clone <YOUR_REPOSITORY_URL>
   cd <REPOSITORY_NAME>
   ```

2. **Initialize and activate a virtual environment:**
   * **Windows:**
     ```powershell
     python -m venv venv
     venv\Scripts\activate
     ```
   * **Linux / macOS:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install dependencies:**
   ```bash
   pip install Flask
   ```

4. **Launch development server:**
   ```bash
   python app.py
   ```
   The local service runs at `http://127.0.0.1:5000/`.