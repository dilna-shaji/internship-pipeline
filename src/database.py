import os
import psycopg2

def get_db_connection():
    return psycopg2.connect(os.environ.get("DB_CONNECTION_STRING"))

def save_internships(jobs_list):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """INSERT INTO internships (company, role, stipend, location, apply_url^) 
               VALUES (%%s, %%s, %%s, %%s, %%s) 
               ON CONFLICT (company, apply_url) DO NOTHING;"""
    for job in jobs_list:
        cursor.execute(query, (job['company'], job['role'], job['stipend'], job['location'], job['apply_url']))
    conn.commit()
    cursor.close()
    conn.close()
