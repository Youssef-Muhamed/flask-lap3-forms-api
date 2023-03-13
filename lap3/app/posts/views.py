from flask import render_template,redirect,url_for,request
from app.models import Posts, Category
from app.posts import  posts_blueprint

from app.models import  db
from werkzeug.utils import secure_filename
import os
from .forms import PostForm,CategoryForm

@posts_blueprint.route('/')
def posts_index():
    posts = Posts.get_all_posts()
    return render_template('Posts/index.html',posts=posts )


@posts_blueprint.route('/<int:id>')
def singlePost(id):
    post=Posts.query.get_or_404(id)
    return render_template('Posts/show.html',post=post)

@posts_blueprint.route('/<int:id>/delete')
def deletePost(id):
    post=Posts.query.get_or_404(id)
    res = post.delete_object()
    if res:
        return redirect(url_for("posts.posts_index"))


@posts_blueprint.route('/createpost', methods=['POST', 'GET'], endpoint="createpost")
def createPost():
    form = PostForm()
    if request.method == 'GET':
        return render_template("Posts/createpost.html", form=form, category=Category.query.all())
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        image = request.form['image']
        category = request.form['category']
        record = Posts(title=title,body=body,cat_id=category)
        db.session.add(record)
        db.session.commit()
        return redirect(url_for("posts.posts_index"))


@posts_blueprint.route('/editpost/<int:id>/', methods=('GET', 'POST'), endpoint="editpost")
def editPost(id):
    post = Posts.query.get_or_404(id)
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        # image=request.files['image']
        post.title = title
        post.body = body
        # post.image= image
        db.session.add(post)
        db.session.commit()
        return redirect(url_for("posts.posts_index"))
    return render_template('Posts/editpost.html', post=post)
