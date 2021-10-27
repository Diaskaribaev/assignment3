from sqlalchemy import create_engine
from sqlalchemy.sql import text 

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
  
app = Flask(__name__)       
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:5432@localhost/flask' 

db = SQLAlchemy(app)   

engine = create_engine('postgresql://postgres:5432@localhost/flask')  


class authorizationn(db.Model):             
    __tablename__ = 'authorizationn'
    id = db.Column ('id', db.Integer, primary_key=True)   
    login = db.Column ('login', db.Unicode)
    password = db.Column ('password', db.Unicode)
    token = db.Column ('token', db.Unicode)


    def __init__(self, id, login, password, token):
        self.id = id
        self.login = login
        self.password = password
        self.token = token
    username = ''     
    passw0rd = ''  

    def sqlconnection(id):                         
        with engine.connect() as connection:

            result = connection.execute(text("select login, password from authorizationn where authorizationn.id = " +str(id)))
            
            for row in result:
                global username, passw0rd
                username = row['login']
                passw0rd = row['password']
        connection.close()                        


#db.create_all()                          

#new_user = authorizationn(1,'random', 'password', 'randomtoken')      
#db.session.add(new_user)                                                              
#db.session.commit()
