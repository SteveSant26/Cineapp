-- CREATE TABLE peliculas (
--     id INT PRIMARY KEY,
--     ruta_imagen VARCHAR(200) NOT NULL,
--     titulo VARCHAR(150) NOT NULL,
--     sinopsis TEXT,
--     genero VARCHAR(255), 
--     duracion INT,
--     estreno DATE,
--     promedio_votos DECIMAL(3, 2)
-- );


-- CREATE TABLE salas (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     nombre VARCHAR(255) NOT NULL UNIQUE,
--     filas INT,
--     columnas INT
-- );


-- CREATE TABLE funciones (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     pelicula_id INT,
--     sala_id INT,
--     fecha_hora DATETIME,
--     FOREIGN KEY (pelicula_id) REFERENCES peliculas(id) ON DELETE CASCADE,
--     FOREIGN KEY (sala_id) REFERENCES salas(id) ON DELETE CASCADE
-- );


