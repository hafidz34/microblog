from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_user, logout_user, login_required
from . import db
from .models import User, Post
from .forms import LoginForm, RegisterForm, PostForm, EditPostForm
from flask import current_app as app

@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    form = PostForm()
    if form.validate_on_submit():
        p = Post(body=form.body.data, author=current_user)
        db.session.add(p)
        db.session.commit()
        flash("Posted!")
        return redirect(url_for("index"))
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template("index.html", form=form, posts=posts)

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            next_page = request.args.get("next") or url_for("index")
            return redirect(next_page)
        flash("Invalid username or password")
    return render_template("login.html", form=form)

@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = RegisterForm()
    if form.validate_on_submit():
        if User.query.filter_by(username=form.username.data).first():
            flash("Username already taken")
        else:
            user = User(username=form.username.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash("Account created, please login")
            return redirect(url_for("login"))
    return render_template("register.html", form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

@app.route("/delete/<int:post_id>", methods=["POST"])
@login_required
def delete_post(post_id):
    p = Post.query.get_or_404(post_id)
    if p.author != current_user:
        flash("You can only delete your own posts")
        return redirect(url_for("index"))
    db.session.delete(p)
    db.session.commit()
    flash("Deleted")
    return redirect(url_for("index"))

@app.route('/edit/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)

    if post.author != current_user:
        flash("You can't edit this post.", "danger")
        return redirect(url_for('index'))

    form = EditPostForm(obj=post)

    if form.validate_on_submit():
        post.body = form.body.data
        db.session.commit()
        flash("Post has been updated!", "success")
        return redirect(url_for('index'))

    return render_template('edit_post.html', form=form, post=post)
