# -*- coding: utf-8 -*-

from flask import Blueprint
from root import app
#from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

mod = Blueprint ('utility',__name__)

class cypherPassword(object):
    bcrypt = None
    cors = None
    
    def bcryptP(self):
        
        app.config['JWT_SECRET_KEY'] = 'secret'
        self.bcrypt = Bcrypt(app)
        self.jwt = JWTManager(app)
        return self.bcrypt
    
#    def corsf(self):
#        self.cors = CORS(app)