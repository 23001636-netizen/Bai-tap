import zipfile, bz2, csv
zpath = r'D:/New folder (3)/archive.zip'
out = r'C:/Users/ACER/Desktop/train_sample_1M.csv'
count_target = 1000000
written = 0
with zipfile.ZipFile(zpath,'r') as z:
    name = 'train.ft.txt.bz2'
    with z.open(name) as entry:
        with bz2.BZ2File(entry) as f, open(out,'w',encoding='utf-8',newline='') as outcsv:
            w = csv.writer(outcsv)
            for line in f:
                if written==0:
                    w.writerow(['text'])
                try:
                    row = line.decode('utf-8','ignore').rstrip('\n')
                except:
                    row = line.decode('latin1','ignore').rstrip('\n')
                w.writerow([row])
                written += 1
                if written % 100000 == 0:
                    print('written', written)
                if written >= count_target:
                    break
print('done', written)
