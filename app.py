from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)
DB_NAME = 'notes.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT NOT NULL)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM notes")
    notes = c.fetchall()
    conn.close()
    return render_template('index.html', notes=notes)

@app.route('/add', methods=['POST'])
def add_note():
    note = request.form['note']
    if note:
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute("INSERT INTO notes (content) VALUES (?)", (note,))
        conn.commit()
        conn.close()
    return redirect('/')

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
