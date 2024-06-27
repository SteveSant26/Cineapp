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

-- CREATE TABLE asientos_reservados (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     funcion_id INT,
--     fila INT,
--     columna INT,
--     reservado BOOLEAN DEFAULT TRUE,
--     FOREIGN KEY (funcion_id) REFERENCES funciones(id) ON DELETE CASCADE,
--     UNIQUE (funcion_id, fila, columna)
-- );

-- INSERT INTO peliculas (id, ruta_imagen, titulo, sinopsis, genero, duracion, estreno, promedio_votos) 
-- VALUES(1154598,'https://image.tmdb.org/t/p/original//4ba3Kw9isyWvu6cupzUagm8ejw2.jpg', 'LEGO Marvel Avengers: Código rojo', 'En un multiverso amenazado por el enigmático Fantasma Rojo, los LEGO Vengadores se unen a sus homólogos para detener el caos de la realidad', 'Animación, Acción, Familia', 46, '2023-10-26', 6.665),
-- INSERT INTO salas (nombre, filas, columnas) VALUES ('Sala 1', 10, 10);
-- INSERT INTO funciones (pelicula_id, sala_id, fecha_hora) VALUES (1154598, 1, '2021-10-10 10:00:00');
-- INSERT INTO peliculas (id, ruta_imagen, titulo, sinopsis, genero, duracion, estreno, promedio_votos) 
-- VALUES(39108,'https://image.tmdb.org/t/p/original//ldTcRH6A2bQ8rd6hGb5C0I4JjIU.jpg', 'Dragon Ball Z: El ataque del dragón','Hoi, un extraño hechicero, le pide a Goku que reúna las bolas de dragón para liberar de su prisión al héroe de su planeta, Tapión. Goku accede a ayudarle, pero pronto se da cuenta de que Tapión es realmente un poderoso monstruo llamado Hildengan', 'Animación, Acción, Ciencia ficción', 50, '1995-07-15', 7.247);

