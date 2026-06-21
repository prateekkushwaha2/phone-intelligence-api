# Phone Intelligence API

Phone Intelligence API is a lightweight **OSINT-inspired phone metadata and intelligence API** built with **FastAPI**.

It analyzes phone numbers and returns publicly observable metadata and intelligence signals.

---

## Features

Current capabilities:

✓ Phone Validation
✓ Country Detection
✓ Carrier Detection
✓ Number Type Classification
✓ Timezone Detection
✓ International Formatting
✓ National Formatting
✓ Reputation Score
✓ Risk Classification

---

## Example Response

Request:

```http
GET /phone/+919797003423
```

Response:

```json
{
  "phone": {
    "valid": true,
    "possible": true,
    "country": "India",
    "carrier": "Airtel",
    "timezone": [
      "Asia/Calcutta"
    ],
    "type": "mobile",
    "international": "+91 97970 03423",
    "national": "097970 03423",
    "e164": "+919797003423"
  },

  "reputation": {
    "score": 0,
    "level": "low",
    "signals": []
  }
}
```

---

# Installation (Kali Linux)

## Clone Repository

```bash
git clone https://github.com/prateekkushwaha2/phone-intelligence-api.git

cd phone-intelligence-api
```

---

## Create Virtual Environment

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install fastapi uvicorn phonenumbers
```

---

## Run API

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Expected:

```text
INFO: Uvicorn running on http://0.0.0.0:8000
```

---

# Usage

Open:

```text
http://127.0.0.1:8000/docs
```

Swagger documentation:

```text
/docs
```

---

## API Endpoint

Lookup a phone number:

```http
GET /phone/{number}
```

Example:

```http
GET /phone/+919797003423
```

---

# Project Structure

```text
phone-intelligence-api/

├── main.py
├── requirements.txt

├── routes/
│   └── phone.py

├── services/
│   ├── phone_lookup.py
│   ├── reputation.py
│   └── risk_engine.py

└── README.md
```

---

# Roadmap

Planned features:

* Public Presence Signals
* Confidence Scoring
* Bulk Lookup
* Export JSON
* Export CSV
* Dashboard
* API Keys
---

# Disclaimer

This project is intended for:

* Learning
* Research
* Security experimentation
* Metadata analysis

It is designed to work with publicly observable metadata and reputation signals.

---

# License

MIT License

