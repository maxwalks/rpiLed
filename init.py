from flask import Flask, render_template
import subprocess
from requests import request

activate_this_file = "/var/www/html/rpiLed/venv/bin/activate_this.py"
with open(activate_this_file) as _file:
        exec(_file.read(), dict(__file__=activate_this_file))

app = Flask(__name__, template_folder='template')

@app.route('/')
async def index():
    return render_template('index.html')

@app.route('/toggle-lights/')
async def toggle_lights():
      subprocess.run(['uhubctl', '-l', '1-1', '-a', 'toggle'], capture_output=False, text=True)
      return render_template('index.html')

@app.route('/lights-on/')
async def lights_on():
       subprocess.run(['uhubctl', '-l', '1-1', '-a', '1'], capture_output=False, text=True)
       return render_template('lights-on.html')

@app.route('/lights-off/')
async def lights_off():
       subprocess.run(['uhubctl', '-l', '1-1', '-a', '0'], capture_output=False, text=True)
       return render_template('lights-off.html')



if __name__ == '__main__':
       app.run(debug=True)