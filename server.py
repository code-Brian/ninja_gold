from flask import Flask, render_template, redirect, request, session
from random import randint

app = Flask(__name__)
app.secret_key ='1234567890'

@app.route('/')
def index():
    if 'balance' not in session:
        session['balance'] = 0
    print("here's the index file!")
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    if request.form['hidden'] == 'farm':
        random = randint(10,20)
        session['balance'] += random
    elif request.form['hidden'] == 'cave':
        random = randint(5,10)
        session['balance'] += random
    elif request.form['hidden'] == 'house':
        random = randint(2,5)
        session['balance'] += random
    else:
        random = randint(1,100)
        if random > 50:
            session['balance'] += 50
        else:
            session['balance'] -= 50

    return render_template('index.html', balance_on_template = session['balance'])

if __name__ == '__main__':
    app.run(debug=True)