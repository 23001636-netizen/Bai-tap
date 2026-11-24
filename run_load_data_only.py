import mysql.connector
import time

DB_CONFIG = {
    'host':'localhost',
    'user':'root',
    'password':'Minhtu2005',
    'database':'test1',
    'allow_local_infile': True,
}
FILES = [
    r'C:\Users\ACER\Desktop\train_part1.csv',
    r'C:\Users\ACER\Desktop\train_part2.csv',
    r'C:\Users\ACER\Desktop\train_part3.csv',
]

conn = mysql.connector.connect(**DB_CONFIG)
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS load_only (id INT AUTO_INCREMENT PRIMARY KEY, text LONGTEXT) ENGINE=InnoDB')
conn.commit()
results = {}
for f in FILES:
    fname = f.split('\\')[-1]
    cur.execute('DELETE FROM load_only')
    conn.commit()
    start = time.time()
    try:
        sql = "LOAD DATA LOCAL INFILE '%s' INTO TABLE load_only FIELDS TERMINATED BY ',' LINES TERMINATED BY '\\n' IGNORE 1 LINES (text)" % f.replace('\\','/')
        print('SQL:', sql)
        cur.execute(sql)
        conn.commit()
        elapsed = time.time() - start
        results[fname] = {'load_data_time': elapsed}
        print(fname, 'loaded in', elapsed)
    except Exception as e:
        results[fname] = {'error': str(e)}
        print(fname, 'failed:', e)
cur.close()
conn.close()

import json
with open('c:\\Users\\ACER\\Desktop\\load_data_only_results.json','w',encoding='utf-8') as out:
    json.dump(results, out, indent=2)
print('Done')
