from flask import Flask, jsonify,request,render_template,redirect,url_for
from db import DB_Manager

app = Flask(__name__)
db_manager = DB_Manager()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/health" , methods = ["GET"])
def get_health():
    return jsonify({"status": "ok"})

@app.route("/reminders" , methods = ["POST"])
def create_reminder():
    data = request.form if request.form else request.json
    
    required_fields = ["email_to", "subject", "message", "send_at"]

    for field in required_fields:
        if not data.get(field):
            return jsonify({"error": f"{field} is required"}), 400
        
    db_manager.create_reminder(
        data["email_to"].strip(),
        data["subject"],
        data["message"],
        data["send_at"]
    )


    if request.form:
        return redirect(url_for("success"))
    return jsonify({"Message":"Reminder created"}),201


@app.route("/reminders", methods = ["GET"])
def list_reminders():
    reminders = db_manager.get_all_reminders()
    return render_template("reminders.html", reminders= reminders)


@app.route("/success" , methods =["GET"])
def success():
    return render_template("success.html")





if __name__ == "__main__":
    app.run(host = "localhost", port=8000, debug=True)