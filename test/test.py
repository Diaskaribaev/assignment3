import users  
import jwt  
from flask.helpers import make_response
from flask import request  
from datetime import datetime, timedelta


app = users.app                                  
app.config['SECRET_KEY'] = 'thisismyflasksecretkey'        


@app.route('/login')
def login():                               
    userautho = request.authorization
    userid = 1                  
    users.authorizationn.sqlconnection(userid)

    if userautho and userautho.username == users.username and userautho.password == users.passw0rd: 
        login.token = jwt.encode({'user':userautho.username, 'exp':datetime.utcnow() + timedelta(minutes=60)}, app.config['SECRET_KEY'])  
        
        update_this =   users.authorizationn.query.filter_by(id=userid).first()  
        update_this.token = '''{}'''.format(login.token)                              
        users.db.session.commit()
        
        return "token: " + '''{}'''.format(login.token)   

    return make_response('There is no user with such login: ' + users.username, 401, {'WWW-userauthoenticate': 'Basic realm="Login required'})  


@app.route('/protected')

def protected():       
    token = request.args.get('token')             

    protected.tokenvalue = '''{}'''.format(token)        
    login.token = '''{}'''.format(login.token)    


    if login.token == protected.tokenvalue:                                
        return '<h3>This token satisfies the condition</h3>'   
          
    else:
        return '<h3>This token is not verified</h3>'   


if __name__ == '__main__':     
    app.run(debug=True)