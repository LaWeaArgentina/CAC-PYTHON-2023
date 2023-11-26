# app/models.py

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cliente(db.Model):
    idCliente = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
    direccion = db.Column(db.String(255))
    telefono = db.Column(db.String(20))
    email = db.Column(db.String(255))
    presupuestos = db.relationship('Presupuesto', backref='cliente', lazy=True)

class Presupuesto(db.Model):
    idPresupuesto = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
    fecha = db.Column(db.Date, default=datetime.utcnow)
    total = db.Column(db.DECIMAL)
    idCliente = db.Column(db.Integer, db.ForeignKey('cliente.idCliente'), nullable=False)
    proyectos = db.relationship('Proyecto', backref='presupuesto', lazy=True)
    items = db.relationship('Item', backref='presupuesto', lazy=True)

class Proyecto(db.Model):
    idProyecto = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
    descripcion = db.Column(db.Text)
    fechaInicio = db.Column(db.Date)
    fechaFin = db.Column(db.Date)
    idPresupuesto = db.Column(db.Integer, db.ForeignKey('presupuesto.idPresupuesto'), nullable=False)
    actores = db.relationship('Actores', backref='proyecto', lazy=True)
    vestuaristas = db.relationship('Vestuaristas', backref='proyecto', lazy=True)
    directores = db.relationship('Directores', backref='proyecto', lazy=True)
    locaciones = db.relationship('Locaciones', backref='proyecto', lazy=True)
    maquilladores = db.relationship('Maquilladores', backref='proyecto', lazy=True)
    utileria = db.relationship('Utileria', backref='proyecto', lazy=True)
    camaras = db.relationship('Camaras', backref='proyecto', lazy=True)
    camarografos = db.relationship('Camarografos', backref='proyecto', lazy=True)
    ambientadores = db.relationship('Ambientadores', backref='proyecto', lazy=True)
    sonido = db.relationship('Sonido', backref='proyecto', lazy=True)
    iluminacion = db.relationship('Iluminacion', backref='proyecto', lazy=True)
    preproduccion = db.relationship('Preproduccion', backref='proyecto', lazy=True)
    edicion = db.relationship('Edicion', backref='proyecto', lazy=True)
    postproduccion = db.relationship('Postproduccion', backref='proyecto', lazy=True)
    transporte = db.relationship('Transporte', backref='proyecto', lazy=True)
    viaticos = db.relationship('Viaticos', backref='proyecto', lazy=True)

class Item(db.Model):
    idItem = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
    costo = db.Column(db.DECIMAL)
    idPresupuesto = db.Column(db.Integer, db.ForeignKey('presupuesto.idPresupuesto'), nullable=False)

class Actores(db.Model):
    idActor = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
    edad = db.Column(db.Integer)
    sexo = db.Column(db.String(10))
    salario = db.Column(db.DECIMAL)
    idProyecto = db.Column(db.Integer, db.ForeignKey('proyecto.idProyecto'), nullable=False)

class Vestuaristas(db.Model):
    idVestuarista = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
    especialidad = db.Column(db.String(255))
    salario = db.Column(db.DECIMAL)
    idProyecto = db.Column(db.Integer, db.ForeignKey('proyecto.idProyecto'), nullable=False)

class Directores(db.Model):
    idDirector = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
    experiencia = db.Column(db.Integer)
    salario = db.Column(db.DECIMAL)
    idProyecto = db.Column(db.Integer, db.ForeignKey('proyecto.idProyecto'), nullable=False)

class Locaciones(db.Model):
    idLocacion = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
    direccion = db.Column(db.String(255))
    costoAlquiler = db.Column(db.DECIMAL)
    idProyecto = db.Column(db.Integer, db.ForeignKey('proyecto.idProyecto'), nullable=False)

class Maquilladores(db.Model):
    idMaquillador = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
    especialidad = db.Column(db.String(255))
    salario = db.Column(db.DECIMAL)
    idProyecto = db.Column(db.Integer, db.ForeignKey('proyecto.idProyecto'), nullable=False)

class Utileria(db.Model):
    idUtileria = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
    descripcion = db.Column(db.Text)
    costo = db.Column(db.DECIMAL)
    idProyecto = db.Column(db.Integer, db.ForeignKey('proyecto.idProyecto'), nullable=False)

class Camaras(db.Model):
    idCamara = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.String(255))
    costo = db.Column(db.DECIMAL)
    idProyecto = db.Column(db.Integer, db.ForeignKey('proyecto.idProyecto'), nullable=False)

class Camarografos(db.Model):
    idCamarografo = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
    experiencia = db.Column(db.Integer)
    salario = db.Column(db.DECIMAL)
    idProyecto = db.Column(db.Integer, db.ForeignKey('proyecto.idProyecto'), nullable=False)

class Ambientadores(db.Model):
    idAmbientador = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
    descripcion = db.Column(db.Text)
    costo = db.Column(db.DECIMAL)
    idProyecto = db.Column(db.Integer, db.ForeignKey('proyecto.idProyecto'), nullable=False)

class Sonido(db.Model):
    idSonido = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
    descripcion = db.Column(db.Text)
    costo = db.Column(db.DECIMAL)
    idProyecto = db.Column(db.Integer, db.ForeignKey('proyecto.idProyecto'), nullable=False)

class Iluminacion(db.Model):
    idIluminacion = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
    descripcion = db.Column(db.Text)
    costo = db.Column(db.DECIMAL)
    idProyecto = db.Column(db.Integer, db.ForeignKey('proyecto.idProyecto'), nullable=False)

class Preproduccion(db.Model):
    idPreproduccion = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
    descripcion = db.Column(db.Text)
    costo = db.Column(db.DECIMAL)
    idProyecto = db.Column(db.Integer, db.ForeignKey('proyecto.idProyecto'), nullable=False)

class Edicion(db.Model):
    idEdicion = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
    descripcion = db.Column(db.Text)
    costo = db.Column(db.DECIMAL)
    idProyecto = db.Column(db.Integer, db.ForeignKey('proyecto.idProyecto'), nullable=False)

class Postproduccion(db.Model):
    idPostproduccion = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
    descripcion = db.Column(db.Text)
    costo = db.Column(db.DECIMAL)
    idProyecto = db.Column(db.Integer, db.ForeignKey('proyecto.idProyecto'), nullable=False)

class Transporte(db.Model):
    idTransporte = db.Column(db.Integer, primary_key=True)
    vehiculo = db.Column(db.String(255))
    costo = db.Column(db.DECIMAL)
    idProyecto = db.Column(db.Integer, db.ForeignKey('proyecto.idProyecto'), nullable=False)

class Viaticos(db.Model):
    idViatico = db.Column(db.Integer, primary_key=True)
    destino = db.Column(db.String(255))
    costo = db.Column(db.DECIMAL)
    idProyecto = db.Column(db.Integer, db.ForeignKey('proyecto.idProyecto'), nullable=False)