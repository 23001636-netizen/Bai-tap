import mysql.connector

cfg = {
    'host':'localhost',
    'user':'root',
    'password':'Minhtu2005',
}
try:
    conn = mysql.connector.connect(**cfg)
    cur = conn.cursor()
    cur.execute("SET GLOBAL local_infile = 1;")
    conn.commit()
    cur.execute("SHOW GLOBAL VARIABLES LIKE 'local_infile';")
    print(cur.fetchall())
    cur.close()
    conn.close()
except Exception as e:
    print('ERROR:', e)
