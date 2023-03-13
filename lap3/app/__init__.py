
from flask import  Flask
from flask_migrate import Migrate
from  app.models import  db
from app.config import  projectConfig as AppConfig
from app.models import Posts,Category

from app.posts.api.api_views import AllPosts,PostGetSpecificAndUpdateAndDelete
from flask_restful import Api

def create_app(config_name):
    app = Flask(__name__)
    current_config = AppConfig[config_name]
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config
    app.config.from_object(current_config)
    db.init_app(app)
    ## add migration
    migrate = Migrate(app, db, render_as_batch=True)
    from app.category import category_blueprint
    from app.posts import posts_blueprint
    app.register_blueprint(category_blueprint)
    app.register_blueprint(posts_blueprint)

    api = Api(app)
    api.add_resource(AllPosts, '/api/posts')
    api.add_resource(PostGetSpecificAndUpdateAndDelete, '/api/posts/<int:id>')
    return  app