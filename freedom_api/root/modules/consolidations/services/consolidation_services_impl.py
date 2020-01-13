import string

from flask import Blueprint
from root.modules.consolidations.dao.consolidation_dao_impl import getFileDetails, getFileList, getProjectDetails, saveConsolidation
import os
from flask import Flask, render_template, url_for, json
import re
import pandas as pd
from flask import request, jsonify
import numpy as np


mod = Blueprint ('consolidations',__name__)


@mod.route('/getConsolidationFile', methods=['GET', 'POST'])
def consolidationList():
  try:
    if request.method == "POST":
        srcGen_ac_token = request.get_json()['srcGen_ac_token']
        user_id = request.get_json()['user_id']

        if user_id == '' and srcGen_ac_token == '':
          return jsonify({'message': 'Mandatory field validation failed!'})
        else:
          getData = getFileDetails(srcGen_ac_token, user_id)
          #fileName =  getData['FILE_PATH'] + getData['FILE_NAME']

          json_url = os.path.join(os.path.abspath(getData['FILE_PATH']), "", getData['FILE_NAME'])
          data = json.load(open(json_url))
          return jsonify({'FILE_CONTENT':data,'FILE_NAME':getData['FILE_NAME'],'FILE_ID':getData['FILE_ID']})

  except Exception as e:
    return jsonify({'error': str(e)})


@mod.route('/fileList', methods=['GET', 'POST'])
def fileList():
  try:
    if request.method == "POST":
        project_ac_token = request.get_json()['project_ac_token']
        user_id = request.get_json()['user_id']
        project_details = getProjectDetails(project_ac_token, user_id)
        project_id = project_details.PKEY_PROJECTS
        if project_id !='' and user_id !='' :
          projectFileList = getFileList(project_id, user_id)
          return jsonify(projectFileList)
 
  except Exception as e:
    return jsonify({'error': str(e)})


@mod.route('/addMoreFiles', methods=['GET', 'POST'])
def addMoreFiles():
    try:
        if request.method == "POST":
            project_ac_token = request.get_json()['project_ac_token']
            user_id = request.get_json()['user_id']
            files = request.get_json()['files']
            #print(files)
            
            con_attribute = list()
            rowarray_list = []
            resultarray_list = []
            for value in files:
              getData = getFileDetails(value, user_id)
              json_url = os.path.join(os.path.abspath(getData['FILE_PATH']), "", getData['FILE_NAME'])
              foo = open(json_url)
              data = json.load(foo)
              foo.close()
              #dataKeys = list()
    
              for i in data[0].keys():
                #dataKeys.append(i) 
                if i in con_attribute:
                    y = "test"
                else:
                    con_attribute.append(i)
              #print(dataKeys)
              #t = {'FILE_AC_TOKEN':value,'KEYS':dataKeys,'NO_KEYS':len(dataKeys),'FILE_NAME':getData['FILE_NAME']}
              #rowarray_list.append(t)
              
            #t= {'CON_ATTR':con_attribute,'NO_CON_ATTR':len(con_attribute), 'DATA':rowarray_list}  
            #resultarray_list.append(t)
            
            
            for value in files:
              getData = getFileDetails(value, user_id)
              json_url = os.path.join(os.path.abspath(getData['FILE_PATH']), "", getData['FILE_NAME'])
              foo = open(json_url)
              data = json.load(foo)
              foo.close()
              dataKeys = list()
              data_list = list()
    
              for i in data[0].keys():
                dataKeys.append(i) 
                
              for conval in con_attribute:
                  if conval in dataKeys:
                      data_list.append(conval) 
                  else:
                      data_list.append("") 
              #print(dataKeys)
              t = {'FILE_AC_TOKEN':value,'KEYS':data_list,'NO_KEYS':len(data_list),'FILE_NAME':getData['FILE_NAME']}
              rowarray_list.append(t)
              
            t= {'CON_ATTR':con_attribute,'NO_CON_ATTR':len(con_attribute), 'DATA':rowarray_list}  
            resultarray_list.append(t)
    
            return jsonify(resultarray_list)
        
    except Exception as e:
        return jsonify({'error': str(e)})


@mod.route('/viewPreview', methods=['GET', 'POST'])
def viewPreview():
    try:
        if request.method == "POST":
            project_ac_token = request.get_json()['project_ac_token']
            user_id = request.get_json()['user_id']
            actual_file = request.get_json()['actual_file']
            files = request.get_json()['files']
            #con_attributes = request.get_json()['con_attributes']
            
            
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
    #                tuple_common_col = tuple(common_col)
                        
                    ###   Merge Both array
                    A = pd.DataFrame(file1)
                    B = pd.DataFrame(file2)
                    
    #                frames = [A, B]
    #                merge_data = pd.concat(frames,str(common_col))
                    print(common_col)
                    merge_data = pd.DataFrame.merge(A, B, how='inner', on=common_col)                
                    column1 = common_col
                    print(merge_data)
                    result_data = pd.DataFrame.to_json(merge_data, orient='records',lines=False)
                    file1 = result_data
                    
                    
    
            return result_data
    
    except Exception as e:
        return jsonify({'error': str(e)})



@mod.route('/savePreview', methods=['GET', 'POST'])
def savePreview():
    try:
        if request.method == "POST":
            project_ac_token = request.get_json()['project_ac_token']
            user_id = request.get_json()['user_id']
            actual_file = request.get_json()['actual_file']
            files = request.get_json()['files']
            con_file_name = request.get_json()['con_file_name']  
            result_data = saveConsolidation(project_ac_token,user_id,actual_file,files,con_file_name)
            
            return result_data
        
    except Exception as e:
        return jsonify({'error': str(e)})




