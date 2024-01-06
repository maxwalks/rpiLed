from flask import Flask, render_template, jsonify
import test

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        import subprocess
        # Run command
        command = subprocess.run(['uhubctl', '-l', '1-1', '-a', 'toggle'], capture_output=False, text=True)

    return render_template('index.html')