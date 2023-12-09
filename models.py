from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Contactos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    mensaje = db.Column(db.Text, nullable=False)
    respondido = db.Column(db.Integer)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

class Cliente(db.Model):
    idCliente = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(255), nullable=False)
    direccion = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(255), nullable=False)

class Presupuesto(db.Model):
    idPresupuesto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fecha = db.Column(db.Date, nullable=False)
    total = db.Column(db.DECIMAL, nullable=False)
    idCliente = db.Column(db.Integer, db.ForeignKey('cliente.idCliente'))
    idProyecto = db.Column(db.Integer, db.ForeignKey('proyecto.idProyecto'))

class Proyecto(db.Model):
    idProyecto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.TEXT)
    fechaInicio = db.Column(db.Date, nullable=False)
    fechaFin = db.Column(db.Date, nullable=False)
    idPresupuesto = db.Column(db.Integer, db.ForeignKey('presupuesto.idPresupuesto'))

class Item(db.Model):
    idItem = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(255), nullable=False)
    costo = db.Column(db.DECIMAL, nullable=False)
    idPresupuesto = db.Column(db.Integer, db.ForeignKey('presupuesto.idPresupuesto'))

class Actores(db.Model):
    idActor = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(255), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    sexo = db.Column(db.String(10), nullable=False)
    salario = db.Column(db.DECIMAL, nullable=False)
    idProyecto = db.Column(db.Integer, db.ForeignKey('proyecto.idProyecto'))

class Vestuaristas(db.Model):
    idVestuarista = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(255), nullable=False)
    especialidad = db.Column(db.String(255), nullable=False)
    salario = db.Column(db.DECIMAL, nullable=False)
    idProyecto = db.Column(db.Integer, db.ForeignKey('proyecto.idProyecto'))

class Directores(db.Model):
    idDirector = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(255), nullable=False)
    experiencia = db.Column(db.Integer, nullable=False)
    salario = db.Column(db.DECIMAL, nullable=False)
    idProyecto = db.Column(db.Integer, db.ForeignKey('proyecto.idProyecto'))

class Locaciones(db.Model):
    idLocacion = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(255), nullable=False)
    direccion = db.Column(db.String(255), nullable=False)
    costoAlquiler = db.Column(db.DECIMAL, nullable=False)
    idProyecto = db.Column(db.Integer, db.ForeignKey('proyecto.idProyecto'))

class Maquilladores(db.Model):
    idMaquillador = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(255), nullable=False)
    especialidad = db.Column(db.String(255), nullable=False)
    salario = db.Column(db.DECIMAL, nullable=False)
    idProyecto = db.Column(db.Integer, db.ForeignKey('proyecto.idProyecto'))

class Utileria(db.Model):
    idUtileria = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    costo = db.Column(db.DECIMAL, nullable=False)
    idProyecto = db.Column(db.Integer, db.ForeignKey('proyecto.idProyecto'))

class Camaras(db.Model):
    idCamara = db.Column(db.Integer, primary_key=True, autoincrement=True)
    modelo = db.Column(db.String(255), nullable=False)
    costo = db.Column(db.DECIMAL, nullable=False)
    idProyecto = db.Column(db.Integer, db.ForeignKey('proyecto.idProyecto'))

class Camarografos(db.Model):
    idCamarografo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(255), nullable=False)
    experiencia = db.Column(db.Integer, nullable=False)
    salario = db.Column(db.DECIMAL, nullable=False)
    idProyecto = db.Column(db.Integer, db.ForeignKey('proyecto.idProyecto'))

class Ambientadores(db.Model):
    idAmbientador = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    costo = db.Column(db.DECIMAL, nullable=False)
    idProyecto = db.Column(db.Integer, db.ForeignKey('proyecto.idProyecto'))

class Sonido(db.Model):
    idSonido = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    costo = db.Column(db.DECIMAL, nullable=False)
    idProyecto = db.Column(db.Integer, db.ForeignKey('proyecto.idProyecto'))

class Iluminacion(db.Model):
    idIluminacion = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    costo = db.Column(db.DECIMAL, nullable=False)
    idProyecto = db.Column(db.Integer, db.ForeignKey('proyecto.idProyecto'))

class Preproduccion(db.Model):
    idPreproduccion = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    costo = db.Column(db.DECIMAL, nullable=False)
    idProyecto = db.Column(db.Integer, db.ForeignKey('proyecto.idProyecto'))

class Edicion(db.Model):
    idEdicion = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    costo = db.Column(db.DECIMAL, nullable=False)
    idProyecto = db.Column(db.Integer, db.ForeignKey('proyecto.idProyecto'))

class Postproduccion(db.Model):
    idPostproduccion = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    costo = db.Column(db.DECIMAL, nullable=False)
    idProyecto = db.Column(db.Integer, db.ForeignKey('proyecto.idProyecto'))

class Transporte(db.Model):
    idTransporte = db.Column(db.Integer, primary_key=True, autoincrement=True)
    vehiculo = db.Column(db.String(255), nullable=False)
    costo = db.Column(db.DECIMAL, nullable=False)
    idProyecto = db.Column(db.Integer, db.ForeignKey('proyecto.idProyecto'))

class Viaticos(db.Model):
    idViatico = db.Column(db.Integer, primary_key=True, autoincrement=True)
    destino = db.Column(db.String(255), nullable=False)
    costo = db.Column(db.DECIMAL, nullable=False)
    idProyecto = db.Column(db.Integer, db.ForeignKey('proyecto.idProyecto'))

# Agrega más clases de modelos según tus necesidades
