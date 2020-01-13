from root.config.db_config import SQLDatabase   #importing Database class

import os
from flask import Flask, render_template, url_for, json
import re
import pandas as pd
from flask import request, jsonify
import numpy as np
import random 
import string 
import json

from root import app

conn = SQLDatabase()                            #creating Database class object
#cur = conn.getConnection()  
home_directory = "C:\\workings\\Python\\testFolder\\"
UPLOAD_FOLDER = "C:\\workings\\Python\\testFolder\\"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def getFileDetails(ac_token, user_id):
    try:
        dbconn = conn.getConnection()           #creating Database connection parameter
        sql = "SELECT * FROM C_SYS_SRC_GEN WHERE AC_TOKEN = '" + str(ac_token) + "' AND USER_ID ='"+ str(user_id) +"'"
        cursor = conn.query(sql, dbconn)
        rv = cursor.fetchone()

        return  {'FILE_NAME': rv.TARGET_FILE_NAME,'FILE_PATH': rv.TARGET_FILE_PATH,'FILE_ID':rv.PKEY_SRC_GEN}

        del dbconn

#    except IOError as e:
#        result = "I/O error"+str(e)
#    except ValueError as e:
#        result = "ValueError error"+str(e)
#    except:
#        raise
#
#    return result
        
    except Exception as e:
        return {'error': str(e)}




def getProjectDetails(project_ac_token, user_id):
    try:
        dbconn = conn.getConnection()  # creating Database connection parameter
        sql = "SELECT * FROM C_SYS_PROJECTS WHERE AC_TOKEN = '" + str(project_ac_token) + "' AND USER_ID ='" + str(
          user_id) + "'"
        cursor = conn.query(sql, dbconn)
        rv = cursor.fetchone()
        return rv
        del dbconn

#  except IOError as e:
#    result = "I/O error" + str(e)
#  except ValueError as e:
#    result = "ValueError error" + str(e)
#  except:
#    raise
#
#  return result
    
    except Exception as e:
       return {'error': str(e)}

def getFileList(project_id, user_id):
    try:
        dbconn = conn.getConnection()  # creating Database connection parameter
        sql = "SELECT * FROM C_SYS_SRC_GEN WHERE PROJECT_ID = '" + str(project_id) + "' AND USER_ID ='" + str(user_id) + "' ORDER BY PKEY_SRC_GEN DESC"
        cursor = conn.query(sql, dbconn)
        rv = cursor.fetchall()
        rowarray_list =[]
        for value in rv:
          t = {'PKEY_SRC_GEN': value.PKEY_SRC_GEN,
               'FILE_NAME': value.TARGET_FILE_NAME,
               'AC_TOKEN': value.AC_TOKEN
               }
          rowarray_list.append(t)
        return rowarray_list
        del dbconn
    
#      except IOError as e:
#        result = "I/O error" + str(e)
#      except ValueError as e:
#        result = "ValueError error" + str(e)
#      except:
#        raise
#    
#      return result
    except Exception as e:
        return {'error': str(e)}


def ran_gen(size, chars=string.ascii_uppercase + string.digits): 
    return ''.join(random.choice(chars) for x in range(size)) 



def saveConsolidation(project_ac_token,user_id,actual_file, files ,con_file_name):
    try:
        dbconn = conn.getConnection()  # creating Database connection parameter
        project_details = getProjectDetails(project_ac_token, user_id)
        project_id = project_details.PKEY_PROJECTS
        
        getData = getFileDetails(actual_file, user_id)
        json_url = os.path.join(os.path.abspath(getData['FILE_PATH']), "", getData['FILE_NAME'])
        foo = open(json_url)
        file1 = json.load(foo)
        foo.close()
        
        
        
        column1 = list()
        result_data = list();
        
        ###   get columns from 1st Array
        for i in file1[0].keys():
            column1.append(i) 
                
        
        for value in files:
            if actual_file!=value:
                column2 = list()
                common_col = list()
                
                ###   Read 2nd File
                getData2 = getFileDetails(value, user_id)
                json_url2 = os.path.join(os.path.abspath(getData2['FILE_PATH']), "", getData2['FILE_NAME'])
                foo2 = open(json_url2)
                file2 = json.load(foo2)
                foo2.close()
                
                ###   get columns from 2nd Array
                for i in file2[0].keys():
                    column2.append(i) 
                new_array = np.intersect1d(column1, column2)
                
                for i in new_array:
                    common_col.append(i)                    
                    
                ###   Merge Both array
                A = pd.DataFrame(file1)
                B = pd.DataFrame(file2)
                merge_data = pd.merge(A, B, on=common_col)                
                column1 = common_col
                result_data = pd.DataFrame.to_json(merge_data, orient='records',lines=False)
                file1 = result_data 
                
       
        #####  insert data into CONSOLIDATION  (START) ####
        ac_token = ran_gen(8, "Rf2IdqUNkURNN6mw82kSpyxQe9ib3usX")
        
        sql1 = "INSERT INTO C_SYS_CONSOLIDATION (AC_TOKEN, PROJECT_ID, USER_ID, CON_NAME) VALUES ('"+str(ac_token)+"','"+str(project_id)+"','"+str(user_id)+"','"+str(con_file_name)+"')"
        conn.query(sql1, dbconn)
        conn.commit(dbconn)
        
        sql = "SELECT max(PKEY_CON) as ID FROM C_SYS_CONSOLIDATION"
        cursor = conn.query(sql, dbconn)
        rv = cursor.fetchone()    
        con_id = rv.ID
        
        file_name_only = "confile"+str(con_id)
        target_directory = home_directory+user_id+'\\consolidation\\'
        if not os.path.exists(target_directory):
            os.makedirs(target_directory)
             
        decode_result_data = (json.loads(result_data))
         
        target_file_name = file_name_only+'.json'
        with open(target_directory+''+target_file_name,'w', encoding='utf-8') as f:
            json.dump(decode_result_data,f,ensure_ascii=False)
        
        sql2 = "UPDATE C_SYS_CONSOLIDATION SET FILE_NAME='"+str(target_file_name)+"', FILE_PATH='"+str(target_directory)+"' WHERE PKEY_CON='"+str(con_id)+"'"
        conn.query(sql2, dbconn)
        conn.commit(dbconn)
        
        con_file_token = ac_token
        sql = "INSERT INTO C_SYS_SRC_GEN (AC_TOKEN, PROJECT_ID, USER_ID, TARGET_FILE_NAME, TARGET_FILE_PATH) VALUES ('"+str(con_file_token)+"','"+str(project_id)+"','"+str(user_id)+"','"+str(target_file_name)+"','"+str(target_directory)+"')"
        conn.query(sql, dbconn)
        conn.commit(dbconn)
        #####  insert data into CONSOLIDATION (END) ####
        
        
        for value in files:
            ac_token = ran_gen(8, "Rf2IdqUNkURNN6mw82kSpyxQe9ib3usX")
            fileDetails = getFileDetails(value, user_id)  
            sql = "INSERT INTO C_SYS_CONSOLIDATION_FILES (AC_TOKEN,CON_ID,USER_ID, PROJECT_ID, FILE_NAME, FILE_PATH) VALUES ('"+str(ac_token)+"','"+str(con_id)+"','"+str(user_id)+"','"+str(project_id)+"','"+str(fileDetails['FILE_NAME'])+"','"+str(fileDetails['FILE_PATH'])+"')"
            conn.query(sql, dbconn)
            conn.commit(dbconn)
        
        
        return jsonify({'result':1, 'token':con_file_token})
        
        del dbconn
    
#      except IOError as e:
#        result = "I/O error" + str(e)
#      except ValueError as e:
#        result = "ValueError error" + str(e)
#      except:
#        raise
#    
#      return result
    except Exception as e:
        return {'error': str(e)}


