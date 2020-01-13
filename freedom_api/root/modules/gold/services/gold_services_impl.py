from flask import Blueprint

from datetime import datetime
from datetime import timezone
from datetime import timedelta
import json
import pandas as pd
import numpy as np

#import re
from flask import request, jsonify
import root.conf as conf


mod = Blueprint ('gold',__name__)




#common methods for gold page
arred = lambda x,n : x*(10**n)//1/(10**n)

def default(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    return super().default(obj)

def object_hook(obj):
    _isoformat = obj.get('_isoformat')
    if _isoformat is not None:
        return datetime.fromisoformat(_isoformat)
    return obj

def is_number(z):
    try:
        int(z)
        x = 'int'
        return x
    except ValueError:
        try:
            float(z)
            y = 'float'
            return y
        except ValueError:
            z = 'string'
            return z

def is_duplicate(arg,col):
    count = 0
    temp = arg.pivot_table(index=[col], aggfunc='size')
    for key, value in temp.items():
        if value > 1:
            count += value
    return (count * 100 / len(arg))      

def is_null(arg,col):
    null_count = arg.col.isnull().sum()
    return (null_count * 100 / len(arg))


def infer_datatype(dataframe):
    result = []
    s = dataframe.shape[0]
    
    for i, j in dataframe.iteritems():
        a = 0
        b = 0
        c = 0
        for value in j:
            t = is_number(value)
            if t == 'int':
                a += 1
            elif t == 'float':
                b += 1
            elif t == 'string':
                c += 1
        ip = 100*a/s
        fp = 100*b/s
        sp = 100*c/s
        
        if ip > fp and ip > sp:
            lp = ip
            tp = 'Integer'
            inconsistent_data = 100 - ip
        elif fp > ip and fp > sp:
            lp = fp
            tp = 'Float'
            inconsistent_data = 100 - fp
        else:
            lp = sp
            tp = 'String'
            inconsistent_data = 100 - sp
            
            
            
        final_data_type = []
        
        if ip > 0:
            ip_temp = {"Integer":format(arred(ip,2))+'%'}
            final_data_type.append(ip_temp)
            
        if fp > 0:
            fp_temp = {"Float":format(arred(fp,2))+'%'}
            final_data_type.append(fp_temp)
            
        if sp > 0:
            sp_temp = {"String":format(arred(sp,2))+'%'}
            final_data_type.append(sp_temp)
        
        temp=0
        
        try:
            openfile=open(conf.domain_dictionary)                          
            domains=json.load(openfile)
        except:
            domains = {"Name" : "Name, First Name, Last Name, First_Name Last_Name middle_name full_name",
                       "Address" : "house_no landmark nearest_landmark street_name street lane Address address1 address2 address3 address_1 address_2 address_3 address_line address_line1 address_line2 address_line3 City Country city_id state_id state_code county county_id county_code country_id country_code",
                       "Social Security Number": "Social Security Number SSN SS Number",
                       "Credit Card" : "Credit Card Number CCNum CC",
                       "Gender" : "gender sex",
                       "Zip" : "postcode postalcode zipcode zip post_code postal_code zip_code",
                       "Email" : "Email EmailAddress emailid email_id email_address",
                       "Phone Number" : "Phone Mobile Number Telephone phone_number mobile_number phone_no mobile_no ph_no mob mob_no",
                       "Date" : "Date DOB Date_of_birth purchase_date last_update_date last_updated purchased_on"}
        
        for domain, word in domains.items():
            if i.lower() in word.lower():
                temp = 1;
                get_domain = domain
                
        if temp == 0:
            temp =0
            get_domain = 'NOT FOUND'
            
              
        incomplete_item = dataframe[i].isnull().sum()
        
        total_non_null_rec = s - sum(dataframe[i].isnull())
        
        dataframe['temp'] = np.where(dataframe[i].astype(str).str.contains('[a-zA-Z]'), 'Latin', 'Non-Latin')
        
        lat_non_lat = dataframe.temp.unique()
        
        del dataframe['temp']
    
        my_dict = dict(enumerate(lat_non_lat))
        
        try:
            max_length = dataframe[i].apply(len).max()
        except:
            max_length = dataframe[i].map(str).apply(len).max()
            
        try:
            min_length = dataframe[i].apply(len).min()
        except:
            min_length = dataframe[i].map(str).apply(len).min()
            
        t = {"column_name": i, "total_records": total_non_null_rec, "data_type": tp, "data_type_parcent": format(arred(lp,2))+'%', "all_data_types": final_data_type, "latin_non_latin": my_dict, "max_len": int(max_length), "min_len": int(min_length), "data_domain": get_domain, "duplicate_item": format(arred(is_duplicate(dataframe,i),2))+'%', "incomplete_data": format(arred(incomplete_item * 100 / len(dataframe),2))+'%', "inconsistent_data": format(arred(inconsistent_data,2))+'%'}
        result.append(t)
    return result


@mod.route('/drilldown', methods=['GET', 'POST'])
def getallprojects():
    try:
        if request.method == "POST":
            created_by = request.get_json()['created_by']
            file_name = request.get_json()['file_name']
            file_path = request.get_json()['file_path']
        #    created_by = '969823826'
            
            if created_by == '':
                return jsonify({'message': 'Mandatory field validation failed'})
            else:
                openfile=open(file_path+file_name)                          
                jsondata=json.load(openfile, strict=False)
                df=pd.DataFrame(jsondata)
                openfile.close()
                
                app_json = infer_datatype(df)
                
                with open(file_path+'gold-'+file_name, 'w') as json_file:
                    json.dump(app_json, json_file)
                
                return jsonify(app_json)
            
    except Exception as e:
        return jsonify({'error': str(e)})