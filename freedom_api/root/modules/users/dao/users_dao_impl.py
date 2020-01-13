from root.config.db_config import SQLDatabase   #importing Database class
conn = SQLDatabase()                            #creating Database class object# -*- coding: utf-8 -*-


from root.modules.utility.app_util import cypherPassword
cp = cypherPassword()

import random
import string

from flask_jwt_extended import create_access_token


def register_users(pkey_user,created_on,user_name,full_name,password,email,primary_phone,secondary_phone):
        try:
            dbconn = conn.getConnection()           #creating Database connection parameter
            bcrypt = cp.bcryptP()
            sql = "SELECT * FROM C_SYS_USER where USER_NAME = '" + str(user_name) +"' or EMAIL= '" + str(email) +"' "
            cursor = conn.query(sql, dbconn)
            rv = cursor.fetchone()
            
            if rv is not None:
                return {'result': 'Username already exists!'}
            else:
                
                password = bcrypt.generate_password_hash(password).decode ('utf-8')
                print(password)
                sql1 = "INSERT INTO C_SYS_USER (PKEY_USER, CREATE_DATE, CREATED_BY, LAST_UPDATE_DATE, UPDATED_BY, USER_NAME, FULL_NAME, PASSWORD, EMAIL, PRIMARY_PHONE, SECONDARY_PHONE) VALUES('" + str(pkey_user) + "','" + str(created_on) + "','" + str(user_name) + "','" + str(created_on) + "','" + str(user_name) + "','" + str(user_name) + "','" + str(full_name) + "','" + str(password) + "','" + str(email) + "','" + str(primary_phone) + "','" + str(secondary_phone) + "')"
                
                cursor = conn.query(sql1, dbconn)
                conn.commit(dbconn)
                result = {'message':'New user created successfully!',
                      'pkey_user':pkey_user,
                      'user_name':user_name,
                      'full_name':full_name,
                      'email':email,
                      'password':password,
                      'primary_phone':primary_phone,
                      'secondary_phone':secondary_phone,
                      'created_on':created_on
                      }
                
            return result
            
            del dbconn                              #destroying Database connection
#        except (conn.Error, conn.Warning) as e:
#            return {'error': str(e)}
        except Exception as e:            
            return {'error': str(e)}
        
        
def login_users(user_name,email,password):

        try:
            dbconn = conn.getConnection()
            bcrypt = cp.bcryptP()
            print(email,user_name)
            sql = "SELECT * FROM C_SYS_USER where EMAIL = '" + str(email) +"' or USER_NAME= '" + str(user_name) +"'"
            cursor = conn.query(sql, dbconn)
            rv = cursor.fetchone()
            
            if rv is None:
                return {'result': 'User not exists'}
            else:
#                result = {'user_name': rv[8],
#                              'full_name': password,
#                              'email': rv[9],
#                              'pkey_user':rv[0],
#                              'message':'Login Successful'}
                print(password)
                print(bcrypt.check_password_hash(rv[8], password))
                if bcrypt.check_password_hash(rv[8], password):
                    access_token = create_access_token(identity = {'user_name': rv[5], 'full_name': rv[7], 'email': rv[9]})
                    
                    result = {'token': access_token,
                              'user_name': rv[5],
                              'full_name': rv[7],
                              'email': rv[9],
                              'pkey_user':rv[0],
                              'message':'Login Successful'}
                                        
                    return result
                else:
                    result = {"error":"Invalid password"}
                    return result
                    
            del dbconn                              #destroying Database connection

        except Exception as e:
            print(str(e))
            return {'error': str(e)}
        
        
def getallusers():
        try:
            dbconn = conn.getConnection()
            sql = """ SELECT PKEY_USER
            ,CREATE_DATE
            ,CREATED_BY
            ,LAST_UPDATE_DATE
            ,UPDATED_BY
            ,USER_NAME
            ,DESCRIPTION
            ,FULL_NAME
            ,EMAIL
            ,PRIMARY_PHONE
            ,SECONDARY_PHONE
            ,ADMIN_IND
            FROM C_SYS_USER """
            cursor = conn.query(sql, dbconn)
            rv = cursor.fetchall()
            
            if rv is None:
                return {'result': 'No user register'}
            else:                
                rowarray_list = []
                for row in rv:
                    t = {'PKEY_USER':row.PKEY_USER, 
                                 'CREATE_DATE':row.CREATE_DATE, 
                                 'CREATED_BY':row.CREATED_BY, 
                                 'LAST_UPDATE_DATE':row.LAST_UPDATE_DATE, 
                                 'UPDATED_BY':row.UPDATED_BY, 
                                 'USER_NAME':row.USER_NAME, 
                                 'DESCRIPTION':row.DESCRIPTION, 
                                 'FULL_NAME':row.FULL_NAME, 
                                 'EMAIL':row.EMAIL, 
                                 'PRIMARY_PHONE':row.PRIMARY_PHONE, 
                                 'SECONDARY_PHONE':row.SECONDARY_PHONE, 
                                 'ADMIN_IND':row.ADMIN_IND}
                    rowarray_list.append(t)
                return(rowarray_list)
                
            del dbconn                              #destroying Database connection
        except Exception as e:
            print(str(e))
            return {'error': str(e)}
        
        
        
def randomString(stringLength):
    """Generate a random string with the combination of lowercase and uppercase letters """
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))

def forgotpassword(email):
    
        try:
            dbconn = conn.getConnection()
            bcrypt = cp.bcryptP()
            sql = "SELECT * FROM C_SYS_USER where EMAIL= '" + str(email) +"'"
            cursor = conn.query(sql, dbconn)
            rv = cursor.fetchone()
            
            if rv is not None:
                temp_password = randomString(10)
                new_password = bcrypt.generate_password_hash(temp_password).decode ('utf-8')
                sql1 = "UPDATE C_SYS_USER SET PASSWORD = '" + str(new_password) +"' WHERE PKEY_USER = '"+ str(rv[0]) +"'"
                cursor = conn.query(sql1, dbconn)
                conn.commit(dbconn)
                
                result = {'pkey_user':rv[0],
                  'user_name':rv[5],
                  'full_name':rv[7],
                  'email':email,
                  'password':temp_password,
                  'message':'Password has been successfully reset!'}
                return result
            
            del dbconn                              #destroying Database connection
        except Exception as e:
            
            return {'error': str(e)}
                
