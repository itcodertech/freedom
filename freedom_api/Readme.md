# Freedom-Rest-Blueprint-Services

## Structure

 - root/
 -- config/
 ---------- db_config.py
 -- modules/
 ---------- modules_folders
 -------------------- dao/
 -------------------- services/
 - run.py


#### Definitions:

  - db_config.py - Database connection object file
  - dao/ - where DB query execution after validation
  - services/ - where mandatory validation takes place

#### Instructions:

  - For each and every modules, there should be separate folders
  - In each module, there should be two folder and under each folder create a blank _ _init__.py file
  --     dao/
  ------ [modulename]_dao_impl.py
  ------     __init__.py
  -- services/
  ------     [modulename]_services_impl.py
  ------     __init__.py


After creating a new module:
  - open the "root/_ _init__.py" file 
  - add the below scripts (replace [module_name] with the actual module name)
```sh
from root.modules.[module_name].services.[module_name]_services_impl import mod
```
```sh
app.register_blueprint(modules.[module_name].services.[module_name]_services_impl.mod, url_prefix = '/[module_name]')
```

**Once done, run the "run.py" file under root directory !**