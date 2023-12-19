from flask import Flask, render_template
from api import login, write

url = 'https://192.168.10.61/api/jsonrpc'
token = login(url)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/on', methods=['POST'])
def turn_on():
    write(url, token, 'ein', True)
    return 'Turned on'

@app.route('/off', methods=['POST'])
def turn_off():
    write(url, token, 'ein', False)
    return 'Turned off'

if __name__ == '__main__':
    app.run(debug=True)
