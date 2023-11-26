# app/routes.py

from flask import render_template, url_for, flash, redirect
from app import app, db
from app.forms import SolicitudPresupuestoForm
from app.models import Cliente

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/solicitud_presupuesto', methods=['GET', 'POST'])
def solicitud_presupuesto():
    form = SolicitudPresupuestoForm()
    if form.validate_on_submit():
        cliente = Cliente(nombre=form.nombre.data, email=form.email.data)
        db.session.add(cliente)
        db.session.commit()
        flash('Solicitud de presupuesto enviada con éxito', 'success')
        return redirect(url_for('index'))
    return render_template('solicitud_presupuesto.html', form=form)