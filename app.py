from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/success')
def success():
    return "Successfully deployed Flask App on Vercel"

if __name__ == '__main__':
    app.run()