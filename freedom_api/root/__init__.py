from flask import Flask
from flask_cors import CORS

app = Flask (__name__)
app.config['JSON_SORT_KEYS'] = False
CORS(app)


from root.modules.projects.services.project_services_impl import mod
from root.modules.sources.services.sources_services_impl import mod
from root.modules.relationship.services.relationship_services_impl import mod
from root.modules.gold.services.gold_services_impl import mod


app.register_blueprint(modules.projects.services.project_services_impl.mod, url_prefix = '/projects')
app.register_blueprint(modules.sources.services.sources_services_impl.mod, url_prefix = '/sources')
app.register_blueprint(modules.relationship.services.relationship_services_impl.mod, url_prefix = '/relationship')
app.register_blueprint(modules.gold.services.gold_services_impl.mod, url_prefix = '/gold')


from root.modules.users.services.users_services_impl import mod
from root.modules.consolidations.services.consolidation_services_impl import mod
from root.modules.wrangle.services.wrangle_services_impl import mod


app.register_blueprint(modules.users.services.users_services_impl.mod, url_prefix = '/users')
app.register_blueprint(modules.consolidations.services.consolidation_services_impl.mod, url_prefix = '/consolidations')
app.register_blueprint(modules.wrangle.services.wrangle_services_impl.mod, url_prefix = '/wrangle')