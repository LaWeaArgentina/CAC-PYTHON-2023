#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from database import create_database_connection, handle_sighup
import os
import signal

# Importa el módulo database y usar el alias db
import database as db

directorio = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
directorio = os.path.join(directorio, 'src', 'templates')

app = Flask(__name__, template_folder=directorio)
app.secret_key = 'tu_clave_secreta'  # Asegúrate de establecer tu propia clave secreta
login_manager = LoginManager(app)

app.config['LOGIN_MANAGER'] = login_manager
login_manager.login_view = 'login'

class User(UserMixin):
    pass

@login_manager.user_loader
def load_user(user_id):
    cursor = db.database.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user_data = cursor.fetchone()
    cursor.close()
    
    if user_data:
        user = User()
        user.id = user_data['id']
        return user


@app.route('/')
def home():

    return render_template('index.html')

@app.route('/inicio')
def inicio():

    return render_template('index.html')

@app.route('/nosotros')
def nosotros():
        
    return render_template('nosotros.html')

@app.route('/clientes')
def clientes():
        
    return render_template('clientes.html')

@app.route('/producto')
def producto():
        
    return render_template('producto.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/contacto_save', methods=['POST'])
def contactoSave():
    try:
        nombre = request.form['nombre']
        email = request.form['email']
        mensaje = request.form['mensaje']

        # Validar datos del formulario
        if not (nombre and email and mensaje):
            flash('Completa todos los campos del formulario', 'error')
            return redirect(url_for('contacto'))

        # Insertar en la base de datos
        cursor = db.database.cursor()
        sql = "INSERT INTO contactos (nombre, email, mensaje) VALUES (%s, %s, %s)"
        data = (nombre, email, mensaje)
        cursor.execute(sql, data)
        db.database.commit()

        flash('Mensaje enviado correctamente', 'success')
    except Exception as e:
        flash(f'Error al enviar el mensaje: {e}', 'error')
    finally:
        cursor.close()

    return redirect(url_for('inicio'))

@app.route('/contactos')
@login_required
def contactos():
    try:
        cursor = db.database.cursor()
        cursor.execute("SELECT * FROM contactos")
        resultado = cursor.fetchall()
        insertObj = [dict(zip([column[0] for column in cursor.description], record)) for record in resultado]
        cursor.close()
        return render_template('contactos.html', data=insertObj)
    except Exception as e:
        flash(f'Error fetching contact entries: {e}', 'error')
        return redirect(url_for('inicio'))

@app.route('/contacto_edit', methods=['POST'])
def contactoEdit():
    try:
        respondido = request.form['respondido']
        id = request.form['id']

        if respondido and id:
            cursor = db.database.cursor()
            sql = "UPDATE contactos SET respondido = %s WHERE id = %s"
            data = (respondido, id)
            cursor.execute(sql, data)
            db.database.commit()
        else:
            flash('Invalid data for updating contact entry', 'error')

        return redirect(url_for('contactos'))
    except Exception as e:
        flash(f'Error updating contact entry: {e}', 'error')
        return redirect(url_for('contactos'))

@app.route('/contacto_delete', methods=['POST'])
def contactoDelete():
    try:
        id = request.form['id']

        if id:
            cursor = db.database.cursor()
            sql = "DELETE FROM contactos WHERE id = %s"
            data = [id]
            cursor.execute(sql, data)
            db.database.commit()
        else:
            flash('Invalid data for deleting contact entry', 'error')

        return redirect(url_for('contactos'))
    except Exception as e:
        flash(f'Error deleting contact entry: {e}', 'error')
        return redirect(url_for('contactos'))

@app.route('/crear-presupuesto')
def crear_presupuesto():
    return render_template('crear-presupuesto.html')

@app.route('/presupuesto_save', methods=['POST'])
@login_required
def presupuestoSave():
    
    cursor = db.database.cursor()

    # Presupuesto
    nombre_presupuesto = request.form.get('nombre_presupuesto')
    fecha_presupuesto = request.form.get('fecha_presupuesto')
    total_presupuesto = request.form.get('total_presupuesto')
    sql = "INSERT INTO Presupuesto (nombre, fecha, total) VALUES (%s, %s, %s)"
    data = [nombre_presupuesto, fecha_presupuesto, total_presupuesto]
    cursor.execute(sql, data)
    db.database.commit()


    sql='SELECT AUTO_INCREMENT FROM information_schema.TABLES WHERE TABLE_SCHEMA = "presupuestar" AND TABLE_NAME = "Proyecto";'
    cursor.execute(sql)
    resultado = cursor.fetchall()
    insertObj = []
    columnNames = [column[0] for column in cursor.description]
    for record in resultado:
        insertObj.append(dict(zip(columnNames, record)))
    idProyecto = insertObj[0]
    idProyecto = idProyecto['AUTO_INCREMENT']

    # Cliente
    nombre_cliente = request.form.get('nombre_cliente')
    direccion_cliente = request.form.get('direccion_cliente')
    telefono_cliente = request.form.get('telefono_cliente')
    email_cliente = request.form.get('email_cliente')
    sql = "INSERT INTO Cliente (nombre, direccion, telefono, email) VALUES (%s, %s, %s, %s)"
    data = [nombre_cliente, direccion_cliente, telefono_cliente, email_cliente]
    cursor.execute(sql, data)
    # Proyecto
    nombre_proyecto = request.form.get('nombre_proyecto')
    sql = "INSERT INTO Proyecto (nombre) VALUES (%s)"
    data = [nombre_proyecto]
    cursor.execute(sql, data)
    # Item
    nombre_item = request.form.get('nombre_item')
    sql = "INSERT INTO Item (nombre) VALUES (%s)"
    data = [nombre_item]
    cursor.execute(sql, data)
    # Actores
    nombre_actor = request.form.get('nombre_actor')
    edad_actor = request.form.get('edad_actor')
    sexo_actor = request.form.get('sexo_actor')
    salario_actor = request.form.get('salario_actor')
    sql = "INSERT INTO Actores (nombre, edad, sexo, salario, idProyecto) VALUES (%s, %s, %s, %s, %s)"
    data = [nombre_actor, edad_actor, sexo_actor, salario_actor, idProyecto]
    cursor.execute(sql, data)
    # Vestuaristas
    nombre_vestuarista = request.form.get('nombre_vestuarista')
    especialidad_vestuarista = request.form.get('especialidad_vestuarista')
    salario_vestuarista = request.form.get('salario_vestuarista')
    sql = "INSERT INTO Vestuaristas (nombre, especialidad, salario, idProyecto) VALUES (%s, %s, %s, %s)"
    data = [nombre_vestuarista, especialidad_vestuarista, salario_vestuarista, idProyecto]
    cursor.execute(sql, data)
    # Directores
    nombre_director = request.form.get('nombre_director')
    experiencia_director = request.form.get('experiencia_director')
    salario_director = request.form.get('salario_director')
    sql = "INSERT INTO Directores (nombre, experiencia, salario, idProyecto) VALUES (%s, %s, %s, %s)"
    data = [nombre_director, experiencia_director, salario_director, idProyecto]
    cursor.execute(sql, data)
    # Locaciones
    nombre_locacion = request.form.get('nombre_locacion')
    direccion_locacion = request.form.get('direccion_locacion')
    costo_alquiler_locacion = request.form.get('costo_alquiler_locacion')
    sql = "INSERT INTO Locaciones (nombre, direccion, costoAlquiler, idProyecto) VALUES (%s, %s, %s, %s)"
    data = [nombre_locacion, direccion_locacion, costo_alquiler_locacion, idProyecto]
    cursor.execute(sql, data)
    # Maquilladores
    nombre_maquillador = request.form.get('nombre_maquillador')
    especialidad_maquillador = request.form.get('especialidad_maquillador')
    salario_maquillador = request.form.get('salario_maquillador')
    sql = "INSERT INTO Maquilladores (nombre, especialidad, salario, idProyecto) VALUES (%s, %s, %s, %s)"
    data = [nombre_maquillador, especialidad_maquillador, salario_maquillador, idProyecto]
    cursor.execute(sql, data)
    # Utileria
    nombre_utileria = request.form.get('nombre_utileria')
    descripcion_utileria = request.form.get('descripcion_utileria')
    costo_utileria = request.form.get('costo_utileria')
    sql = "INSERT INTO Utileria (nombre, descripcion, costo, idProyecto) VALUES (%s, %s, %s, %s)"
    data = [nombre_utileria, descripcion_utileria, costo_utileria, idProyecto]
    cursor.execute(sql, data)

    db.database.commit()

    return redirect(url_for('inicio'))

@app.route('/registro', methods=['GET', 'POST'])
@login_required
def registro():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor = db.database.cursor()
        sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
        data = (username, password)

        try:
            cursor.execute(sql, data)
            db.database.commit()
            flash('Registro exitoso', 'success')  # Mensaje de éxito
            return redirect('/dashboard')  # Con registro exitoso vuelve a '/dashboard'
        except Exception as e:
            print(f"Error al registrar usuario: {e}")
            db.database.rollback()
            flash('Error en el registro. Inténtalo nuevamente.', 'error')  # Mensaje de error

    # If it's a GET request, simply display the form
    return render_template('registro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Retrieve form data
        username = request.form['username']
        password = request.form['password']

        # Validate data
        if not username or not password:
            return render_template('login.html', error='Debes completar todos los campos.')

        # Check if the user exists
        cursor = db.database.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user_data = cursor.fetchone()
        cursor.close()

        # If the user exists, log them in
        if user_data:
            user = User()
            user.id = user_data['id']
            login_user(user)
            return redirect(url_for('dashboard'))

        # Otherwise, show an error message
        return render_template('login.html', error='El usuario o la contraseña son incorrectos.')

    # If it's a GET request, simply display the form
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('inicio'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/listado-clientes')
@login_required
def listado_clientes():

    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM Cliente")
    resultado = cursor.fetchall()
    insertObj = []
    columnNames = [column[0] for column in cursor.description]
    for record in resultado:
        insertObj.append(dict(zip(columnNames, record)))
    cursor.close
    return render_template('listado-clientes.html', clientes=insertObj)

@app.route('/listado-proyectos')
@login_required
def listado_proyectos():
    try:
        cursor = db.database.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Proyecto")
        proyectos = cursor.fetchall()
        cursor.close()
        print(proyectos)  # Agrega este print para ver los proyectos en la consola

        return render_template('listado-proyectos.html', proyectos=proyectos)
    except Exception as e:
        print(f"Error: {e}")
        return "Error al recuperar los proyectos de la base de datos."

@app.route('/listado-presupuestos')
@login_required
def listado_presupuestos():
    # Obtener datos de la base de datos
    cursor = db.database.cursor(dictionary=True)
    sql = """
    SELECT P.idPresupuesto, Pr.nombre AS nombreProyecto, P.fecha, P.total, C.nombre AS nombreCliente
    FROM Presupuesto P
    INNER JOIN Cliente C ON P.idCliente = C.idCliente
    INNER JOIN Proyecto Pr ON P.idProyecto = Pr.idProyecto
    """
    cursor.execute(sql)
    presupuestos = cursor.fetchall()
    cursor.close()

    # Renderizar la plantilla con los datos obtenidos
    return render_template('listado-presupuestos.html', presupuestos=presupuestos)


if __name__ == '__main__':
    app.run(debug=True, port=4000)