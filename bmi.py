from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from mail import send_mail

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
db=SQLAlchemy(app)

class User_data(db.Model):
    __tablename__="User_Data"
    sno=db.Column(db.Integer,primary_key=True)
    user_name=db.Column(db.String(25))
    user_email=db.Column(db.String,nullable=False)
    user_age=db.Column(db.Integer)
    user_height=db.Column(db.Integer)
    user_weight=db.Column(db.Integer)

    # def __repr__(self) -> str:
    #     return f"{self.sno}"

    def __init__(self,user_email,user_height,user_weight):
        self.user_email=user_email
        self.user_height=user_height
        self.user_weight=user_weight
        

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result/',methods=['POST'])
def bmi_res():
    if request.method=='POST':
        email=request.form['email_name']
        height=request.form['height']
        weight=request.form['weight']
        user_bmi=(weight)/((weight/100)**2)

        if db.session.query(User_data).filter(User_data.user_email==email).count()==0:
            data=User_data(email,height,weight)
            db.session.add(data)
            db.session.commit()
            send_mail(email,height,weight,user_bmi)
            return render_template('bmi_res.html')
    return render_template('home.html',text='Seems like you have previously used this email address')
if __name__=='__main__':
    app.debug=True
    app.run()