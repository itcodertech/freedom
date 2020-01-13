import string

from flask import Blueprint
from root.modules.wrangle.dao.wrangle_dao_impl import getFileDetails, getFileList, getProjectDetails, saveConsolidation
import os
from flask import Flask, render_template, url_for, json
import re
import pandas as pd
from flask import request, jsonify
import numpy as np


mod = Blueprint ('wrangle',__name__)


@mod.route('/getWrangleTransform', methods=['GET', 'POST'])
def wrangleTransform():
  try:
    if request.method == "POST":
        
        project_ac_token = request.get_json()['project_ac_token']
        file_ac_token = request.get_json()['file_ac_token']
        user_id = request.get_json()['user_id']
        #update_date = datetime.utcnow()
        column = request.get_json()['column']
        transform_type = request.get_json()['transform_type']
        
        file_details = getFileDetails(file_ac_token, user_id)
        
        with open(file_details['FILE_PATH'] + file_details['FILE_NAME']) as f:
            output_res = json.load(f)
        
        data = pd.read_json(file_details['FILE_PATH'] + file_details['FILE_NAME'])

 

        if transform_type == 'upper':
            data[column] = data.pop(column).str.upper()
        elif transform_type == 'lower':
            data[column] = data.pop(column).str.lower()
        elif transform_type == 'title':
            data[column] = data.pop(column).str.title()
        elif transform_type == 'capitalize':
            data[column] = data.pop(column).str.capitalize()
        elif transform_type == 'swapcase':
            data[column] = data.pop(column).str.swapcase()
        elif transform_type == 'casefold':
            data[column] = data.pop(column).str.casefold()
        else:
            pass        
        
        result_data = pd.DataFrame.to_json(data, orient='records',lines=False)
       # print(data)        
        return result_data

  except Exception as e:
    return jsonify({'error': str(e)})






