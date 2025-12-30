import sqlite3
from datetime import datetime

class DB_Manager():
    def __init__(self, db_path = "db.sqlite3"):
        self.db_path = db_path
        self._create_tables()

    def _get_connection(self):
        return sqlite3.connect(self.db_path)
    
    def _create_tables(self):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                        CREATE TABLE IF NOT EXISTS reminders(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            email_to TEXT NOT NULL,
                            subject TEXT NOT NULL,
                            message TEXT NOT NULL,
                            send_at DATETIME NOT NULL,
                            sent BOOLEAN DEFAULT 0,
                            created_at DATETIME NOT NULL         
                        )
                        """)
            conn.commit()

    def create_reminder(self,email_to,subject,message,send_at):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                            INSERT INTO reminders(email_to,subject,message,send_at,sent,created_at) VALUES (?, ?, ?, ?, ?, ?)
                        """,(email_to,subject,message,send_at,0,datetime.now().isoformat()))
            
            conn.commit()

    def get_pending_reminders(self):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                            SELECT id,subject,email_to, message FROM reminders WHERE sent = 0 and send_at <= ?
                            """,(datetime.now().isoformat(),))
            rows = cursor.fetchall()
        return rows

    def mark_as_sent(self, reminder_id):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""UPDATE reminders SET sent = 1 WHERE id = ?""",(reminder_id,))

            conn.commit()
        
    



