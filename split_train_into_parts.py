import zipfile, bz2, csv

ZIP_PATH = r'D:/New folder (3)/archive.zip'
ENTRY = 'train.ft.txt.bz2'
OUT_DIR = r'C:/Users/ACER/Desktop'
PART_LINES = 1200000
PART_COUNT = 3

out_paths = [f"{OUT_DIR}/train_part{i+1}.csv" for i in range(PART_COUNT)]
written = 0
current_part = 0
fouts = [open(p, 'w', encoding='utf-8', newline='') for p in out_paths]
writers = [csv.writer(fouts[i]) for i in range(PART_COUNT)]
for w in writers:
    w.writerow(['text'])

try:
    with zipfile.ZipFile(ZIP_PATH,'r') as z:
        with z.open(ENTRY) as entry:
            with bz2.BZ2File(entry) as f:
                for line in f:
                    if current_part >= PART_COUNT:
                        break
                    try:
                        row = line.decode('utf-8','ignore').rstrip('\n')
                    except:
                        row = line.decode('latin1','ignore').rstrip('\n')
                    writers[current_part].writerow([row])
                    written += 1
                    if written % PART_LINES == 0:
                        print(f'Completed part {current_part+1} with {PART_LINES} lines')
                        current_part += 1
    print('Done. Total written lines:', written)
finally:
    for f in fouts:
        f.close()
