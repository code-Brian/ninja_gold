from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key ='1234567890'

@app.route('/')
def index():
    print("here's the index file!")
    return render_template('index.html')
    
if __name__ == '__main__':
    app.run(debug=True)