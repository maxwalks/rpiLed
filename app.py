from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/toggle-lights/')
def toggle_lights():
    subprocess.run(['uhubctl', '-l', '1-1', '-a', 'toggle'], capture_output=False, text=True)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
