from flask import Blueprint
from root.modules.sources.dao.sources_dao_impl import getFilesByProject, uploadFile, previewSource,gen_sys_preview,editColumnNames,genRawPreview,initiateSysPreview
#from root.modules.projects.dao.new_project_dao import newprojectfn

from root.config.db_config import SQLDatabase   #importing Database class
conn = SQLDatabase()

#from datetime import datetime
#from datetime import timezone
#from datetime import timedelta
#import re
#import csv

#import json
#from detect_delimiter import detect
#import pandas as pd


#import magic
#import urllib.request
import os
from flask import Flask, flash, request, redirect, render_template, jsonify
from werkzeug.utils import secure_filename



#import re
#from flask import request, jsonify


mod = Blueprint ('sources',__name__)



UPLOAD_FOLDER = "C:\\workings\\Python\\testFolder\\"


@mod.route('/fileupload', methods=['GET', 'POST'])
def upload_file():
    try:
    	if request.method == 'POST':
            ac_token = request.headers.get('ac_token')
            user_id = request.headers.get('user_id')
            file = request.files['file']
#            return jsonify({request.file['file']})
            
            # check if the post request has the file part
            if 'file' not in request.files:
                return jsonify({'message':'No file part'})
#            
            if file.filename == '':
                return jsonify({'message':'No file selected for uploading'})
            
            else:
                file_name = secure_filename(file.filename)
                file_path = os.path.join(UPLOAD_FOLDER, file_name)
                file.save(file_path)

                return jsonify(uploadFile(ac_token,file_name,file_path,user_id))
        
            
    except Exception as e:
        return jsonify({'error': str(e)})
    
@mod.route('/genarate-pre-source', methods=['GET','POST'])
def gen_prev_source():
    try:
        if request.method == "POST":
            user_id =  request.get_json()['user_id']
            file_name = request.get_json()['file_name']
            file_path = request.get_json()['file_path']       
            return jsonify(genRawPreview(file_path,file_name,user_id))
    
    except Exception as e:
        return jsonify({'error': str(e)})
    
@mod.route('/preview-source', methods=['GET', 'POST'])
def previw_source():
    try:
        if request.method == "POST":
            user_id =  request.get_json()['user_id']
            file_name = request.get_json()['file_name']
            file_path = request.get_json()['file_path']       
            ac_token = request.get_json()['ac_token']

        return jsonify(previewSource(user_id,file_name,file_path,ac_token))               
         
            
            
    except Exception as e:
        return jsonify({'error': str(e)})
    
@mod.route('/init-sys-source', methods=['GET', 'POST'])
def initiate_sysgen_source():
    try:
        if request.method == "POST":
            user_id =  request.get_json()['user_id']
            file_name = request.get_json()['file_name']
            ac_token = request.get_json()['ac_token']
            
            
            return jsonify(initiateSysPreview(user_id,file_name,ac_token))
            
            
            
    except Exception as e:
        return jsonify({'error': str(e)})
    
    
    
@mod.route('/preview-sys-source', methods=['GET', 'POST'])
def preview_sysgen_source():
    try:
        if request.method == "POST":
            user_id =  request.get_json()['user_id']
            file_name = request.get_json()['file_name']
            ac_token = request.get_json()['ac_token']
            
            
            return jsonify(gen_sys_preview(user_id,file_name,ac_token))
            
            
            
    except Exception as e:
        return jsonify({'error': str(e)})
    
    
@mod.route('/edit-columns', methods=['GET','POST'])
def edit_cols():
    try:
        if request.method == "POST":
            user_id = request.get_json()['user_id']
            file_name = request.get_json()['file_name']
            old_col_val = request.get_json()['old_col_val']
            new_col_val = request.get_json()['new_col_val']
            
            if old_col_val == '' and new_col_val == '':
                return jsonify({'error': 'columns name needed'})
            else:
                return jsonify(editColumnNames(user_id,file_name,old_col_val,new_col_val))
    except Exception as e:
        return jsonify({'error':str(e)})



@mod.route('/files-by-project', methods=['GET', 'POST'])
def getfiles_by_project():
    try:
        if request.method == "POST":
            ac_token = request.get_json()['ac_token']
        #    created_by = '969823826'
            
            if ac_token == '':
                return jsonify({'message': 'Mandatory field validation failed'})
            else:
                return jsonify(getFilesByProject(ac_token))
    except Exception as e:
        return jsonify({'error': str(e)})
    
#@mod.route('/getuploadedfiledetails', methods=['GET', 'POST'])
#def getuploadedfiledetails():
#    try:
#        if request.method == "POST":
#            ctl_key = request.get_json()['ctl_key']
#            if ctl_key == '':
#                return jsonify({'message': 'Mandatory field validation failed!'})
#            else:
#                return jsonify(getuploadedfiledetailsFn(ctl_key))
#    except Exception as e:
#        return jsonify({'error': str(e)})
#    
#    
#@mod.route('/file-details2', methods=['GET', 'POST'])
#def fileDetails2():
#    try:
#        if request.method == "POST":
#            file_name = request.get_json()['file_name']
#            file_path = request.get_json()['file_path']
#            file_sep = request.get_json()['file_sep']
#            if file_sep != '':
#                file_sep = re.escape(file_sep)
#            else:
#                file_sep = ','
#            
#            file_quotechar = request.get_json()['file_quotechar']
#                
#            file_skiprows = request.get_json()['file_skiprows']
#            if file_skiprows != '':
#                file_skiprows = int(file_skiprows)
#            else:
#                file_skiprows = 0
#            
#            file_header = request.get_json()['file_header']
#            if file_header != '':
#                file_header = int(file_header)
#                start_pos = file_header+1
#            else:
#                file_header = None
#                start_pos = 0
#                
#            file_encoding = request.get_json()['file_encoding']
#            
#            file_nrows = request.get_json()['file_nrows']
#            if file_nrows != '':
#                file_nrows = int(file_nrows)
#            else:
#                file_nrows = None
#                
#            file_quoting = request.get_json()['file_quoting']
#            
#            if file_quoting == '1':
#                file_quoting = csv.QUOTE_ALL
#            elif file_quoting == '3':
#                file_quoting = csv.QUOTE_NONE
#            else:
#                file_quoting = csv.QUOTE_MINIMAL
#            
#            created_by = request.get_json()['created_by']
#                    
#            create_date = datetime.utcnow()
#            create_date = create_date.strftime('%Y-%m-%d %H:%M:%S.%f')
#        
#
#            output_dump = ''
#            
#            ctl_key = created_by+re.sub('[^A-Za-z0-9]+', '', file_name)
#            
#            file_sheet_name  = request.get_json()['file_sheet_name']
#            
#            file_name_only = os.path.splitext(file_name)[0]
#            file_type = os.path.splitext(file_name)[1]
#            
#            allowed_file_types = ('.csv', '.txt', '.xls', '.xlt', '.xlm', '.xlsx', '.xlsm', '.xltx', '.xltm', '.xlsb', '.xla', '.xlam', '.xll', '.xlw')
#            allowed_excel_types = ('.xls', '.xlt', '.xlm', '.xlsx', '.xlsm', '.xltx', '.xltm', '.xlsb', '.xla', '.xlam', '.xll', '.xlw')
#            
#            csvlist = []
#            
#            if file_name == '' or file_path == '' or ctl_key == '':
#                return jsonify({'message': 'Mandatory field validation failed!'})
#            else:
#                return jsonify(uploadFileDetails(file_name,file_path,file_sep,file_quotechar,file_skiprows,file_header,file_encoding,file_nrows,file_quoting,created_by,output_dump,ctl_key,file_sheet_name,file_name_only,file_type,start_pos,create_date,allowed_file_types,allowed_excel_types,csvlist))
#    except Exception as e:
#        return jsonify({'error': str(e)})
    
#@mod.route('/del-project', methods=['GET', 'POST'])
#def delProject():
#    try:
#        if request.method == "POST":
#            ctl_sys_projects = request.get_json()['ctl_sys_projects']
#            
#            if ctl_sys_projects == '':
#                return jsonify({'message': 'Mandatory field validation failed!'})
#            else:
#                return jsonify(delProjectFn(ctl_sys_projects))
#    except Exception as e:
#        return jsonify({'error': str(e)})