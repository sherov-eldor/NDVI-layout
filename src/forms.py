from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from src.models.user import User
from werkzeug.security import check_password_hash

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message='Username kiritilmadi!!!')])
    password = PasswordField('Password', validators=[DataRequired(message='Parol kiritilmadi!!!')])
    remember = BooleanField('Meni eslab qol')
    submit = SubmitField('Login')
    
    # def validate_username(self, username):
    #     user = User.query.filter_by(username=username.data).first()
        
    #     if not user:
    #         raise ValidationError('Bunday username mavjud emas!!!')
    
    def validate_password(self, password):
        username = self.data['username']
        user = User.query.filter_by(username=username).first()
        
        if user:
            checked_password = check_password_hash(user.password, password.data)
        
            if not checked_password:
                raise ValidationError('Parol noto`g`ri!!!')