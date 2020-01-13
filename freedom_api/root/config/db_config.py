from flask import Blueprint
import pyodbc
import root.conf as conf



mod = Blueprint ('config',__name__)

class SQLDatabase(object):
    dbconn = None
    cursor = None

    def __init__(self):
#        initializing parameter values  
#        self.Driver = '{SQL Server}'
#        self.Server = 'wizcondapsql.centralindia.cloudapp.azure.com'
#        self.Database = 'Wizcon_Freedom'
#        self.UID = 'wizdev1'
#        self.PWD = 'Password@123'
#        self.Trusted_Connection = 'True'
#        self.MARS_Connection = 'yes'
        self.Driver = conf.Driver
        self.Server = conf.Server
        self.Database = conf.Database
        self.UID = conf.UID
        self.PWD = conf.PWD
    
    def getConnection(self):
#        creating cursor object from the connection string        
#        self.connectionstring = f'Driver='+self.Driver+';Server='+self.Server+';Database='+self.Database+';UID='+self.UID+';PWD='+self.PWD+';Trusted_Connection='+self.Trusted_Connection+';MARS_Connection='+self.MARS_Connection
        self.connectionstring = f'Driver='+self.Driver+';Server='+self.Server+';Database='+self.Database+';UID='+self.UID+';PWD='+self.PWD
        self.dbconn = pyodbc.connect(self.connectionstring)
        self.cursor = self.dbconn.cursor()
        return self.cursor
    
    def query(self, query, dbconn):
#        executing cursor object
        return dbconn.execute(query)

    def commit(self, dbconn):
#        committing cursor object
        return dbconn.commit()

    def __del__(self):
#        closing cursor object
        self.dbconn.close()