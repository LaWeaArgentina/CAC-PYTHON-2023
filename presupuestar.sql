-- Estructura de tabla para la tabla `contactos`
--

CREATE TABLE `contactos` (
  `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4,
  `nombre` varchar(20) NOT NULL,
  `email` varchar(40) NOT NULL,
  `mensaje` text NOT NULL,
  `respondido` int(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `contactos` (`id`, `nombre`, `email`, `mensaje`, `respondido`) VALUES
(1, 'juan', 'juan@gmail.com', 'hola test', 1),
(2, 'Juan Ignacio', 'juansolari39@gmail.com', 'SDA', 0);
ALTER TABLE `contactos`
  ADD PRIMARY KEY (`id`);
