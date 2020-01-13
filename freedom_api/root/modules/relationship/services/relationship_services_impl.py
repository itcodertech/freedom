from flask import Blueprint
from root.modules.relationship.dao.relationship_dao_impl import createrelationshipFn
import json
import pandas as pd

from datetime import datetime
#import pyodbc



#import re
from flask import request, jsonify


mod = Blueprint ('relationship',__name__)


@mod.route('/createrelationship', methods=['GET', 'POST'])
def createrelationship():
    try:
        if request.method == "POST":
            updated_by = request.get_json()['updated_by']
            relation_on = request.get_json()['relation_on']
            join_type = request.get_json()['join_type']
            obj_name = request.get_json()['obj_name']
            cur_date = datetime.utcnow()
            sources = request.get_json()['sources']
            sources = str(sources).replace("'", '"')
            
            if updated_by == '' or sources =='':
                return jsonify({'message': 'Mandatory field validation failed'})
            else:
                return jsonify(createrelationshipFn(updated_by,relation_on,join_type,obj_name,cur_date,sources))
    except Exception as e:
        return jsonify({'error': str(e)})
    
    
#new relationship modules
@mod.route('/getallrelationship', methods=['GET', 'POST'])
def getallRelationship():
    try:
        if request.method == "POST":
            CTL_SYS_PROJECTS = request.get_json()['CTL_SYS_PROJECTS']
        #    created_by = '969823826'
            
            if created_by == '':
                return jsonify({'message': 'Mandatory field validation failed'})
            else:
                return jsonify(getallrelationshipFn(CTL_SYS_PROJECTS))
    except Exception as e:
        return jsonify({'error': str(e)})
    
@mod.route('/create-relationship', methods=['GET', 'POST'])
def create_Relationship():
    try:
        if request.method == "POST":
            created_by = request.get_json()['created_by']
            project_name = request.get_json()['project_name'].strip()
            ingestion = request.get_json()['ingestion'].strip()
            curation = request.get_json()['curation'].strip()
            reports = request.get_json()['reports'].strip()   
            create_date = datetime.utcnow()
            ctl_sys_projects = created_by+re.sub('[^A-Za-z0-9]+', '', str(create_date)).strip()
            
            
            if created_by == '' or project_name == '':
                return jsonify({'message': 'Mandatory field validation failed!'})
            else:
                return jsonify(create_RelationshipFn(created_by,project_name,ingestion,curation,reports,create_date,ctl_sys_projects))
    except Exception as e:
        return jsonify({'error': str(e)})
    
    
@mod.route('/edit-relationship', methods=['GET', 'POST'])
def editRelationship():
    try:
        if request.method == "POST":
            ctl_sys_projects = request.get_json()['ctl_sys_projects']
            last_updated_by = request.get_json()['last_updated_by']
            ingestion = request.get_json()['ingestion'].strip()
            curation = request.get_json()['curation'].strip()
            reports = request.get_json()['reports'].strip()
            last_update_date = datetime.utcnow()
            
            if ctl_sys_projects == '':
                return jsonify({'message': 'Mandatory field validation failed!'})
            else:
                return jsonify(editProjectFn(ctl_sys_projects,last_updated_by,ingestion,curation,reports,last_update_date))
    except Exception as e:
        return jsonify({'error': str(e)})
    
@mod.route('/del-relationship', methods=['GET', 'POST'])
def delRelationship():
    try:
        if request.method == "POST":
            ctl_sys_projects = request.get_json()['ctl_sys_projects']
            
            if ctl_sys_projects == '':
                return jsonify({'message': 'Mandatory field validation failed!'})
            else:
                return jsonify(delProjectFn(ctl_sys_projects))
    except Exception as e:
        return jsonify({'error': str(e)})        
