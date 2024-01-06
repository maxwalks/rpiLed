from requests import request
from flask import Flask, render_template
import subprocess

activate_this_file = "/var/www/html/rpiLed/venv/bin/activate_this.py"
with open(activate_this_file) as _file:
        exec(_file.read(), dict(__file__=activate_this_file))

app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/toggle-lights/')
def toggled():
      import subprocess
      # Run command
      command = subprocess.run(['uhubctl', '-l', '1-1', '-a', 'toggle'], capture_output=False, text=True)
      return render_template('index.html')


if __name__ == '__main__':
        app.run(debug=True)