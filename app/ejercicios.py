import mysql.connector
import os

try:

    # 1. Conectar a la base de datos
    conn = mysql.connector.connect(
        host="db-server",
        user="root",
        password="clase123",
        database="escuela_db"
    )

    cursor = conn.cursor()

    # Ejercicio 1: Agregar más estudiantes
    print("\n ### Ejercicio 1: Agregar más estudiantes ###")
    print("\n--- 3 Estudiantes mas insertados ---")
    datos_estudiantes = [
        ("Elias Gomez", 21, "Ingeniería de Software"),
        ("Luis Valdez", 37, "Lic. Comunicaciones"),
        ("Xochilt Gomez", 25, "Actriz")
    ]

    cursor.executemany(
        "INSERT INTO estudiantes (nombre, edad, carrera) VALUES (%s, %s, %s)",
        datos_estudiantes
    )
    print("Tabla estudiantes:")
    cursor.execute("SELECT * FROM estudiantes")
    for fila in cursor.fetchall():
        print(fila)

    # Ejercicio 2: SELECT con filtro (WHERE)
    print("\n ### Ejercicio 2: SELECT con filtro (WHERE) ###")
    print("\n--- Estudiantes de Medicina ---")
    cursor.execute("SELECT * FROM estudiantes WHERE carrera = 'Medicina'")
    for fila in cursor.fetchall():
        print(fila)

    # Ejercicio 3: Crear una nueva tabla
    print("\n ### Ejercicio 3: Crear una nueva tabla ### ")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS profesores (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            materia VARCHAR(100),
            email VARCHAR(100)
        )
    """)
    print("\n✅ Tabla 'profesores' lista")

    # Insertar profesores
    print("\n--- 2 Registros insertados en profesores ---")
    datos_profesores = [
        ("Ray Brunett", "Aplicaciones moviles", "ray@gmail.com"),
        ("Clenorio Hernandez", "Base de datos", "cleo@gmail.com"),
        ("Jose Falcon", "Ingles", "falcon@gmail.com")
    ]

    cursor.executemany(
        "INSERT INTO profesores (nombre, materia, email) VALUES (%s, %s, %s)",
        datos_profesores
    )
    print("Mostrando resultados de profesores:")
    cursor.execute("SELECT * FROM profesores")
    for fila in cursor.fetchall():
        print(fila)

    # Ejercicio 4: Actualizar y eliminar
    print("\n ### Ejercicio 4: Actualizar y eliminar ### ")
    cursor.execute("UPDATE estudiantes SET edad = 21 WHERE nombre = 'Ana López'")
    cursor.execute("DELETE FROM estudiantes WHERE nombre = 'Carlos Ruiz'")

    # Mostrar resultados finales de estudiantes
    print("\n--- Lista de Estudiantes Actualizada ---")
    cursor.execute("SELECT * FROM estudiantes")
    for est in cursor.fetchall():
        print(est)

    print("\n--- Resultado ---")
    cursor.execute("SELECT * FROM estudiantes")
    for fila in cursor.fetchall():
        print(fila)

    print(f"\n✅ Proceso finalizado.")

    cursor.close()
    conn.close()
except Exception as e:
    print(f"❌ Error: {e}")