-- Tabla para almacenar la información de cada sesión de flexiones
CREATE TABLE SesionesFlexiones (
    id_sesion INT AUTO_INCREMENT PRIMARY KEY,
    nombre_usuario VARCHAR(50) NOT NULL,
    objetivo INT NOT NULL,
    flexiones_realizadas INT DEFAULT 0,
    estado ENUM('Iniciada', 'Finalizada') DEFAULT 'Iniciada',
    fecha_inicio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_fin TIMESTAMP NULL
);

-- Tabla para almacenar el progreso de flexiones realizadas en cada sesión
CREATE TABLE ProgresoSesion (
    id_progreso INT AUTO_INCREMENT PRIMARY KEY,
    id_sesion INT,
    flexiones INT,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_sesion) REFERENCES SesionesFlexiones(id_sesion)
);


-- Insertar sesiones de flexiones
INSERT INTO SesionesFlexiones (nombre_usuario, objetivo, flexiones_realizadas, estado, fecha_inicio)
VALUES 
('Juan Pérez', 20, 15, 'Iniciada', '2024-09-01 08:00:00'),
('Ana Martínez', 30, 25, 'Iniciada', '2024-09-01 09:00:00'),
('Luis García', 15, 15, 'Finalizada', '2024-09-01 10:00:00', '2024-09-01 10:30:00'),
('Laura Fernández', 25, 20, 'Iniciada', '2024-09-01 11:00:00'),
('Carlos López', 10, 10, 'Finalizada', '2024-09-01 12:00:00', '2024-09-01 12:30:00'),
('Marta González', 40, 35, 'Iniciada', '2024-09-02 08:00:00'),
('Pedro Sánchez', 50, 45, 'Iniciada', '2024-09-02 09:00:00'),
('Sofia Ruiz', 12, 12, 'Finalizada', '2024-09-02 10:00:00', '2024-09-02 10:30:00'),
('Jorge Ramírez', 18, 16, 'Iniciada', '2024-09-02 11:00:00'),
('Isabel Morales', 22, 22, 'Finalizada', '2024-09-02 12:00:00', '2024-09-02 12:30:00');

-- Insertar progreso de flexiones
INSERT INTO ProgresoSesion (id_sesion, flexiones)
VALUES 
(1, 1),
(1, 1),
(1, 1),
(1, 1),
(1, 1),
(1, 1),
(1, 1),
(1, 1),
(1, 1),
(1, 1),
(1, 1),
(1, 1),
(1, 1),
(1, 1),
(1, 1),
(1, 1),
(1, 1),
(1, 1),
(1, 1),
(1, 1),
(1, 1),
(2, 1),
(2, 1),
(2, 1),
(2, 1),
(2, 1),
(2, 1),
(2, 1),
(2, 1),
(2, 1),
(2, 1),
(2, 1),
(2, 1),
(2, 1),
(2, 1),
(2, 1),
(2, 1),
(2, 1),
(2, 1),
(2, 1),
(2, 1),
(2, 1),
(3, 1),
(3, 1),
(3, 1),
(3, 1),
(3, 1),
(3, 1),
(3, 1),
(3, 1),
(3, 1),
(3, 1),
(3, 1),
(3, 1),
(3, 1),
(3, 1),
(3, 1),
(3, 1),
(3, 1),
(3, 1),
(3, 1),
(3, 1),
(4, 1),
(4, 1),
(4, 1),
(4, 1),
(4, 1),
(4, 1),
(4, 1),
(4, 1),
(4, 1),
(4, 1),
(4, 1),
(4, 1),
(4, 1),
(4, 1),
(4, 1),
(4, 1),
(4, 1),
(4, 1),
(4, 1),
(4, 1);


SELECT * FROM SesionesFlexiones
WHERE flexiones_realizadas >= objetivo;


SELECT * FROM ProgresoSesion
WHERE id_sesion = 1;


SELECT AVG(flexiones_realizadas) AS promedio_flexiones
FROM SesionesFlexiones
WHERE estado = 'Finalizada';


SELECT s.id_sesion, s.nombre_usuario, s.objetivo, s.flexiones_realizadas, p.flexiones
FROM SesionesFlexiones s
LEFT JOIN ProgresoSesion p ON s.id_sesion = p.id_sesion
WHERE s.estado = 'Iniciada';


SELECT nombre_usuario, SUM(flexiones_realizadas) AS total_flexiones
FROM SesionesFlexiones
GROUP BY nombre_usuario;


