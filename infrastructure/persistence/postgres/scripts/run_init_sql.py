import asyncio
import os
import sys
import re
from sqlalchemy import text
from infrastructure.persistence.postgres.postgres import engine
sys.path.append(os.getcwd())


async def run_init_sql():

    sql_file_path = "infrastructure/persistence/postgres/scripts/audify.sql"

    if not os.path.exists(sql_file_path):
        raise FileNotFoundError(f"No se encontró el archivo {sql_file_path}")

    try:
        print(f"Leyendo script SQL desde {sql_file_path}...")
        with open(sql_file_path, "r", encoding="utf-8") as f:
            sql_content = f.read()
    except Exception as e:
        raise FileNotFoundError(f"Error al leer el archivo {sql_file_path}: {e}")

    # Separar por ";" para ejecutar pos statements
    statements = re.split(r';\s*(?=(?:[^\$]*\$\$[^\$]*\$\$)*[^\$]*$)', sql_content)

    try:
        print("Conectando a Railway...")
        async with engine.begin() as conn:
            for statement in statements:
                stmt = statement.strip()
                if not stmt:
                    continue
                print(f"Ejecutando bloque: {stmt[:50]}...")
                await conn.execute(text(stmt))
        print("\n¡Éxito! La base de datos en Railway ha sido inicializada.")
    except Exception as e:
        raise Exception(f"Error al ejecutar el script: {e}")
    finally:
        await engine.dispose()

if __name__ == "__main__":
    asyncio.run(run_init_sql())
