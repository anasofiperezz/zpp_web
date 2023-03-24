from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)
url = 'https://api-todo-list-dvtp.onrender.com/api/tasks'

@app.route('/')
def home():
    try:
        response = requests.get(url).json()['tasks']
        print(response)
    except:
        print("Error...")
        response = ()
    return render_template('index.html',  tasks = response)
if __name__ == '__main__':
    app.run(debug = True)