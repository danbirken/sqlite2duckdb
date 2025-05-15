import duckdb
import os
import time


def sqlite_to_duckdb(sqlite_db: str, duck_db: str):
    print(f"Create {duck_db} databases")

    if not os.path.exists(sqlite_db):
        raise Exception(f"File {sqlite_db} doesn't exists")

    # Remove target db if exists
    if os.path.exists(duck_db):
        raise Exception(f"Database {duck_db} already exists")

    start_time = time.perf_counter()
    conn = duckdb.connect()

    ## Install sqlite
    conn.sql("INSTALL sqlite;")
    conn.sql("LOAD sqlite;")

    # Use the "COPY" duckdb command to copy the databases
    # This will preserve the constraints
    conn.execute(f"ATTACH '{sqlite_db}' as sqlite_db;")
    conn.execute(f"ATTACH '{duck_db}' as duck_db;")
    conn.execute("COPY FROM DATABASE sqlite_db TO duck_db;")
    conn.close()

    end_time = time.perf_counter()
    execution_time = (end_time - start_time) * 1000
    print(f"Done in {execution_time:.2f} ms !")
