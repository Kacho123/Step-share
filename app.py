from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'static/images'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def get_tutorials():
    conn = sqlite3.connect('tutorials.db')
    cur = conn.cursor()
    cur.execute("SELECT id, title, description, image FROM tutorials")
    tutorials = cur.fetchall()
    conn.close()
    return tutorials

def get_steps(tutorial_id):
    conn = sqlite3.connect('tutorials.db')
    cur = conn.cursor()
    cur.execute("SELECT step_number, step_text FROM steps WHERE tutorial_id = ? ORDER BY step_number", (tutorial_id,))
    steps = cur.fetchall()
    conn.close()
    return steps

@app.route('/')
def index():
    tutorials = get_tutorials()
    return render_template('index.html', tutorials=tutorials)

@app.route('/tutorial/<int:tutorial_id>')
def tutorial(tutorial_id):
    steps = get_steps(tutorial_id)
    return render_template('tutorial.html', steps=steps)

@app.route('/add', methods=['GET', 'POST'])
def add_tutorial():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        image_file = request.files['image']
        image_path = None

        if image_file and image_file.filename:
            filename = secure_filename(image_file.filename)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image_file.save(image_path)
            image_path = f'images/{filename}'

        conn = sqlite3.connect('tutorials.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO tutorials (title, description, image) VALUES (?, ?, ?)",
                    (title, description, image_path))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    return render_template('add_tutorial.html')

if __name__ == '__main__':
    app.run(debug=True)
