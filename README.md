# AdminX

> A high-performance, production-ready backend tool that dynamically generates structured CRUD APIs from your databases. Build any custom frontend on top — no codegen, no mess.

---

## ✨ What is AdminX?

AdminX introspects your connected databases and automatically builds RESTful APIs for CRUD operations, metadata inspection, and schema-aware forms.

Designed for **scalability**, **speed**, and **customizability**, AdminX empowers you to:

* Build admin dashboards
* Auto-generate form UIs
* Create internal tools
* Prototype frontend tools without building backend boilerplate

> Think Django Admin, but decoupled. Think Retool, but fully open and backend-native.

---

## 🚀 How it Works

AdminX connects to one or more databases and extracts their schema (tables, fields, constraints). It builds dynamic API routes on startup using a cached internal structure.

### Example API Endpoints

#### 📚 Introspection

* `GET /databases`
* `GET /databases/<database_id>`
* `GET /tables`
* `GET /tables/<table_id>`

#### 📊 Data Operations

* `GET /tables/<table_id>/rows`
* `POST /tables/<table_id>/rows`
* `PUT /tables/<table_id>/rows/<row_id>`
* `DELETE /tables/<table_id>/rows/<row_id>`

#### 🔎 Constraints & Metadata

* `GET /tables/<table_id>/constraints`
* `GET /fields/<field_id>/validation`

> Everything is introspected and exposed in a structured, frontend-friendly JSON format.

---

## 🔧 Technologies

* **Python 3.11+**
* **FastAPI** — Web framework
* **SQLAlchemy** — Database introspection & ORM
* **Pydantic** — Data validation
* **Uvicorn** — ASGI server
* **SQLite / PostgreSQL / MySQL** — Multi-database support

---

## 🫠 Features

* 🧹 Plug-in multiple databases (PostgreSQL, SQLite, etc.)
* 📁 Auto-detect table/field constraints (e.g., `gte`, `regex`, `choices`)
* ⚡ Fast introspection and caching
* 🔐 Optional authentication system
* 🎛️ Designed to be embedded in full applications or standalone
* 🧠 Form-rendering friendly responses
* 🏗️ Extensible schema and validation engine

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/adminx
cd adminx
poetry install  # or pip install -r requirements.txt
```

---

## 🧪 Running Locally

```bash
uvicorn main:app --reload
```

This will:

* Load the internal schema DB (`schema_database.sqlite3`)
* Introspect connected external databases
* Expose static API routes dynamically mapped to introspected objects

---

## 📁 Project Structure

```
src/
├── api/                # FastAPI endpoints
├── core/               # Core service logic
├── framework/          # Generic schema models and abstractions
├── config/             # App, logging, and YAML configs
├── main.py             # Entrypoint
└── utils/              # Helpers
```

---

## 📄 Example Schema Response

```json
{
  "id": "db-uuid",
  "name": "user_service_db",
  "tables": [
    {
      "id": "table-uuid",
      "name": "users",
      "fields": [
        {
          "name": "email",
          "type": "string",
          "constraints": {
            "regex": "^[^@]+@[^@]+$",
            "max_length": 255
          }
        }
      ]
    }
  ]
}
```

---

## 📌 Roadmap

*

---

## 🤝 Contributing

Contributions, feature requests, and discussions are welcome!

* Fork it
* Create your feature branch: `git checkout -b feature/my-feature`
* Commit your changes: `git commit -am 'Add new feature'`
* Push to the branch: `git push origin feature/my-feature`
* Open a pull request

---

## 📜 License
MIT License

Copyright (c) 2025 Fazliddin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

## 🙏 Acknowledgements

* Inspired by tools like Superset, Retool, and Django Admin
* Built with love by open-source developers

---

## 📬 Contact

Have questions, feedback, or ideas?
[Open an issue](https://github.com/abdurahimovf18/adminx/issues) or DM me on Telegram: `@abdurahimov_f18`
