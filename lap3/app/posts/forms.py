from flask_wtf import FlaskForm
from wtforms import StringField,FileField


class PostForm(FlaskForm):
    title = StringField('Title')
    body = StringField('Body')
    # desc = StringField('desc')
    image = StringField('image')


class CategoryForm(FlaskForm):
    categoryName = StringField('Category Name')