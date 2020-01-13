from flask import Blueprint
import pandas as pd
import json

mod = Blueprint ('common',__name__)

class CommonActions(object):
    #The capitalize() function returns a string with first letter capitalized and all other characters lowercased. 
    #It doesn't modify the original string.
    def stringCapitalize(obj):
        if obj != None:
            obj = obj.capitalize()
        return obj
    
    
    #The center() method returns a string padded with specified fillchar. It doesn't modify the original string.
    #The center() method takes two arguments:
    #
    #    width - length of the string with padded characters
    #    fillchar (optional) - padding character
    #The fillchar argument is optional. If it's not provided, space is taken as default argument.
    def stringCenter(obj, width, fillchar):
        if obj != None:
            if fillchar != '':
                obj = obj.center(width, fillchar)
            else:
                obj = obj.center(width)
        return obj
    
    
    #The casefold() method is removes all case distinctions present in a string. 
    #It is used for caseless matching, i.e. ignores cases when comparing.
    def stringCasefold(obj):
        if obj != None:
            obj = obj.casefold()
        return obj
    
    
    #count() method searches the substring in the given string and returns how many times the substring is present in it.
    #count() method only requires a single parameter for execution. However, it also has two optional parameters:
    #
    #    substring - string whose count is to be found.
    #    start (Optional) - starting index within the string where search starts.
    #    end (Optional) - ending index within the string where search ends.
    #Note: Index in Python starts from 0, not 1.
    def stringCount(obj, substring, first, last):
        if obj != None:
            if first == '':
                first = None
            if last == '':
                last = None
            obj = obj.count(substring, first, last)
        return obj
    
    
    #The endswith() method returns True if a string ends with the specified suffix. If not, it returns False.
    #The endswith() takes three parameters:
    #
    #    suffix - String or tuple of suffixes to be checked
    #    start (optional) - Beginning position where suffix is to be checked within the string.
    #    end (optional) - Ending position where suffix is to be checked within the string.
    def stringEndswith(obj, substring, first, last):
        if obj != None:
            if first == '':
                first = None
            if last == '':
                last = None
            obj = obj.endswith(substring, first, last)
        return obj
    
    
    #The expandtabs() method returns a copy of string with all tab characters '\t' replaced 
    #with whitespace characters until the next multiple of tabsize parameter.
    #The expandtabs() takes an integer tabsize argument. The default tabsize is 8.
    def stringExpandtabs(obj, arg):
        if obj != None:
            obj = obj.expandtabs(arg)
        return obj
    
    
    #Using string's encode() method, you can convert unicoded strings into any encodings 
    #supported by Python. By default, Python uses utf-8 encoding.
    #encoding - the encoding type a string has to be encoded to
    #errors - response when encoding fails. There are six types of error response
    #    strict - default response which raises a UnicodeDecodeError exception on failure
    #    ignore - ignores the unencodable unicode from the result
    #    replace - replaces the unencodable unicode to a question mark ?
    #    xmlcharrefreplace - inserts XML character reference instead of unencodable unicode
    #    backslashreplace - inserts a \uNNNN espace sequence instead of unencodable unicode
    #    namereplace - inserts a \N{...} escape sequence instead of unencodable unicode
    def stringEncode(obj, enc, err):
        if obj != None:
            obj = obj.encode(encoding=enc,errors=err)
        return obj
    
    
    #The find() method returns the index of first occurrence of the substring (if found). If not found, it returns -1.
    #The find() method takes maximum of three parameters:
    #
    #    sub - It's the substring to be searched in the str string.
    #    start and end (optional) - substring is searched within str[start:end]
    def stringFind(obj, sub, start, end):
        if start == '':
            start = None
        if end == '':
            end = None
        obj = obj.find(sub, start, end)
        return obj
    
    
    #pandas dataframe transformations
    def pdUpper(data, column):
        data[column] = data.pop(column).str.upper()
        return data[column]
    
    
    def pdLower(data, column):
        data[column] = data.pop(column).str.lower()
        return data[column]
    
    
    def pdTitle(data, column):
        data[column] = data.pop(column).str.title()
        return data[column]
    
    
    def pdCapitalize(data, column):
        data[column] = data.pop(column).str.capitalize()
        return data[column]
    
    
    def pdSwapcase(data, column):
        data[column] = data.pop(column).str.swapcase()
        return data[column]
    
    
    def pdCasefold(data, column):
        data[column] = data.pop(column).str.casefold()
        return data[column]
    
    def upperFn(ctl_sys_projects,updated_by,column,action,json_path,json_file):
        
        data = pd.read_json(json_path+json_file) 
        
        previous_content = data[column]
        
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
        
        result = {'previous_content': previous_content,
                      'present_content':data[column]}
        return result
        
#        data.to_json(json_path+json_file, orient='records')
#        with open(json_path+json_file) as f:
#            output_res = json.load(f)
#        return output_res
