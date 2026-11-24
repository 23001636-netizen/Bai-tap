import mysql.connector
import csv
import time
import json

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
RESULTS = {}

conn = mysql.connector.connect(**DB_CONFIG)
cursor = conn.cursor()
# ensure table
cursor.execute('''CREATE TABLE IF NOT EXISTS multi_sample (id INT AUTO_INCREMENT PRIMARY KEY, text LONGTEXT) ENGINE=InnoDB''')
conn.commit()

for fpath in FILES:
    fname = fpath.split('\\')[-1]
    RESULTS[fname] = {}
    print('\nProcessing', fname)
    # Method 1: row-by-row
    cursor.execute('DELETE FROM multi_sample')
    conn.commit()
    start = time.time()
    with open(fpath,'r',encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        for i,row in enumerate(reader,1):
            cursor.execute('INSERT INTO multi_sample (text) VALUES (%s)', (row[0],))
            if i%500000==0:
                print('  inserted',i)
    conn.commit()
    RESULTS[fname]['row_by_row'] = time.time() - start
    print('  row_by_row time:', RESULTS[fname]['row_by_row'])

    # Method 2: executemany chunked
    cursor.execute('DELETE FROM multi_sample')
    conn.commit()
    start = time.time()
    data = []
    with open(fpath,'r',encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            data.append((row[0],))
    CHUNK = 100000
    for i in range(0, len(data), CHUNK):
        chunk = data[i:i+CHUNK]
        cursor.executemany('INSERT INTO multi_sample (text) VALUES (%s)', chunk)
        conn.commit()
        print('  executemany inserted', min(i+CHUNK, len(data)))
    RESULTS[fname]['executemany'] = time.time() - start
    print('  executemany time:', RESULTS[fname]['executemany'])

    # Method 3: LOAD DATA LOCAL INFILE
    cursor.execute('DELETE FROM multi_sample')
    conn.commit()
    start = time.time()
    try:
        sql = ("LOAD DATA LOCAL INFILE '%s' INTO TABLE multi_sample "
                       "FIELDS TERMINATED BY ',' LINES TERMINATED BY '\\n' "
               "IGNORE 1 LINES (text)") % fpath.replace('\\\\','/')
        cursor.execute(sql)
        conn.commit()
        RESULTS[fname]['load_data'] = time.time() - start
        print('  load_data time:', RESULTS[fname]['load_data'])
    except Exception as e:
        RESULTS[fname]['load_data_error'] = str(e)
        print('  load_data failed:', e)

# write results
with open('c:\\Users\\ACER\\Desktop\\multi_file_benchmark_results.json','w',encoding='utf-8') as out:
    json.dump(RESULTS, out, indent=2)

cursor.close()
conn.close()
print('\nAll done. Results written to Desktop/multi_file_benchmark_results.json')