from flask import Flask, render_template, request, redirect, url_for
import os
import database as db

directorio = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
directorio = os.path.join(directorio, 'src', 'templates')

app = Flask(__name__, template_folder=directorio)

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

@app.route('/contactos')
def contactos():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM contactos")
    resultado = cursor.fetchall()
    insertObj = []
    columnNames = [column[0] for column in cursor.description]
    for record in resultado:
        insertObj.append(dict(zip(columnNames, record)))
    cursor.close
    return render_template('contactos.html', data=insertObj)

@app.route('/contacto_save', methods=['POST'])
def contactoSave():
    nombre = request.form['nombre']
    email = request.form['email']
    mensaje = request.form['mensaje']
    if nombre and email and mensaje:
        cursor = db.database.cursor()
        sql = "INSERT INTO contactos (nombre, email, mensaje) VALUES (%s, %s, %s)"
        data = (nombre, email, mensaje)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('inicio'))

@app.route('/contacto_edit', methods=['POST'])
def contactoEdit():
    respondido = request.form['respondido']
    id = request.form['id']

    if respondido and id:
        cursor = db.database.cursor()
        sql = "UPDATE contactos SET respondido = %s WHERE id = %s"
        data = (respondido, id)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('contactos'))

@app.route('/contacto_delete', methods=['POST'])
def contactoDelete():
    id = request.form['id']

    if id:
        cursor = db.database.cursor()
        sql = "DELETE FROM contactos WHERE id = %s"
        data = [id]
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('contactos'))


if __name__ == '__main__':
    app.run(debug=True, port=4000)