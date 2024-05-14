from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

t=[]

@app.route('/')
def print():
    return t


@app.route('/form')
def welcome():
    return render_template('index.html')

@app.route('/info')
def printinfo():
    return 'This project is created by George, Jenil, Justin, and Kevin'

@app.route('/home')
def renderhome():
    return 'This is where the home page is.'

@app.route('/results/<int:marks>')
def results(marks):
    if marks < 50:
        return redirect(url_for('fail', score=marks))
    else:
        return redirect(url_for('pas', score=marks))

@app.route('/passed/<int:score>')
def pas(score):
    return 'The student\'s parents are Asian and they are disappointed with the marks: ' + str(score)

@app.route('/failed/<int:score>')
def fail(score):
    return 'The student has failed with: ' + str(score)

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        t=[]
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data = float(request.form['datascience'])
        t.append(science)
        t.append(maths)
        t.append(c)
        t.append(data)
        totalc = (science + maths + c + data) / 4
        #print("Total Score:", totalc)
        return redirect(url_for('results', marks=int(totalc)))

if __name__ == '__main__':
    app.run(debug=True)
