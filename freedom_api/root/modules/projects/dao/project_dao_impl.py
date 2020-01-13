from root.config.db_config import SQLDatabase   #importing Database class
conn = SQLDatabase()                            #creating Database class object

import secrets


    
def createProject(user_id,project_name,ingestion,curation,reports,created_at,proj_desc):
    try:
        dbconn = conn.getConnection()           #creating Database connection parameter
        sql = "SELECT * FROM C_SYS_PROJECTS where PROJECT_NAME = '" + str(project_name) +"' AND USER_ID = '" + str(user_id) +"'"
        cursor = conn.query(sql, dbconn)
        rv = cursor.fetchone()        

        if rv is not None:
            result = {'message':project_name+' is already created on '+rv.CREATED_AT+'!',
                    'project_name':rv.PROJECT_NAME,
                    'user_id':rv.USER_ID,
                    'created_at':rv.CREATED_AT,
                    'ac_token':rv.AC_TOKEN}
            
        else:
            active_ind = '1'
#            str_token = user_id + project_name + str(created_at)
            ac_token = secrets.token_urlsafe(20)
            print(ac_token)
            sql1 = "INSERT INTO C_SYS_PROJECTS (AC_TOKEN, USER_ID, PROJECT_NAME, INGESTION, CURATION, REPORTS, PROJ_DESC, UPDATED_BY, ACTIVE_IND, CREATED_AT, UPDATED_AT) VALUES('" +str(ac_token)+"', '"+str(user_id)+"','" +str(project_name) + "', '" + str(ingestion) + "', '" + str(curation) + "', '" + str(reports) + "', '" + str(proj_desc) + "','" + str(user_id) + "', '" +str(active_ind)+"','"+ str(created_at) + "','"+str(created_at)+ "' )"
            conn.query(sql1, dbconn)
            conn.commit(dbconn)
            result = {'message':'New project "'+project_name+'" has been created successfully!','ac_token':ac_token}
        return result
        del dbconn                              #destroying Database connection
    except Exception as e:
        return {'error': str(e)}
    
    
def getAllProjects(pkey_user):
    try:
        dbconn = conn.getConnection()           #creating Database connection parameter
        sql = "SELECT * FROM C_SYS_USER where PKEY_USER = '" + str(pkey_user) +"' "
        cursor = conn.query(sql, dbconn)
        rv = cursor.fetchone()
        user_name = rv.USER_NAME
        
        if rv is None:
            return {'result': 'Unauthenticate access!'}
        else:
            active_ind = 1
            sql1 = "SELECT * FROM C_SYS_PROJECTS WHERE USER_ID = '" + str(pkey_user) +"'AND ACTIVE_IND = '" +str(active_ind)+"' ORDER BY CREATED_AT DESC"
          
            cursor = conn.query(sql1, dbconn)  
            rows = cursor.fetchall()
            
            rowarray_list = []
            for row in rows:
                t = {'PKEY_PROJECTS':row.PKEY_PROJECTS,
                     'Notebook_Id':row.AC_TOKEN,
                     'Notebook_Name':row.PROJECT_NAME,
                     'Created_By':user_name,
                     'Created_On':row.CREATED_AT,
                     'Last_Modified':row.UPDATED_AT}
                
                rowarray_list.append(t)
            return rowarray_list
        del dbconn                              #destroying Database connection
    except Exception as e:
        return {'error': str(e)}
    
    
def editProject(ac_token,updated_by,ingestion,curation,reports,update_at,proj_desc):
    try:
        dbconn = conn.getConnection()           #creating Database connection parameter
        sql = "SELECT * FROM C_SYS_PROJECTS where AC_TOKEN = '" + str(ac_token) +"'"
        cursor = conn.query(sql, dbconn)
        rv = cursor.fetchone()
        
        if rv is not None:
            if rv.USER_ID == updated_by:
                sql1 = "UPDATE C_SYS_PROJECTS SET INGESTION = '" + str(ingestion) + "', CURATION = '" + str(curation) + "', REPORTS = '" + str(reports) + "', UPDATED_BY = '" + str(updated_by) + "', UPDATED_AT = '" + str(update_at) + "' where AC_TOKEN = '" + str(ac_token) +"'"
                cursor = conn.query(sql1, dbconn)
                conn.commit(dbconn)
                conn.query("SELECT * FROM C_SYS_PROJECTS where AC_TOKEN = '" + str(ac_token) +"' ", dbconn)
                rv = cursor.fetchone()
                result = {'message':rv.PROJECT_NAME+' has been updated successfully!',
                        'AC_TOKEN':rv.AC_TOKEN,
                        'PROJECT_NAME':rv.PROJECT_NAME,
                        'UPDATED_BY':rv.UPDATED_BY,
                        'UPDATED_AT':rv.UPDATED_AT,
                        'INGESTION':rv.INGESTION.strip(),
                        'CURATION':rv.CURATION.strip(),
                        'REPORTS':rv.REPORTS.strip()}
            else:
                result = {'error':'User not matched'}
        else:
            result = {'error':'This project is not present!'}
        return result
        del dbconn                              #destroying Database connection
    except Exception as e:
        return {'error': str(e)}
    
def delProject(ac_token):
    try:
        dbconn = conn.getConnection()           #creating Database connection parameter
        sql = "SELECT * FROM C_SYS_PROJECTS where AC_TOKEN = '" + str(ac_token) +"'"
        cursor = conn.query(sql, dbconn)
        rv = cursor.fetchone()
        active_ind = 0
        if rv is not None:
            sql1 = "UPDATE C_SYS_PROJECTS SET ACTIVE_IND = '" + str(active_ind) +"' WHERE AC_TOKEN = '" +str(ac_token)+"'"
            cursor = conn.query(sql1, dbconn)
            conn.commit(dbconn)
            result = {'message':'The project has been deleted successfully!'}
        else:
            result = {'error':'This project is not present!'}
        return result
        del dbconn                              #destroying Database connection
    except Exception as e:
        return {'error': str(e)}