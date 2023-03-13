from flask import render_template,redirect,url_for
from app.models import Category
from app.category import  category_blueprint
@category_blueprint.route('/')
def category_index():
    categories = Category.get_all_category()
    return render_template('category/index.html',categories=categories )

@category_blueprint.route('/<int:id>')
def singleCategory(id):
    category=Category.query.get_or_404(id)

    return render_template('category/show.html',post=category)


@category_blueprint.route('/<int:id>/delete')
def deleteCategory(id):
    category=Category.query.get_or_404(id)
    res = category.delete_object()
    if res:
        return redirect(url_for("category.category_index"))