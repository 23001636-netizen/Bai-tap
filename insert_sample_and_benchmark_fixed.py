import mysql.connector
import csv
import time

DB_CONFIG = {
    'host':'localhost',
    'user':'root',
    'password':'Minhtu2005',
    'database':'test1',
    'allow_local_infile': True,
}
FILE = r'C:\Users\ACER\Desktop\train_sample_1M.csv'

# Prepare DB table
conn = mysql.connector.connect(**DB_CONFIG)
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS sample_text (
    id INT AUTO_INCREMENT PRIMARY KEY,
    text LONGTEXT
) ENGINE=InnoDB;
''')
conn.commit()

# Helper to clear table
def clear_table():
    cursor.execute('DELETE FROM sample_text')
    conn.commit()

# Method 1: insert row by row
print('Starting Method 1 (row-by-row)')
clear_table()
start = time.time()
with open(FILE,'r',encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    for i,row in enumerate(reader,1):
        cursor.execute('INSERT INTO sample_text (text) VALUES (%s)', (row[0],))
        if i%100000==0:
            print('inserted',i)
conn.commit()
end = time.time()
print('Row-by-row time:', end-start)

# Method 2: executemany
print('Starting Method 2 (executemany)')
clear_table()
start = time.time()
with open(FILE,'r',encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    data = [(r[0],) for r in reader]
# send in chunks to avoid memory spike
CHUNK = 100000
for i in range(0, len(data), CHUNK):
    cursor.executemany('INSERT INTO sample_text (text) VALUES (%s)', data[i:i+CHUNK])
    conn.commit()
end = time.time()
print('Executemany time:', end-start)

# Method 3: LOAD DATA INFILE
print('Starting Method 3 (LOAD DATA LOCAL INFILE)')
clear_table()
start = time.time()
try:
    sql = ("LOAD DATA LOCAL INFILE '%s' INTO TABLE sample_text "
           "FIELDS TERMINATED BY ',' ENCLOSED BY '\"' LINES TERMINATED BY '\\n' "
           "IGNORE 1 LINES (text)") % FILE.replace('\\','/')
    cursor.execute(sql)
    conn.commit()
    end = time.time()
    print('LOAD DATA INFILE time:', end-start)
except Exception as e:
    print('LOAD DATA INFILE failed:', e)

cursor.close()
conn.close()
