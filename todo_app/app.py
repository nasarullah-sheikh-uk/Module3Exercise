from flask import Flask

# we need to import this method for rendering templates and is not imported by default
from flask import render_template , redirect

# we need request module to query the application from browser
from flask import request
import os

########################################################################################
#####  The default repo has some functions written in ./data/sessions_items.py
####   Importing functions written under ./data/sessions_items.py
#####
from todo_app.data.trello_items import get_cards, add_card, update_card
from todo_app.data.View import ViewModel
from todo_app.flask_config import Config

#app = Flask(__name__)
#app.config.from_object(Config())

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    @app.route('/')
    def index():
        cards=get_cards()
        item_view_model=ViewModel(cards)
        return render_template('index.html', view_model=item_view_model)

    
    return app
