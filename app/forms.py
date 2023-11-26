# app/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class SolicitudPresupuestoForm(FlaskForm):
    nombre = StringField('Nombre')
    email = StringField('Email')
    mensaje = StringField('Mensaje')
    submit = SubmitField('Enviar')