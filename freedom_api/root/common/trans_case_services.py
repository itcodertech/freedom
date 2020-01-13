import pandas as pd
import json


class CommonActions(object):
    def __init__(self):
        pass
    
    def caseFormatFn(self,ctl_sys_projects,updated_by,column,action,json_path,json_file):
    
        data = pd.read_json(json_path+json_file) 
        
        with open(json_path+json_file) as f:
            previous_content = json.load(f)
        
#        previous_content = data[column]
        
        if action == 'upper':
            data[column] = data.pop(column).str.upper()
        elif action == 'lower':
            data[column] = data.pop(column).str.lower()
        elif action == 'title':
            data[column] = data.pop(column).str.title()
        elif action == 'capitalize':
            data[column] = data.pop(column).str.capitalize()
        elif action == 'swapcase':
            data[column] = data.pop(column).str.swapcase()
        elif action == 'casefold':
            data[column] = data.pop(column).str.casefold()
        else:
            pass
        
        data.to_json(json_path+json_file, orient='records')
        
        with open(json_path+json_file) as f:
            output_res = json.load(f)
        
        result = {'ctl_sys_projects': ctl_sys_projects,
                  'updated_by': updated_by,
                  'column': column,
                  'action': action,
                  'json_path': json_path,
                  'json_file': json_file,
                  'previous_content': previous_content,
                  'present_content': output_res}

        return result
    
    def dateTimeFormatFn(self,ctl_sys_projects,updated_by,column,action,json_path,json_file):
        
        data = pd.read_json(json_path+json_file) 
        
        with open(json_path+json_file) as f:
            previous_content = json.load(f)
        
#        data[column]=pd.to_datetime(data[column].dt.strftime('% B % d, % Y, % r'))
        
        data[column]=pd.to_datetime(data[column]).dt.strftime(action)
        
        data.to_json(json_path+json_file, orient='records')
        
        with open(json_path+json_file) as f:
            output_res = json.load(f)
        
        result = {'ctl_sys_projects': ctl_sys_projects,
                  'updated_by': updated_by,
                  'column': column,
                  'action': action,
                  'json_path': json_path,
                  'json_file': json_file,
                  'previous_content': previous_content,
                  'present_content': output_res}

        return result
    
    
    def roundingOffFn(self,ctl_sys_projects,updated_by,column,action,json_path,json_file):
        
        data = pd.read_json(json_path+json_file) 
        
        with open(json_path+json_file) as f:
            previous_content = json.load(f)
    
        data[column] = data[column].apply(lambda x: round(x, int(action)))
        
        data.to_json(json_path+json_file, orient='records')
        
        with open(json_path+json_file) as f:
            output_res = json.load(f)
        
        result = {'ctl_sys_projects': ctl_sys_projects,
                  'updated_by': updated_by,
                  'column': column,
                  'decimals': action,
                  'json_path': json_path,
                  'json_file': json_file,
                  'previous_content': previous_content,
                  'present_content': output_res}

        return result   

    
    def stripFn(self,ctl_sys_projects,updated_by,column,action,json_path,json_file,char):
        
        data = pd.read_json(json_path+json_file) 
        
        with open(json_path+json_file) as f:
            previous_content = json.load(f)
        
        if action == 'lstrip':
            data[column] = data[column].str.lstrip(char)
        elif action == 'rstrip':
            data[column] = data[column].str.rstrip(char)
        else:
            data[column] = data[column].str.strip(char)
        
        data.to_json(json_path+json_file, orient='records')
        
        with open(json_path+json_file) as f:
            output_res = json.load(f)
        
        result = {'ctl_sys_projects': ctl_sys_projects,
                  'updated_by': updated_by,
                  'column': column,
                  'action': action,
                  'char_to_remove': char,
                  'json_path': json_path,
                  'json_file': json_file,
                  'previous_content': previous_content,
                  'present_content': output_res}

        return result 

    
    def replaceFn(self,ctl_sys_projects,updated_by,column,json_path,json_file,toReplace,replaceVal):
        
        data = pd.read_json(json_path+json_file) 
        
        with open(json_path+json_file) as f:
            previous_content = json.load(f)
        
        data[column] = data[column].replace(toReplace,replaceVal)
        
        data.to_json(json_path+json_file, orient='records')
        
        with open(json_path+json_file) as f:
            output_res = json.load(f)
        
        result = {'ctl_sys_projects': ctl_sys_projects,
                  'updated_by': updated_by,
                  'column': column,
                  'old_value': toReplace,
                  'new_value': replaceVal,
                  'json_path': json_path,
                  'json_file': json_file,
                  'previous_content': previous_content,
                  'present_content': output_res}

        return result 
    

#    def joinFn(self,ctl_sys_projects,updated_by,json_path1,json_file1,json_path2,json_file2,joinHow,joinOn):    
    def joinFn(self,ctl_sys_projects,updated_by,json_path1,json_file1,json_path2,json_file2,joinHow):
        
#        how : {‘left’, ‘right’, ‘outer’, ‘inner’}, default ‘left’
        
        data1 = pd.read_json(json_path1+json_file1) 
        data2 = pd.read_json(json_path2+json_file2) 
        
#        if joinOn == '':
#            joinOn = None
        
#        data = data1.join(data2, how=joinHow, on=joinOn)
        data = data1.join(data2, how=joinHow)
        
        data = data.to_json(orient='records')
        
        data = json.loads(data)
       
        result = {'ctl_sys_projects': ctl_sys_projects,
                  'updated_by': updated_by,
                  'join_type': joinHow,
#                  'join_on': joinOn,
                  'content': data}

        return result
    
        
