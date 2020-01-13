from flask import Blueprint
from root.modules.projects.dao.project_dao_impl import getAllProjects, createProject, editProject, delProject
#from root.modules.projects.dao.new_project_dao import newprojectfn

from datetime import datetime
from datetime import timezone
from datetime import timedelta
import re
#import pyodbc



#import re
from flask import request, jsonify


mod = Blueprint ('projects',__name__)
    
@mod.route('/create-project', methods=['GET', 'POST'])
def create_project():
    try:
        if request.method == "POST":
            user_id = request.get_json()['user_id']
            project_name = request.get_json()['project_name']
            ingestion = request.get_json()['ingestion']
            curation = request.get_json()['curation']
            reports = request.get_json()['reports']   
            created_at = datetime.utcnow()
            proj_desc = request.get_json()['proj_desc']
            
            
            if user_id == '' or project_name == '':
                return jsonify({'error': 'Mandatory field validation failed!'})
            else:
                return jsonify(createProject(user_id,project_name,ingestion,curation,reports,created_at,proj_desc))
    except Exception as e:
        return jsonify({'error': str(e)})
    
    
@mod.route('/getall-projects', methods=['GET', 'POST'])
def getall_projects():
    try:
        if request.method == "POST":
            pkey_user = request.get_json()['pkey_user']
        #    created_by = '969823826'
            
            if pkey_user == '':
                return jsonify({'message': 'Mandatory field validation failed'})
            else:
                return jsonify(getAllProjects(pkey_user))
    except Exception as e:
        return jsonify({'error': str(e)})
    
    
@mod.route('/edit-project', methods=['GET', 'POST'])
def edit_project():
    try:
        if request.method == "POST":
            ac_token = request.get_json()['ac_token']
            updated_by = request.get_json()['updated_by']
            ingestion = request.get_json()['ingestion'].strip()
            curation = request.get_json()['curation'].strip()
            reports = request.get_json()['reports'].strip()
            proj_desc = request.get_json()['proj_desc']
            update_at = datetime.utcnow()
            
            if ac_token == '':
                return jsonify({'message': 'Mandatory field validation failed!'})
            else:
                return jsonify(editProject(ac_token,updated_by,ingestion,curation,reports,update_at,proj_desc))
    except Exception as e:
        return jsonify({'error': str(e)})
    
@mod.route('/del-project', methods=['GET', 'POST'])
def del_project():
    try:
        if request.method == "POST":
            ac_token = request.get_json()['ac_token']
            
            if ac_token == '':
                return jsonify({'message': 'Mandatory field validation failed!'})
            else:
                return jsonify(delProject(ac_token))
    except Exception as e:
        return jsonify({'error': str(e)})