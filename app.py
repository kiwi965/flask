from flask import Flask
from flask import redirect# this is to redirect you to another page 
from flask import url_for #to access the url dynamically ////just use it
from flask import render_template
app=Flask(__name__)#wsgi application inititlaision that communicates with the server 




@app.route('/')#decorator the / is url in string format  and its the first parameter and there is a second parameter 
def welcome():# biding function 
    #return'kevin benny thukkuparambil'
    return render_template('index.html')

@app.route('/info')
def printinfo():
    return 'This project is created by george,jenil,justin and kevin'


@app.route('/home')
def renderhome():
    return 'This is where the home page is.'


@app.route('/results/<int:marks>')
def re(marks):
    result=''
    if(marks<50):
      
        result='fail'
    else:
       
        result='pas'
    return redirect(url_for(result,score=marks))#the first variable needs the fkingf binding function and not the url name 

@app.route('/passed/<int:score>')
def pas(score):
    return 'The students parents are asian and they are disapointed witht the marks'+ str(score)

@app.route('/failed/<int:score>')
def fail(score):
    return 'The students has failed with '+ str(score)

if __name__=='__main__':# basically main function 
    app.run(debug=True)#ddebug is true is used to restart tje server if u make a change 



























