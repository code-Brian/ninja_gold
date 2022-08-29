from flask import Flask, render_template, redirect, request, session
from random import randint

app = Flask(__name__)
app.secret_key ='1234567890'

@app.route('/')
def index():
    if 'balance' not in session:
        session['balance'] = 0
    if 'journal' not in session:
        session['journal'] = []
        session['journal'].append('<li class="list-group-item text-info">Welcome to Ninja Gold!</li>')
    print("here's the index file!")
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    if request.form['hidden'] == 'farm':
        random = randint(10,20)
        message = f"<li class='list-group-item bg-success'> Added {random} gold to purse.</li>"
        session['balance'] += random
        session['journal'].append(message)
    elif request.form['hidden'] == 'cave':
        random = randint(5,10)
        message = f"<li class='list-group-item bg-success'> Added {random} gold to purse.</li>"
        session['balance'] += random
        session['journal'].append(message)
    elif request.form['hidden'] == 'house':
        random = randint(2,5)
        message = f"<li class='list-group-item bg-success'> Added {random} gold to purse.</li>"
        session['balance'] += random
        session['journal'].append(message)
    else:
        random = randint(1,100)
        if random > 50:
            message = f"<li class='list-group-item bg-success'> Added 50 gold to purse.</li>"
            session['balance'] += 50
            session['journal'].append(message)
        else:
            message = f"<li class='list-group-item bg-danger'> Subtracted 50 gold from purse.</li>"
            session['balance'] -= 50
            session['journal'].append(message)

    return render_template('index.html', balance_on_template = session['balance'], journal_on_template = session['journal'])

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)