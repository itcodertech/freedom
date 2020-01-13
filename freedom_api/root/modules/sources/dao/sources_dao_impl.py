from root.config.db_config import SQLDatabase   #importing Database class
conn = SQLDatabase()                            #creating Database class object

from root.modules.utility.app_dictionary import CountryName, CountryCode

import csv
from collections import OrderedDict
import json
import pandas as pd
from pandas import DataFrame
from datetime import datetime
from datetime import timezone
from datetime import timedelta
import re
import os
from detect_delimiter import detect
from pathlib import Path
from flask import Flask, flash, request, redirect, render_template, jsonify
from werkzeug.utils import secure_filename
from root import app
import secrets

home_directory = "C:\\workings\\Python\\testFolder\\"

UPLOAD_FOLDER = "C:\\workings\\Python\\testFolder\\"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def default(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    return super().default(obj)

def object_hook(obj):
    _isoformat = obj.get('_isoformat')
    if _isoformat is not None:
        return datetime.fromisoformat(_isoformat)
    return obj


ALLOWED_EXTENSIONS = set(['csv', 'txt', 'xls', 'xlt', 'xlm', 'xlsx', 'xlsm', 'xltx', 'xltm', 'xlsb', 'xla', 'xlam', 'xll', 'xlw'])
allowed_header = ['email', 'phone', 'name', 'currency']

def allowedFile(file):
    filename = file.filename
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def common_member(a, b): 
    a_set = set(a) 
    b_set = set(b) 
    if (a_set & b_set): 
        return True 
    else: 
        return False
    
    
def emailCheck(data):

    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    lis = data.values.tolist()
    Tf = 0
    Ff= 0
    f=0
    for i in lis:
        j = str(i)
        if (j != 'nan'):
            
            if(re.search(regex,j)):
                f=f+1
                Tf = Tf+1
            else:
            
                Ff = Ff + 1
                          
    if(f > Ff):
        return ((f*100)/(f+Ff))
    return 0

def phoneCheck(data):
    
    regex = ['\b(?!000|.+0{4})(?:\d{9}|\d{3}-\d{2}-\d{4})\b','(\w{3})\w{3}-\w{4}','\(\w{3}\)\w{3}-\w{4}','^(0\d{10})(?:\s|$)','^(\d{10})(?:\s|$)']
    lis = data.values.tolist()
    Tf = 0
    Ff= 0
    f=0
    for i in lis:
        j = str(i)
        if (j != 'nan'):
            
            for reg in regex:
                Tf = 0
                Ff= 0
                if(re.search(reg,j)):
                    f=f+1
                    Tf = Tf+1
                else:
            
                    Ff = Ff + 1             

    if(f > Ff):
        return ((f*100)/(f+Ff))
    return 0
        
    
def genderCheck(data):
         
    regex = ['Male','Female']
    lis = data.values.tolist()
    Tf = 0
    Ff= 0
    f=0
    for i in lis:
        j = str(i)
        if (j != 'nan'):
            
            for reg in regex:
                Tf = 0
                Ff= 0
                if(re.search(reg,j)):
                    f=f+1
                    Tf = Tf+1
                else:
            
                    Ff = Ff + 1             

    if(f > Ff):
        
        return ((f*100)/(f+Ff))
    return 0
        

def addressCheck(data):
         
    regex = ['^\d+\s[A-z]+\s[A-z]+']
    lis = data.values.tolist()
    Tf = 0
    Ff= 0
    f=0
    for i in lis:
        j = str(i)
        if (j != 'nan'):
            
            for reg in regex:
                Tf = 0
                Ff= 0
                if(re.search(reg,j,re.IGNORECASE)):
                    f=f+1
                    Tf = Tf+1
                else:
            
                    Ff = Ff + 1             

    if(f > Ff):
        return ((f*100)/(f+Ff))
    return 0
        
    

def postCodeCheck(data):
         
    regex = ['([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9][A-Za-z]?))))\s?[0-9][A-Za-z]{2})']
    lis = data.values.tolist()
    Tf = 0
    Ff= 0
    f=0
    for i in lis:
        j = str(i)
        if (j != 'nan'):
            
            for reg in regex:
                Tf = 0
                Ff= 0
                if(re.search(reg,j,re.IGNORECASE)):
                    f=f+1
                    Tf = Tf+1
                else:
            
                    Ff = Ff + 1             

    if(f > Ff):
        return ((f*100)/(f+Ff))
    return 0
        
    
def CountryCodeCheck(data):
    
    regex = CountryCode()
    lis = data.values.tolist()
    Tf = 0
    Ff= 0
    f=0
    for i in lis:
        j = str(i)
        if (j != 'nan'):
            
            for reg in regex:
                Tf = 0
                Ff= 0
                if(re.search(reg,j,re.IGNORECASE)):
                    f=f+1
                    Tf = Tf+1
                else:
            
                    Ff = Ff + 1             

    if(f > Ff):
        
        return ((f*100)/(f+Ff))
    return 0
        
    
def CountryNameCheck(data):
         
    regex = CountryName()
    lis = data.values.tolist()
    Tf = 0
    Ff= 0
    f=0
    for i in lis:
        j = str(i)
        if (j != 'nan'):
            
            for reg in regex:
                Tf = 0
                Ff= 0
                if(re.search(reg,j,re.IGNORECASE)):
                    f=f+1
                    Tf = Tf+1
                else:
            
                    Ff = Ff + 1             

    if(f > Ff):
        return ((f*100)/(f+Ff))
    return 0
        


    
def titleCheck(data):
         
    regex = ['^MR$','^HONORABLE$','^MR$','^DR$','^HON$','^MRS$']
    lis = data.values.tolist()
    Tf = 0
    Ff= 0
    f=0
    for i in lis:
        j = str(i)
        if (j != 'nan'):
            
            for reg in regex:
                Tf = 0
                Ff= 0
                if(re.search(reg,j,re.IGNORECASE)):
                    f=f+1
                    Tf = Tf+1
                else:
            
                    Ff = Ff + 1             

    if(f > Ff):
        return ((f*100)/(f+Ff))
    return 0
        
   
def dateCheck(data):
       
    regex =[]
    regex = ['[\d]{1,2}/[\d]{1,2}/[\d]{4}', '[\d]{1,2} [ADFJMNOS]\w* [\d]{4}','[\d]{1,2}-[\d]{1,2}-[\d]{2}']
#    print (data.isnull().sum())
    lis = data.values.tolist()
    Tf = 0
    Ff= 0
    f=0
    for i in lis:
        j = str(i)
        if (j != 'nan'):
            
            for reg in regex:
                Tf = 0
                Ff= 0
                if(re.search(reg,j)):
                    f=f+1
                    Tf = Tf+1
                else:
            
                    Ff = Ff + 1
             
    if(f > Ff):
        return ((f*100)/(f+Ff))
    return 0

def nameCheck(data):
    
    regex = ["[a-z]{1,10}"]
             
    lis = data.values.tolist()
    Tf = 0
    Ff= 0
    f=0
    for i in lis:
        j = str(i)
        if (j != 'nan'):
            print(j)
            for reg in regex:
                Tf = 0
                Ff= 0
                if(re.search(reg,j,re.IGNORECASE)):
                    f=f+1
                    Tf = Tf+1
                else:
            
                    Ff = Ff + 1
             
    if(f > Ff):
        return ((f*100)/(f+Ff))
    return 0
    


def getClm(df):

    check=''
    ClmName = ''
    maxFlag = 0
#    check = nameCheck(df)
#    if (check > maxFlag):
#        ClmName = 'NAME'
#        maxFlag = check
    check = emailCheck(df)
    if (check > maxFlag):
        ClmName = 'EMAIL ADDRESS'
        maxFlag = check
    check = phoneCheck(df)
    if (check  > maxFlag):
        ClmName =  'PHONE NUMBER'
        maxFlag = check    
    check = dateCheck(df)
    if (check > maxFlag):
        ClmName = 'DATE'
        maxFlag = check    
    check = genderCheck(df)
    if (check > maxFlag):
        ClmName =  'GENDER'
        maxFlag = check    
    check = titleCheck(df)
    if (check > maxFlag):
        ClmName =  'TITLE'
        maxFlag = check    
    check = addressCheck(df)
    if (check > maxFlag):
        ClmName =  'ADDRESS'
        maxFlag = check    
    check = postCodeCheck(df)
    if (check > maxFlag):
        ClmName =  'POSTAL CODE'
        maxFlag = check    
    check = CountryCodeCheck(df)
    if (check > maxFlag):
        ClmName =  'COUNTRY CODE'
        maxFlag = check    
    check = CountryNameCheck(df)
    if (check > maxFlag):
        ClmName =  'COUNTRY NAME'
    
    if (ClmName == ''):
        return 0
    return ClmName

def uploadFile(ac_token,file_name,file_path,user_id):
    try:
        print(file_path)
        dbconn = conn.getConnection()
        created_on = datetime.utcnow()
        target_directory = UPLOAD_FOLDER + user_id + '\\'
        
         
        raw_data = list()
        hdata = []
        data_list = []
        
        sql = "SELECT * FROM C_SYS_PROJECTS where AC_TOKEN = '" + str(ac_token) +"'"
        cursor = conn.query(sql, dbconn)
        rv = cursor.fetchone()
        project_id = rv.PKEY_PROJECTS
        
        sfn = os.path.splitext(file_name)
        for index, value in enumerate(sfn):
            if index == 0:
                file_name_only = value
                tgt_filename = file_name_only + '.json'
                
            else:
                file_type = value
        
        file_token = secrets.token_urlsafe(20)           
        sql1 = "INSERT INTO C_SYS_UPLOADED_FILES_DETAILS (AC_TOKEN, PROJECT_ID, USER_ID, FILE_NAME, FILE_EXT, FILE_PATH, TARGET_FILE_NAME, TARGET_FILE_PATH, UPDATED_BY, CREATED_AT, UPDATED_AT) VALUES('" +str(file_token)+ "','" +str(project_id)+ "','" +str(user_id)+"','" +str(file_name)+ "','" +str(file_type)+ "','" +str(UPLOAD_FOLDER)+ "','" +str(tgt_filename)+ "','" + str(target_directory) +"','"+str(user_id)+ "','" +str(created_on)+ "','" +str(created_on)+ "')"
        cursor = conn.query(sql1, dbconn)
        conn.commit(dbconn)
        
        sql2 = "INSERT INTO C_SYS_SRC_GEN (AC_TOKEN, PROJECT_ID, USER_ID, TARGET_FILE_NAME, TARGET_FILE_PATH, UPDATED_BY, CREATED_AT, UPDATED_AT) VALUES('" +str(file_token)+ "','" +str(project_id)+ "','" +str(user_id)+"','" +str(tgt_filename)+ "','" + str(target_directory) +"','"+str(user_id)+ "','" +str(created_on)+ "','" +str(created_on)+ "')"
        cursor = conn.query(sql2, dbconn)
        conn.commit(dbconn)
        
        return {'result': 'File successfully uploaded'}
        
        
    except Exception as e:
        return {'error': str(e)}
    
def genRawPreview(file_path,file_name,user_id):
    try:
        
        with open(os.path.join(file_path, file_name), 'r', encoding='utf-8') as file:
            filehead = file.readline() # skip the first line
            hdata = []
            data_list = []
            target_directory = UPLOAD_FOLDER + user_id + '\\'
            str_filehead = ''
            for h_content in filehead:
                str_filehead += h_content
                
            sfn = os.path.splitext(file_name)
            for index, value in enumerate(sfn):
                if index == 0:
                    file_name_only = value
                    tgt_filename = file_name_only + '.json'
                    tgt_filePath = target_directory
                else:
                    file_type = value
                
            deli = detect(str_filehead,whitelist = [',', ';', ':', '|', '\t'])
            hdata.append(str_filehead.split(deli))
            for h in hdata:
                list_h = list(h)
#            print(list_h)
            
            allowed_header = ['email','phone','name', 'currency', 'merchant_id','ID','EMAIL']
    
        
            h_flag = common_member(list_h,allowed_header)
        
            rows = [[str(x) for x in line.split(deli)] for line in file]
            cols = [list(col) for col in zip(*rows)]
            
            if not os.path.exists(target_directory):
                    os.makedirs(target_directory)
            
            if h_flag == True:
                tuples = [tuple(x) for x in rows]
#                print(tuples)
                for row in tuples:
                    save_data = OrderedDict()
                    for i, r in enumerate(row):
                        save_data[list_h[i]] = row[i]
                    data_list.append(save_data)
            else:
                with open(os.path.join(file_path, file_name), 'r',encoding='utf-8') as file:
                    rows = [[str(x) for x in line.split(deli)] for line in file]
                    cols = [list(col) for col in zip(*rows)]
                    tuples = [tuple(x) for x in rows]
                    for row in tuples:
                        save_data = OrderedDict()
                        for i, r in enumerate(row):
                            j = 'col'+str(i)
                            save_data[j] = row[i]
                        data_list.append(save_data)

            with open(os.path.join(tgt_filePath,tgt_filename), 'w') as json_file:
                json.dump(data_list, json_file)
                return {'result': 'File successfully uploaded'}
    
    except Exception as e:
        return {'error': str(e)}

def previewSource(user_id,file_name,file_path,ac_token):
    try:
        dbconn = conn.getConnection()
        created_on = datetime.utcnow()
        target_directory = UPLOAD_FOLDER + user_id + '\\'
        
         
        raw_data = {}
        save_data = {}
        
        sfn = os.path.splitext(file_name)
        for index, value in enumerate(sfn):
            if index == 0:
                file_name_only = value
                tgt_filename = file_name_only + '.json'
                tgt_filePath = target_directory
            else:
                file_type = value
        
        
        with open(os.path.join(file_path,file_name), "r", encoding='utf-8') as files:
            data = files.read()
#            print(data)
            raw_data = data
            return {'raw_view':raw_data}
            
    except Exception as e:
        return {'error': str(e)}
    
def initiateSysPreview(user_id,file_name,ac_token):
    try:
        dbconn = conn.getConnection()
        hdata = []
        h_flag = ''
        SourceName= []
        ParsedName =[]
        
        sql = "SELECT TARGET_FILE_NAME, TARGET_FILE_PATH FROM C_SYS_UPLOADED_FILES_DETAILS WHERE FILE_NAME = '" + str(file_name) +"' and USER_ID= '" + str(user_id) +"' "
        cursor = conn.query(sql, dbconn)
        rows = cursor.fetchall()
        for rv in rows:
            target_filename = rv.TARGET_FILE_NAME
            target_directory = rv.TARGET_FILE_PATH

        print(target_directory)
#        with open(os.path.join(target_directory,target_filename), "r") as read_files:
        data = pd.read_json(os.path.join(target_directory,target_filename), orient='columns')
#        print(data.columns)
        col = data.columns
        for v in col:
            SourceName.append(v)
#        print(SourceName)
        ndf=pd.DataFrame(data)
        ndf = ndf.reindex(SourceName, axis=1)
        ndf = ndf.applymap(str)
        
        
             
        temp=-1
        c = 0
        
        for j in ndf.columns:
            z =ndf[j]
            c = 0
            temp = temp+1
#            print(type(z))
            resp = str(getClm(z))
            if resp != str(0):
                
                if resp in ParsedName:
                    c = c+1
                    resp = resp+str(c)
                ParsedName.append(resp)
            else:
                ParsedName.append(j.upper())
            
            

        fetched_data = []
        dataF = pd.DataFrame({'SourceName': SourceName, 'ParsedName': ParsedName})
#        print(dataF)
        ndf.columns = ParsedName
        ndf = ndf.infer_objects()
        
        for val in ndf.values:
            sys_data = OrderedDict()
            for i, v in enumerate(val):
#                    print(ndf.columns[i])
                sys_data[ndf.columns[i]] = v
            fetched_data.append(sys_data)
        with open(os.path.join(target_directory,target_filename), 'w') as json_file:
                json.dump(fetched_data, json_file)
        return {'success':'sys_source created'}
    
    except Exception as e:
        return {'error': str(e)}
    
    
def gen_sys_preview(user_id,file_name,ac_token):
    try:
        dbconn = conn.getConnection()
        ParsedCol =[]
        fetched_data = []
        ParsedName= []
        
        sql = "SELECT TARGET_FILE_NAME, TARGET_FILE_PATH FROM C_SYS_UPLOADED_FILES_DETAILS WHERE FILE_NAME = '" + str(file_name) +"' and USER_ID= '" + str(user_id) +"' "
        cursor = conn.query(sql, dbconn)
        rows = cursor.fetchall()
        for rv in rows:
            target_filename = rv.TARGET_FILE_NAME
            target_directory = rv.TARGET_FILE_PATH


        data = pd.read_json(os.path.join(target_directory,target_filename), orient='columns')            

        col = data.columns
        for v in col:
            ParsedName.append(v)
        
        ndf=pd.DataFrame(data)
        ndf = ndf.reindex(ParsedName, axis=1)
        ndf = ndf.applymap(str)

        for val in ndf.values:
            sys_data = dict()
            for i, v in enumerate(val):
                sys_data[ndf.columns[i]] = val[i]
            fetched_data.append(sys_data)
            print(fetched_data)
        return {'sys_view':fetched_data}

        
        
    except Exception as e:
        return {'error': str(e)}
    

def editColumnNames(user_id,file_name,old_col_val,new_col_val):
    try:
        dbconn = conn.getConnection()
        r_columns = {}
        data_list = []
        
        sql = "SELECT TARGET_FILE_NAME, TARGET_FILE_PATH FROM C_SYS_UPLOADED_FILES_DETAILS WHERE FILE_NAME = '" + str(file_name) +"' and USER_ID= '" + str(user_id) +"' "
        cursor = conn.query(sql, dbconn)
        rows = cursor.fetchall()
        for rv in rows:
            target_filename = rv.TARGET_FILE_NAME
            target_directory = rv.TARGET_FILE_PATH
            
        with open(os.path.join(target_directory,target_filename), "r") as read_files2:
            data = json.load(read_files2)
            
            cdf = pd.DataFrame(data)
            cdf = cdf.applymap(str)
            
            print(old_col_val)
            
            for col_val in cdf.columns:
                if old_col_val in col_val:

                    r_columns[old_col_val] = new_col_val
            
            new_data = cdf.rename(columns = r_columns)
            ParsedName = new_data.columns
            print(ParsedName)
            for val in new_data.values:
                data_dict = dict()
                for i, v in enumerate(val):
                    data_dict[ParsedName[i]] = v
                data_list.append(data_dict)
            
            with open(os.path.join(target_directory,target_filename), 'w') as json_file:
                json.dump(data_list, json_file)
                
#            print(data_list)
            return {'mod_col':data_list}
            
    except Exception as e:
        return {'error': str(e)}        


def getFilesByProject(ac_token):
    try:
        dbconn = conn.getConnection()           #creating Database connection parameter
        sql = "SELECT PKEY_PROJECTS, PROJECT_NAME, USER_ID FROM C_SYS_PROJECTS WHERE AC_TOKEN = '"+str(ac_token)+"'"
        cursor = conn.query(sql, dbconn)
        rd = cursor.fetchone()
        
        if rd is None:
            return {'result': 'Unauthenticate access!'}
        else:
            project_id = rd.PKEY_PROJECTS
            user_id = rd.USER_ID
            sql1 = "SELECT * FROM C_SYS_UPLOADED_FILES_DETAILS WHERE PROJECT_ID = '"+str(project_id)+"'AND USER_ID = '"+str(user_id)+"'"
            cursor = conn.query(sql1, dbconn)
            rows = cursor.fetchall()
            rowarray_list = []
            for row in rows:
                t = {'PROJECT_ID':row.PROJECT_ID,
                     'FILE_NAME':row.FILE_NAME,
                     'FILE_PATH':row.FILE_PATH,
                     'CREATED_AT':row.CREATED_AT, 
                     'UPDATED_BY':row.UPDATED_BY,
                     'File_Token': row.AC_TOKEN}
                rowarray_list.append(t)
            return rowarray_list
        del dbconn                              #destroying Database connection
    except Exception as e:
        return {'error': str(e)}
    
#def getuploadedfiledetailsFn(ctl_key):
#    try:
#        dbconn = conn.getConnection()           #creating Database connection parameter
#        
#        sql = "SELECT * FROM C_SYS_UPLOADED_FILES WHERE CTL_KEY = '"+str(ctl_key)+"'"
#        cursor = conn.query(sql, dbconn)
#        rv = cursor.fetchone()
#        
#        if rv is None:
#            return {'result': 'Unauthenticate access!'}
#        else:
#            with open(rv.FILE_PATH+''+rv.FILE_NAME,'r') as f:
#                    reader = csv.reader(f)
#                    headerlist = next(reader)
#                    csvlist = []
#                    for row in reader:
#                            d = OrderedDict()
#                            for i, x in enumerate(row):
#                                    d[headerlist[i]] = x
#                            csvlist.append(d)
#        
#            output_dump = json.dumps(csvlist)
#            output_res = json.loads(output_dump)
#            
#            #get keys from json object
#            with open(rv.TARGET_FILE_PATH+''+rv.TARGET_FILE_NAME) as json_file:
#                dict_lst = json.load(json_file)
#            
#            df = pd.DataFrame.from_dict(dict_lst)
#            all_keys = list(df.columns)
#            
#                
#            result = {'PKEY_FILE': rv.PKEY_FILE,
#                      'CTL_KEY':rv.CTL_KEY,
#                      'CREATE_DATE': rv.CREATE_DATE,
#                      'CREATED_BY': rv.CREATED_BY,
#                      'FILE_NAME': rv.FILE_NAME,
#                      'FILE_PATH': rv.FILE_PATH,
#                      'TARGET_FILE_NAME': rv.TARGET_FILE_NAME,
#                      'TARGET_FILE_PATH': rv.TARGET_FILE_PATH,
#                      'COLUMN_LIST': all_keys,
#                      'FILE_CONTENT': output_res}
#            return {'result': result}
#        del dbconn                              #destroying Database connection
#    except Exception as e:
#        return {'error': str(e)}
#    
#def uploadFileDetails(file_name,file_path,file_sep,file_quotechar,file_skiprows,file_header,file_encoding,file_nrows,file_quoting,created_by,output_dump,ctl_key,file_sheet_name,file_name_only,file_type,start_pos,create_date,allowed_file_types,allowed_excel_types,csvlist):
#    try:
#        dbconn = conn.getConnection()           #creating Database connection parameter
#        
##        allowed_file_types = ('.csv', '.txt', '.xls', '.xlt', '.xlm', '.xlsx', '.xlsm', '.xltx', '.xltm', '.xlsb', '.xla', '.xlam', '.xll', '.xlw')
##        allowed_excel_types = ('.xls', '.xlt', '.xlm', '.xlsx', '.xlsm', '.xltx', '.xltm', '.xlsb', '.xla', '.xlam', '.xll', '.xlw')
##        
##        create_date = datetime.utcnow()
##        create_date = create_date.strftime('%Y-%m-%d %H:%M:%S.%f')
##        
##        csvlist = []
#            
#        if file_type in allowed_file_types:
#            if file_type in allowed_excel_types:
#
#                xls = pd.ExcelFile(file_path+''+file_name)
#                all_sheet_names = []
#    
#                for i in xls.sheet_names:
#                    all_sheet_names.append(i)
#                    
#                all_sheet_names = json.dumps(list(all_sheet_names))
#                all_sheet_names_json = json.loads(all_sheet_names)
##                print(all_sheet_names)
#                
#                if file_sheet_name == '':
#                    
#                    sql = "SELECT * FROM C_SYS_UPLOADED_FILES where (FILE_NAME = '" + str(file_name) +"' and CREATED_BY= '" + str(created_by) +"') or CTL_KEY= '" + str(ctl_key) +"'"
#                    cursor = conn.query(sql, dbconn)
#                    rv = cursor.fetchone()
#                    
#                    if rv is None:
#                        
#                        sql1 = "INSERT INTO C_SYS_UPLOADED_FILES (CREATE_DATE, CREATED_BY, FILE_NAME, FILE_EXT, FILE_PATH, CTL_KEY, ALL_SHEET_NAMES, CTL_SYS_PROJECTS) VALUES('" + str(create_date) + "','" + str(created_by) + "','" + str(file_name) + "','" + str(file_type) + "','" + str(file_path) + "','" + str(ctl_key) + "','" + str(all_sheet_names) + "')"
#                        cursor = conn.query(sql1, dbconn)
#                        conn.commit(dbconn)
#                        
#                        result = {'file_name':file_name,
#                          'file_path':file_path,
#                          'file_type':file_type,
#                          'created_on':create_date,
#                          'created_by':created_by,
#                          'ctl_key':ctl_key,
#                          'message':'File has been uploaded successfully',
#                          'sheet_names':all_sheet_names_json
#                        }
#                    else:
#                        result = {'file_name':file_name,
#                          'file_path':file_path,
#                          'ctl_key':ctl_key,
#                          'file_type':file_type,
#                          'created_on':create_date,
#                          'created_by':created_by,
#                          'message':'File is already uploaded',
#                          'sheet_names':all_sheet_names_json
#                        }
#                else:
#                    reader = pd.read_excel(
#                            file_path+''+file_name,
#                            skiprows=range(start_pos, file_skiprows),				
#                            header=file_header,               
#                            nrows=file_nrows,
#                            engine='xlrd',
#                            parse_dates=True,
#                            index_col=None,
#                            sheet_name=file_sheet_name
#                            )
#                    headerlist = list(reader.columns)
#                    tuples = [tuple(x) for x in reader.values]
#                    
#                    for row in list(tuples):
#                        d = OrderedDict()
#                        for i, x in enumerate(row):
#                            d[headerlist[i]] = x
#                        csvlist.append(d)
##                    print(csvlist)
#                    output_dump = json.dumps(csvlist, default=default)
#                    output_res = json.loads(output_dump)
#                    
#                    
#                    
#                    target_directory = home_directory+created_by+'\\'
#                    if not os.path.exists(target_directory):
#                        os.makedirs(target_directory)
#            
#                    target_file_name = file_name_only+'_'+re.sub('[^A-Za-z0-9]+', '', file_sheet_name)+'.json'
#                    with open(target_directory+''+target_file_name,'w', encoding='utf-8') as f:
#                        json.dump(csvlist,f,ensure_ascii=False, default=default)
#                        
#                    
#                    sql2 = "UPDATE C_SYS_UPLOADED_FILES SET LAST_UPDATE_DATE= '" + str(create_date) +"', UPDATED_BY= '" + str(created_by) +"', TARGET_FILE_NAME= '" + str(target_file_name) +"', TARGET_FILE_PATH= '" + str(target_directory) +"', ALL_SHEET_NAMES= '" + str(all_sheet_names) +"', CURRENT_SHEET_NAME= '" + str(file_sheet_name) +"', FILE_SKIPROWS= '" + str(file_skiprows) +"', FILE_HEADER= '" + str(file_header) +"', FILE_ENCODING= '" + str(file_encoding) +"', FILE_NROWS= '" + str(file_nrows) +"' WHERE CTL_KEY= '" + str(ctl_key) +"'"
#                    cursor = conn.query(sql2, dbconn)
#                    conn.commit(dbconn)
#
#                    result = {'file_name':file_name,
#                      'file_path':file_path,
#                      'file_type':file_type,
#                      'created_on':create_date,
#                      'created_by':created_by,
#                      'target_file_name':target_file_name,
#                      'target_file_path':target_directory,
#                      'last_update_date':create_date,
#                      'updated_by':created_by,
#                      'sheet_names':all_sheet_names_json,
#                      'current_sheet_name':file_sheet_name,
#                      'file_content':output_res,
#                      'ctl_key':ctl_key,
#                      'file_skiprows':file_skiprows,
#                      'file_header':file_header,
#                      'file_encoding':file_encoding,
#                      'file_nrows':file_nrows,
#                      'message':'File has been updated successfully'
#                    }
#
#            else: 
#                #json conversion  
#                if file_quotechar != '':
#                    reader = pd.read_csv(
#                        file_path+''+file_name,      # relative python path to subdirectory
#                        sep=file_sep, 					# Tab-separated value file.
#                        quotechar=file_quotechar,				# single quote allowed as quote character
#                        skiprows=range(start_pos, file_skiprows),				# Skip the first 10 rows of the file,
#                        header=file_header,               #0  1st row as header
#                        encoding = file_encoding,      #utf8   ascii
#                        nrows=file_nrows,
#                        engine='python'                  
#                   )
#                else:
#                    reader = pd.read_csv(
#                        file_path+''+file_name,      # relative python path to subdirectory
#                        sep=file_sep, 					# Tab-separated value file.
#                        skiprows=range(start_pos, file_skiprows),				# Skip the first 10 rows of the file,
#                        header=file_header,               #0  1st row as header
#                        encoding = file_encoding,      #utf8   ascii
#                        nrows=file_nrows,
#                        engine='python'                      
#                    )
#                
#                headerlist = list(reader.columns)
#                tuples = [tuple(x) for x in reader.values]
#                    
#                csvlist = []
#                for row in tuples:
#                    d = OrderedDict()
#                    for i, x in enumerate(row):
#                        d[headerlist[i]] = x
#                    csvlist.append(d)
#                
#                output_dump = json.dumps(csvlist)
#                output_res = json.loads(output_dump)
#                
#                
#                df=pd.DataFrame(output_res)                
#                x = pd.DataFrame(df.iloc[0])               
#                z = x.transpose()
#                z = z.applymap(str)                
#                y=z.values.tolist()[0]
#                df.columns = y
#                df=df.drop(df.index[0])         
#                pdf = x.replace([r'[_]'], [' '], regex=True)
#                pdf=pdf[0].str.upper()
#                pdf=pd.concat([x,pdf], axis = 1)
#                #print (pdf)
#                pdf.columns = ['SourceName','ParsedName']
#                parsed_dump = pdf.to_json(orient= 'columns')
#                parsedCol = json.loads(parsed_dump)
#                
#                
#                
#                
#                sql3 = "SELECT * FROM C_SYS_UPLOADED_FILES where (FILE_NAME = '" + str(file_name) +"' and CREATED_BY= '" + str(created_by) +"') or CTL_KEY= '" + str(ctl_key) +"'"
#                cursor = conn.query(sql3, dbconn)
#                rv = cursor.fetchone()
#                
#                if rv is not None:
#                    
#                    target_directory = home_directory+created_by+'\\'
#                    if not os.path.exists(target_directory):
#                        os.makedirs(target_directory)
#            
#                    target_file_name = file_name_only+'.json'
#                    with open(target_directory+''+target_file_name,'w', encoding='utf-8') as f:
#                        json.dump(csvlist,f,ensure_ascii=False)
#                        
#                    sql4 = "UPDATE C_SYS_UPLOADED_FILES SET LAST_UPDATE_DATE= '" + str(create_date) +"', UPDATED_BY= '" + str(created_by) +"', TARGET_FILE_NAME= '" + str(target_file_name) +"', TARGET_FILE_PATH= '" + str(target_directory) +"', FILE_SEP= '" + str(file_sep) +"', FILE_QUOTECHAR= '" + str(file_quotechar) +"', FILE_SKIPROWS= '" + str(file_skiprows) +"', FILE_HEADER= '" + str(file_header) +"', FILE_ENCODING= '" + str(file_encoding) +"', FILE_NROWS= '" + str(file_nrows) +"', FILE_QUOTING= '" + str(file_quoting) +"' WHERE CTL_KEY= '" + str(ctl_key) +"'"
#                    cursor = conn.query(sql4, dbconn)
#                    conn.commit(dbconn)
#
#                    result = {'file_name':file_name,
#                      'file_path':file_path,
#                      'file_type':file_type,
#                      'created_on':create_date,
#                      'created_by':created_by,
#                      'target_file_name':target_file_name,
#                      'target_file_path':target_directory,
#                      'last_update_date':create_date,
#                      'updated_by':created_by,
#                      'file_columns':parsedCol,
#                      'file_content':output_res,
#                      'ctl_key':ctl_key,
#                      'file_sep':file_sep,
#                      'file_quotechar':file_quotechar,
#                      'file_skiprows':file_skiprows,
#                      'file_header':file_header,
#                      'file_encoding':file_encoding,
#                      'file_nrows':file_nrows,
#                      'file_quoting':file_quoting,
#                      'message':'File has been updated successfully'
#                    }
#                else:
#                    sql4 = "INSERT INTO C_SYS_UPLOADED_FILES (CREATE_DATE, CREATED_BY, FILE_NAME, FILE_EXT, FILE_PATH, CTL_KEY) VALUES('" + str(create_date) + "','" + str(created_by) + "','" + str(file_name) + "','" + str(file_type) + "','" + str(file_path) + "','" + str(ctl_key) + "')"
#                    cursor = conn.query(sql4, dbconn)
#                    conn.commit(dbconn)
#                    
#                    result = {'file_name':file_name,
#                      'file_path':file_path,
#                      'file_type':file_type,
#                      'created_on':create_date,
#                      'created_by':created_by,
#                      'message':'File has been uploaded successfully',
#                      'file_content':output_res
#                    }
#        else:
#            result = "Invalid file format. Please try again with a valid file!"
#        return result
#        del dbconn                              #destroying Database connection
#    except Exception as e:
#        return {'error': str(e)}
#    
##def delProjectFn(ctl_sys_projects):
##    try:
##        dbconn = conn.getConnection()           #creating Database connection parameter
##        sql = "SELECT * FROM C_SYS_PROJECTS where CTL_SYS_PROJECTS = '" + str(ctl_sys_projects) +"'"
##        cursor = conn.query(sql, dbconn)
##        rv = cursor.fetchone()
##        
##        if rv is not None:
##            sql1 = "DELETE FROM C_SYS_PROJECTS WHERE CTL_SYS_PROJECTS = '" + str(ctl_sys_projects) +"'"
##            cursor = conn.query(sql1, dbconn)
##            conn.commit(dbconn)
##            result = {'message':'The project has been deleted successfully!'}
##        else:
##            result = {'message':'This project is not present!'}
##        return result
##        del dbconn                              #destroying Database connection
##    except Exception as e:
##        return {'error': str(e)}