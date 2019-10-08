from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', pageTitle='Flask Server Home Page')

@app.route('/chengze')
def chengze():
    return render_template('chengze.html', pageTitle='About Chengze')

if __name__ == '__main__':
    app.run(debug=True)
