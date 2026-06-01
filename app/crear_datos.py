import mysql.connector
import os
import time

# Esperar un poco a que la DB esté lista
time.sleep(5)

try:
    # 1. Conectar a la base de datos
    conn = mysql.connector.connect(
        host="db-server",
        user="root",
        password="clase123",
        database="escuela_db"
    )

    # 2. Crear un cursor: es como un "puntero" para ejecutar comandos
    cursor = conn.cursor()
    
    # 3. Crear la tabla (si no existe)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS estudiantes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            edad INT,
            carrera VARCHAR(100)
        )
    """)
    print("✅ Tabla 'estudiantes' lista")

    # 4. Insertar datos usando parámetros (%s) en lugar de valores fijos
    #    Esto es más seguro y evita errores de tipos
    datos = [
        ("Ana López", 20, "Ingeniería de Sistemas"),
        ("Carlos Ruiz", 22, "Medicina"),
        ("María Torres", 19, "Diseño Gráfico")
    ]

    cursor.executemany(
        "INSERT INTO estudiantes (nombre, edad, carrera) VALUES (%s, %s, %s)",
        datos
    )

    conn.commit()  # ⚠️ OBLIGATORIO: guarda los cambios en la BD
    print(f"✅ {cursor.rowcount} filas insertadas.")

    # 5. Leer los datos y mostrarlos
    cursor.execute("SELECT * FROM estudiantes")
    for fila in cursor.fetchall():
        print(fila)

    # 6. Cerrar todo (buena práctica)
    cursor.close()
    conn.close()
except Exception as e:
    print(f"❌ Error: {e}")