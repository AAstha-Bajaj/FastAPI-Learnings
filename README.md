# FastAPI-Learnings
Welcome to my FastAPI journey! This repository contains my hands-on learning progression with building web APIs using Python, moving step-by-step through core routing, parameters, data validation, and logic structuring.

---

## 📚 What I Learned & Project Structure

Here is a breakdown of what each script in this repository covers:

### 1. Basic Routing & Server Setup (`main.py`, `main_s.py`)
* Setting up local development servers using **Uvicorn** with hot-reloading (`--reload`).
* Designing standard **HTTP GET methods** to send simple JSON payloads back to the client.
* Fixing structural indentation rules to ensure Python functions evaluate and return data structures properly instead of returning `null`.

### 2. Path Parameters (`path_parameter.py`)
* Capturing dynamic inputs natively through URL routes (e.g., `/customer/{cust_id}`).
* Leveraging Python typing (`cust_id: int`) to perform automatic type validation.
* Implementing internal checks to find records within dictionary lookups (`customer_risk_profiles`) and returning clean custom error status schemas when a record doesn't exist.

### 3. Query Parameters (`query_parameter.py`)
* Handling optional and required query parameters passed via the URL string (e.g., `?limit=10`).
* Managing data sorting, filtering, and pagination concepts inside API controllers.

### 4. Data Validation with Pydantic (`loan.py`, `loan_pydantic.py`)
* Creating custom input schemas using Pydantic's `BaseModel` to handle incoming JSON payloads for more complex use cases like loan predictions.
* Extracting variables from Pydantic objects (`application.income`) to calculate approval logic.
* Implementing inline ternary operators to format dynamic evaluation responses (`"approved" if approved else "rejected"`).
* *Crucial Lesson Learned:* Naming a local file `pydantic.py` overrides the official library and causes a circular import crash. Always use unique names like `loan_pydantic.py`!

---

## 🛠️ Tech Stack & Tools Used
* **Backend Framework:** FastAPI
* **ASGI Web Server:** Uvicorn
* **Data Validation:** Pydantic
* **API Testing Tool:** Swagger UI (Interactive Docs)

---

## ⚙️ How to Run Locally

1. **Clone this repository:**
   ```bash
   git clone [https://github.com/AAstha-Bajaj/FastAPI-Learnings.git](https://github.com/AAstha-Bajaj/FastAPI-Learnings.git)
   cd FastAPI-Learnings
