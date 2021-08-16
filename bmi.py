from threading import main_thread
from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result/',methods=['POST'])
def bmi_res():
    if request.method=='POST':
        email=request.form['email_name']
        print(email)
    return render_template('bmi_res.html')

if __name__=='__main__':
    app.debug=True
    app.run()