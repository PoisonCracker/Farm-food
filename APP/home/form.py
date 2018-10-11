from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField


class SigninForm(FlaskForm):
    name = StringField(
        label=u'账号',
        render_kw={
            'type': "text",
            'id': "inputEmail",
            'class': "form-control",
            'placeholder': "Name",
        }
    )
    password = PasswordField(
        label=u'密码',
        render_kw={
            'type': "password",
            'id ': "inputPassword",
            'class': "form-control",
            'placeholder': "Password",
        }
    )
    submit = SubmitField(
        label=u'登陆',
        render_kw={
            'class': "btn btn-lg btn-primary btn-block",  # 前端属性
            'type': "submit"
        }
    )
