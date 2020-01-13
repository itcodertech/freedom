from flask import Blueprint
from root.modules.users.dao.users_dao_impl import register_users, login_users, getallusers, forgotpassword

from datetime import datetime
from flask import request, jsonify
import random

mod = Blueprint ('users',__name__)


@mod.route('/register-user', methods=['GET', 'POST'])
def registerUsers():
    try:
        if request.method == "POST":
            pkey_user = random.randrange(1000, 999999999, 2)
            user_name = request.get_json()['user_name']
            full_name = request.get_json()['full_name']
            password = request.get_json()['password']
            email = request.get_json()['email']
            primary_phone = request.get_json()['primary_phone']
            secondary_phone = request.get_json()['secondary_phone']
            created_on = datetime.utcnow()
            
            return jsonify(register_users(pkey_user,created_on,user_name,full_name,password,email,primary_phone,secondary_phone))
#            return jsonify({'message': 'User register sucessfully'})
        
    except Exception as e:
        return jsonify({'error': str(e)})
    
    
@mod.route('/login', methods=['GET','POST'])
def loginUsers():
    try:
        if request.method == 'POST':
            user_name = request.get_json()['user_name']
            email = request.get_json()['email']
            password = request.get_json()['password']
            print(user_name)
        if user_name == '' and email == '':
            return jsonify({"error":"Please fill up mandatory fields!"})
            
        else:                       
            return jsonify(login_users(user_name,email,password))
            
    except Exception as e:
        return jsonify({'error': str(e)})
    

    
#@mod.route('/get-users', methods=['GET','POST'])
#def getAllUsers():
#    try:
#        if request.method == 'GET':
#            return jsonify(getallusers())
#    except Exception as e:
#        return jsonify({'error': str(e)})
    
    
    
@mod.route('/forgot-password', methods=['GET','POST'])
def forgotPassword():
    try:
        if request.method == 'POST':
            email = request.get_json()['email']
            
        if email == '':
            return jsonify({"error": "Email required"})
        
        else:
            return jsonify(forgotpassword(email))
        
    except Exception as e:
        return jsonify({'error': str(e)})


