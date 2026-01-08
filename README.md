# Reminder App

A small backend-focused application that allows users to schedule email reminders that are sent automatically at a specified date and time.

This project demonstrates real-world backend concepts such as background workers, scheduling, email automation, and frontend–backend integration.

---

## Features

- Create email reminders with a scheduled date and time
- Automatic email delivery using a background worker
- Windows Task Scheduler for periodic execution
- Email delivery via Resend API
- Simple web interface (HTML + CSS)
- Reminder status tracking (Pending / Sent)

---

## How it works

1. The user creates a reminder from the web form
2. The reminder is stored in the database with sent = 0
3. A background worker runs periodically(every 5 minutes)
4. The worker checks for reminders where

```python
   sent = 0
   send_at <= current_time
```

5. Emails are sent automatically
6. The reminder is marked as sent=1
   The design ensures reliability and avoids duplicate emails.

---

## Tech Stack

- Python
- Flask
- SQLite
- Background worker
- Windows Task Scheduler
- Resend (Email API)
- HTML + CSS
- Jinja Templates

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/frasegura/reminder_app
cd reminder_app
```

### 2. (Optional) Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3.Install dependencies

```bash
pip install flask resend
```

### 4.Set environment variables

```powershell
$Env:RESEND_API_KEY="your_resend_api_key"
```

---

## Running the application

- Start the Flask server:

```bash
py app.py
```

- Open your browser at:

```
http://localhost:8000
```

- The background worker runs automatically using Windows Task Scheduler and can also be executed manually:

```bash
py worker.py
```

## Author

**Francisco Segura**
Software Engineering Student  
Backend-focused developer

GitHub: https://github.com/frasegura
