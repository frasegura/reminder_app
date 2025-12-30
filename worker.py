import os
import resend
from db import DB_Manager

db_manager = DB_Manager()
resend.api_key = os.getenv("RESEND_API_KEY")

def send_email(to,subject, message):
    resend.Emails.send({
        "from": "Reminders <onboarding@resend.dev>",
        "to": to,
        "subject": subject,
        "html": f"<p>{message}</p>",
    })

def process_pending_reminders():
    pending = db_manager.get_pending_reminders()
    for r in pending:
        reminder_id = r[0]
        subject = r[1]
        email_to = r[2]
        message = r[3]

        #print("EMAIL TO:", repr(email_to))
        send_email(email_to,subject,message)
        db_manager.mark_as_sent(reminder_id)

if __name__ == "__main__":
    process_pending_reminders()

