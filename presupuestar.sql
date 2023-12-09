DROP TABLE IF EXISTS contactos, users, Cliente, Proyecto, Presupuesto, Item, Actores, Vestuaristas, Directores, Locaciones, Maquilladores, Utileria, Camaras, Camarografos, Ambientadores, Sonido, Iluminacion, Preproduccion, Edicion, Postproduccion, Transporte, Viaticos;

-- Estructura de tabla para la tabla `contactos`

CREATE TABLE `contactos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(20) NOT NULL,
  `email` VARCHAR(40) NOT NULL,
  `mensaje` TEXT NOT NULL,
  `respondido` INT DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `contactos` (`nombre`, `email`, `mensaje`, `respondido`) VALUES
('Juan', 'juan@example.com', 'Hola, estoy interesado en sus servicios.', 0),
('Ana', 'ana@example.com', 'Quisiera obtener más información sobre sus productos.', 1),
('Carlos', 'carlos@example.com', 'Tengo una consulta acerca de sus servicios.', NULL);


-- Creación de la tabla Usuarios App (Equipo de Trabajo)

CREATE TABLE users (
  id INT PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(50) UNIQUE NOT NULL,
  password VARCHAR(255) NOT NULL,
  is_admin BOOLEAN DEFAULT FALSE
);

-- Insertar datos ficticios en la tabla Users
INSERT INTO users (username, password, is_admin) VALUES
  ('ana', '111', TRUE),
  ('juan', '111', FALSE),
  ('diego', '111', FALSE),
  ('guillermo', '111', TRUE),
  ('gonzalo', '111', FALSE),
  ('hernan', '111', TRUE);

-- Creación de la tabla para Cliente
CREATE TABLE Cliente (
    idCliente INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    direccion VARCHAR(255) NOT NULL,
    telefono VARCHAR(20) NOT NULL,
    email VARCHAR(255) NOT NULL
);

-- Insertar datos ficticios en la tabla Cliente
INSERT INTO Cliente (nombre, direccion, telefono, email) VALUES
  ('Cliente1', 'Dirección1', '123456789', 'cliente1@example.com'),
  ('Cliente2', 'Dirección2', '987654321', 'cliente2@example.com'),
  ('Cliente3', 'Dirección3', '111223344', 'cliente3@example.com');

-- Creación de la tabla para Proyecto
CREATE TABLE Proyecto (
    idProyecto INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT,
    fechaInicio DATE NOT NULL,
    fechaFin DATE NOT NULL
);

-- Insertar datos ficticios en la tabla Proyecto
INSERT INTO Proyecto (nombre, descripcion, fechaInicio, fechaFin) VALUES
  ('Proyecto1', 'Descripción Proyecto 1', '2023-01-10', '2023-02-10'),
  ('Proyecto2', 'Descripción Proyecto 2', '2023-02-15', '2023-03-15'),
  ('Proyecto3', 'Descripción Proyecto 3', '2023-03-20', '2023-04-20');


-- Creación de la tabla para Presupuesto
CREATE TABLE Presupuesto (
    idPresupuesto INT PRIMARY KEY AUTO_INCREMENT,
    fecha DATE NOT NULL,
    total DECIMAL NOT NULL,
    idCliente INT,
    idProyecto INT,
    FOREIGN KEY (idCliente) REFERENCES Cliente(idCliente),
    FOREIGN KEY (idProyecto) REFERENCES Proyecto(idProyecto)
);

-- Insertar datos ficticios en la tabla Presupuesto
INSERT INTO Presupuesto (fecha, total, idCliente, idProyecto) VALUES
  ('2023-01-01', 1500.00, 1, 1),
  ('2023-02-01', 2000.00, 2, 2),
  ('2023-03-01', 1800.00, 3, 3);

-- Creación de la tabla para Item
CREATE TABLE Item (
    idItem INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    costo DECIMAL NOT NULL,
    idPresupuesto INT,
    FOREIGN KEY (idPresupuesto) REFERENCES Presupuesto(idPresupuesto)
);

-- Insertar datos ficticios en la tabla Item
INSERT INTO Item (nombre, costo, idPresupuesto) VALUES
  ('Item1', 100.00, 1),
  ('Item2', 150.00, 2),
  ('Item3', 120.00, 3);

-- Creación de la tabla para Actores
CREATE TABLE Actores (
    idActor INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    edad INT NOT NULL,
    sexo VARCHAR(10) NOT NULL,
    salario DECIMAL NOT NULL,
    idProyecto INT,
    FOREIGN KEY (idProyecto) REFERENCES Proyecto(idProyecto)
);

-- Insertar datos ficticios en la tabla Actores
INSERT INTO Actores (nombre, edad, sexo, salario, idProyecto) VALUES
  ('Actor1', 30, 'Masculino', 2000.00, 1),
  ('Actor2', 25, 'Femenino', 1800.00, 2),
  ('Actor3', 35, 'Masculino', 2200.00, 3);

-- Creación de la tabla para Vestuaristas
CREATE TABLE Vestuaristas (
    idVestuarista INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    especialidad VARCHAR(255) NOT NULL,
    salario DECIMAL NOT NULL,
    idProyecto INT,
    FOREIGN KEY (idProyecto) REFERENCES Proyecto(idProyecto)
);

-- Insertar datos ficticios en la tabla Vestuaristas
INSERT INTO Vestuaristas (nombre, especialidad, salario, idProyecto) VALUES
  ('Vestuarista1', 'Diseño de Vestuario', 1500.00, 1),
  ('Vestuarista2', 'Estilismo', 1200.00, 2),
  ('Vestuarista3', 'Diseño de Moda', 1800.00, 3);

  -- Creación de la tabla para Directores
CREATE TABLE Directores (
    idDirector INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    experiencia INT NOT NULL,
    salario DECIMAL NOT NULL,
    idProyecto INT,
    FOREIGN KEY (idProyecto) REFERENCES Proyecto(idProyecto)
);

-- Insertar datos ficticios en la tabla Directores
INSERT INTO Directores (nombre, experiencia, salario, idProyecto) VALUES
  ('Director1', 10, 2500.00, 1),
  ('Director2', 15, 2800.00, 2),
  ('Director3', 20, 3000.00, 3);

  -- Creación de la tabla para Locaciones
CREATE TABLE Locaciones (
    idLocacion INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    direccion VARCHAR(255) NOT NULL,
    costoAlquiler DECIMAL NOT NULL,
    idProyecto INT,
    FOREIGN KEY (idProyecto) REFERENCES Proyecto(idProyecto)
);

-- Insertar datos ficticios en la tabla Locaciones
INSERT INTO Locaciones (nombre, direccion, costoAlquiler, idProyecto) VALUES
  ('Locacion1', 'Calle Principal 123', 1500.00, 1),
  ('Locacion2', 'Avenida Secundaria 456', 2000.00, 2),
  ('Locacion3', 'Plaza Central 789', 1800.00, 3);

-- Creación de la tabla para Maquilladores
CREATE TABLE Maquilladores (
    idMaquillador INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    especialidad VARCHAR(255) NOT NULL,
    salario DECIMAL NOT NULL,
    idProyecto INT,
    FOREIGN KEY (idProyecto) REFERENCES Proyecto(idProyecto)
);

-- Insertar datos ficticios en la tabla Maquilladores
INSERT INTO Maquilladores (nombre, especialidad, salario, idProyecto) VALUES
  ('Maquillador1', 'Maquillaje de Fantasía', 1200.00, 1),
  ('Maquillador2', 'Maquillaje de Cine', 1000.00, 2),
  ('Maquillador3', 'Estilismo de Maquillaje', 1300.00, 3);

-- Creación de la tabla para Utileria
CREATE TABLE Utileria (
    idUtileria INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT NOT NULL,
    costo DECIMAL NOT NULL,
    idProyecto INT,
    FOREIGN KEY (idProyecto) REFERENCES Proyecto(idProyecto)
);

-- Insertar datos ficticios en la tabla Utileria
INSERT INTO Utileria (nombre, descripcion, costo, idProyecto) VALUES
  ('Utileria1', 'Elementos de Escenografía', 800.00, 1),
  ('Utileria2', 'Accesorios de Ambientación', 700.00, 2),
  ('Utileria3', 'Objetos Decorativos', 900.00, 3);

  -- Creación de la tabla para Camaras
CREATE TABLE Camaras (
    idCamara INT PRIMARY KEY AUTO_INCREMENT,
    modelo VARCHAR(255) NOT NULL,
    costo DECIMAL NOT NULL,
    idProyecto INT,
    FOREIGN KEY (idProyecto) REFERENCES Proyecto(idProyecto)
);

-- Insertar datos ficticios en la tabla Camaras
INSERT INTO Camaras (modelo, costo, idProyecto) VALUES
  ('Camara1', 5000.00, 1),
  ('Camara2', 6000.00, 2),
  ('Camara3', 5500.00, 3);

-- Creación de la tabla para Camarografos
CREATE TABLE Camarografos (
    idCamarografo INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    experiencia INT NOT NULL,
    salario DECIMAL NOT NULL,
    idProyecto INT,
    FOREIGN KEY (idProyecto) REFERENCES Proyecto(idProyecto)
);

-- Insertar datos ficticios en la tabla Camarografos
INSERT INTO Camarografos (nombre, experiencia, salario, idProyecto) VALUES
  ('Camarografo1', 5, 2000.00, 1),
  ('Camarografo2', 7, 2500.00, 2),
  ('Camarografo3', 6, 2200.00, 3);

-- Creación de la tabla para Ambientadores
CREATE TABLE Ambientadores (
    idAmbientador INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT NOT NULL,
    costo DECIMAL NOT NULL,
    idProyecto INT,
    FOREIGN KEY (idProyecto) REFERENCES Proyecto(idProyecto)
);

-- Insertar datos ficticios en la tabla Ambientadores
INSERT INTO Ambientadores (nombre, descripcion, costo, idProyecto) VALUES
  ('Ambientador1', 'Fragancia floral para ambientar', 300.00, 1),
  ('Ambientador2', 'Esencias naturales para la atmosfera', 250.00, 2),
  ('Ambientador3', 'Aromas especiales para eventos', 280.00, 3);

-- Creación de la tabla para Sonido
CREATE TABLE Sonido (
    idSonido INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT NOT NULL,
    costo DECIMAL NOT NULL,
    idProyecto INT,
    FOREIGN KEY (idProyecto) REFERENCES Proyecto(idProyecto)
);

-- Insertar datos ficticios en la tabla Sonido
INSERT INTO Sonido (nombre, descripcion, costo, idProyecto) VALUES
  ('Sonido1', 'Equipo de audio profesional', 1200.00, 1),
  ('Sonido2', 'Altavoces de alta fidelidad', 1000.00, 2),
  ('Sonido3', 'Sistema de grabación de calidad', 1300.00, 3);

  -- Creación de la tabla para Iluminacion
CREATE TABLE Iluminacion (
    idIluminacion INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT NOT NULL,
    costo DECIMAL NOT NULL,
    idProyecto INT,
    FOREIGN KEY (idProyecto) REFERENCES Proyecto(idProyecto)
);

-- Insertar datos ficticios en la tabla Iluminacion
INSERT INTO Iluminacion (nombre, descripcion, costo, idProyecto) VALUES
  ('Iluminacion1', 'Luces LED para escenarios', 800.00, 1),
  ('Iluminacion2', 'Focos halógenos de alta potencia', 1000.00, 2),
  ('Iluminacion3', 'Efectos especiales de iluminación', 900.00, 3);

-- Creación de la tabla para Preproduccion
CREATE TABLE Preproduccion (
    idPreproduccion INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT NOT NULL,
    costo DECIMAL NOT NULL,
    idProyecto INT,
    FOREIGN KEY (idProyecto) REFERENCES Proyecto(idProyecto)
);

-- Insertar datos ficticios en la tabla Preproduccion
INSERT INTO Preproduccion (nombre, descripcion, costo, idProyecto) VALUES
  ('Preproduccion1', 'Planificación y guion', 1500.00, 1),
  ('Preproduccion2', 'Revisión de locaciones y casting', 1800.00, 2),
  ('Preproduccion3', 'Diseño de arte y vestuario', 1600.00, 3);

-- Creación de la tabla para Edicion
CREATE TABLE Edicion (
    idEdicion INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT NOT NULL,
    costo DECIMAL NOT NULL,
    idProyecto INT,
    FOREIGN KEY (idProyecto) REFERENCES Proyecto(idProyecto)
);

-- Insertar datos ficticios en la tabla Edicion
INSERT INTO Edicion (nombre, descripcion, costo, idProyecto) VALUES
  ('Edicion1', 'Montaje y edición de video', 2000.00, 1),
  ('Edicion2', 'Efectos visuales y sonoros', 2200.00, 2),
  ('Edicion3', 'Corrección de color y postproducción', 2400.00, 3);

-- Creación de la tabla para Postproduccion
CREATE TABLE Postproduccion (
    idPostproduccion INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT NOT NULL,
    costo DECIMAL NOT NULL,
    idProyecto INT,
    FOREIGN KEY (idProyecto) REFERENCES Proyecto(idProyecto)
);

-- Insertar datos ficticios en la tabla Postproduccion
INSERT INTO Postproduccion (nombre, descripcion, costo, idProyecto) VALUES
  ('Postproduccion1', 'Masterización y finalización', 1800.00, 1),
  ('Postproduccion2', 'Diseño de efectos especiales', 2000.00, 2),
  ('Postproduccion3', 'Entrega y distribución', 1600.00, 3);

-- Creación de la tabla para Transporte
CREATE TABLE Transporte (
    idTransporte INT PRIMARY KEY AUTO_INCREMENT,
    vehiculo VARCHAR(255) NOT NULL,
    costo DECIMAL NOT NULL,
    idProyecto INT,
    FOREIGN KEY (idProyecto) REFERENCES Proyecto(idProyecto)
);

-- Insertar datos ficticios en la tabla Transporte
INSERT INTO Transporte (vehiculo, costo, idProyecto) VALUES
  ('Transporte1', 500.00, 1),
  ('Transporte2', 600.00, 2),
  ('Transporte3', 550.00, 3);

-- Creación de la tabla para Viaticos
CREATE TABLE Viaticos (
    idViatico INT PRIMARY KEY AUTO_INCREMENT,
    destino VARCHAR(255) NOT NULL,
    costo DECIMAL NOT NULL,
    idProyecto INT,
    FOREIGN KEY (idProyecto) REFERENCES Proyecto(idProyecto)
);

-- Insertar datos ficticios en la tabla Viaticos
INSERT INTO Viaticos (destino, costo, idProyecto) VALUES
  ('Viaje a locaciones', 800.00, 1),
  ('Estadía y alimentación', 1000.00, 2),
  ('Gastos varios durante la producción', 900.00, 3);

  
