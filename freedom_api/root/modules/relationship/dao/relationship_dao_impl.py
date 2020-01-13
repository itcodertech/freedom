from root.config.db_config import SQLDatabase   #importing Database class
conn = SQLDatabase()                            #creating Database class object
import json
import pandas as pd
import os
import re

import root.conf as conf

home_directory = conf.home_directory

def createrelationshipFn(updated_by,relation_on,join_type,obj_name,cur_date,sources):
    try:
        dbconn = conn.getConnection()           #creating Database connection parameter
        
        sources = json.loads(sources)
        maindataframe=pd.DataFrame(sources)
        rowcount = len(maindataframe)
        
        if rowcount > 1:
            file1 = maindataframe['path'][0]+maindataframe['json_obj'][0]
            file2 = maindataframe['path'][1]+maindataframe['json_obj'][1]
            
            
            
            df1 = pd.read_json(file1)
            df2 = pd.read_json(file2)
            
            target_directory = home_directory+updated_by+'\\relationship\\'
            if not os.path.exists(target_directory):
                os.makedirs(target_directory)
                
            target_directory_1 = home_directory+updated_by+'\\'
            if not os.path.exists(target_directory):
                os.makedirs(target_directory)
            
            relationship_file_name = obj_name+".json"
            ctl_key = updated_by+re.sub('[^A-Za-z0-9]+', '', obj_name)
            
            new_df = pd.merge(df1, df2, on=relation_on, how=join_type)
            
            new_df.to_json(target_directory+relationship_file_name, orient='records')
            new_df.to_json(target_directory_1+relationship_file_name, orient='records')
            
            output_res = new_df.to_json(orient='records')
            
            output_res = json.loads(output_res)
        
        else:
    #        pass
            file1 = maindataframe['path'][0]+maindataframe['json_obj'][0]
            file_name = maindataframe['file_name'][0]
            file_name_only = os.path.splitext(file_name)[0]
    #        print(file_name)
            new_df = pd.read_json(file1)
            
            target_directory = home_directory+updated_by+'\\relationship\\'
            if not os.path.exists(target_directory):
                os.makedirs(target_directory)
                
            target_directory_1 = home_directory+updated_by+'\\'
            if not os.path.exists(target_directory):
                os.makedirs(target_directory)
            
            if obj_name != "":
                relationship_file_name = obj_name+".json"
            else:
                relationship_file_name = file_name_only+".json"
            
            new_df.to_json(target_directory+relationship_file_name, orient='records')
            new_df.to_json(target_directory_1+relationship_file_name, orient='records')
        
            output_res = new_df.to_json(orient='records')
            
            output_res = json.loads(output_res)
        
        if obj_name != "":
            sql = "SELECT * FROM C_SYS_UPLOADED_FILES WHERE CONVERT(VARCHAR, RELATIONSHIP_FILE_NAME) = '"+str(relationship_file_name)+"' AND CREATED_BY = '"+str(updated_by)+"'"
        else:
            sql = "SELECT * FROM C_SYS_UPLOADED_FILES WHERE FILE_NAME = '"+str(file_name)+"' AND CREATED_BY = '"+str(updated_by)+"'"

        cursor = conn.query(sql, dbconn)
        rv = cursor.fetchone()
        
        if rv is None:
            conn.query("INSERT INTO C_SYS_UPLOADED_FILES (FILE_NAME, FILE_EXT, FILE_PATH, TARGET_FILE_PATH, TARGET_FILE_NAME, CREATE_DATE, CREATED_BY, LAST_UPDATE_DATE, UPDATED_BY, RELATIONSHIP_FILE_NAME, RELATIONSHIP_FILE_PATH, CTL_KEY) VALUES('" + 
                            str(relationship_file_name) + "','JSON','" +
                            str(target_directory) + "','" +
                            str(target_directory_1) + "','" +
                            str(relationship_file_name) + "','" +
                            str(cur_date) + "','" +
                            str(updated_by) + "','" +
                            str(cur_date) + "','" +
                            str(updated_by) + "','" +
                            str(relationship_file_name) + "','" +
                            str(target_directory) + "','" +
                            str(ctl_key) + "')")
            conn.commit()
            result = {'created_on':cur_date,
              'created_by':updated_by,
              'relationship_file_name':relationship_file_name,
              'relationship_file_path':target_directory,
              'last_update_date':cur_date,
              'updated_by':updated_by,
              'file_content':output_res,
              'ctl_key':ctl_key,
              'message':'Relationsip object has been updated successfully'
            }
        else:
            conn.query("UPDATE C_SYS_UPLOADED_FILES SET LAST_UPDATE_DATE= '" + str(cur_date) +"', UPDATED_BY= '" + str(updated_by) +"', RELATIONSHIP_FILE_NAME= '" + str(relationship_file_name) +"', RELATIONSHIP_FILE_PATH= '" + str(target_directory) +"' WHERE CTL_KEY= '" + str(rv.CTL_KEY) +"'", dbconn)
            result = {'relationship_file_name':relationship_file_name,
              'relationship_file_path':target_directory,
              'last_update_date':cur_date,
              'updated_by':updated_by,
              'file_content':output_res,
              'message':'Relationsip object has been updated successfully'
            }
        return result
        del dbconn                              #destroying Database connection
    except Exception as e:
        return {'error': str(e)}