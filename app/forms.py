from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=3, max=64)])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=3, max=64)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    submit = SubmitField("Create Account")

class PostForm(FlaskForm):
    body = TextAreaField("What's happening?", validators=[DataRequired(), Length(max=280)])
    submit = SubmitField("Post")

class EditPostForm(FlaskForm):
    body = TextAreaField("Edit content", validators=[DataRequired(), Length(max=280)])
    submit = SubmitField("Update")

# Baru: untuk proteksi CSRF pada aksi delete
class DeleteForm(FlaskForm):
    submit = SubmitField("Delete")
