from flask import Flask, render_template, request, redirect, url_for
import json
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/message', methods=['GET', 'POST'])
def message():
    if request.method == 'POST':
        # Handle form data
        username = request.form['username']
        user_message = request.form['message']
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

        new_entry = {
            now: {
                "username": username,
                "message": user_message
            }
        }

        storage_file = os.path.join("storage", "data.json")

        # Load existing data or start with empty dict
        if os.path.exists(storage_file):
            with open(storage_file, "r", encoding="utf-8") as file:
                data = json.load(file)
        else:
            data = {}

        # Add new entry and save
        data.update(new_entry)
        with open(storage_file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)

        return redirect(url_for('index'))

    return render_template('message.html')

@app.route('/read')
def read_messages():
    storage_file = os.path.join("storage", "data.json")

    # Read messages from data.json
    if os.path.exists(storage_file):
        with open(storage_file, "r", encoding="utf-8") as file:
            data = json.load(file)
    else:
        data = {}

    # Pass messages to the template
    return render_template("read.html", messages=data)

@app.errorhandler(404)
def page_not_found(e):
    # Render error page when 404 Not Found occurs
    return render_template('error.html'), 404

if __name__ == '__main__':
    # Start the Flask app on port 3000
    app.run(host="0.0.0.0", port=3000)
