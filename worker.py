from db import DB_Manager

db_manager = DB_Manager()

def send_email(subject,to, message):
    print(f"Sending email to {to}")

pending = db_manager.get_pending_reminders()

for r in pending:
    send_email(r[1], r[2], r[3])
    db_manager.mark_as_sent(r[0])