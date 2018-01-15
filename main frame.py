import csv
temp = input("Please fill in the SKU:")
isku = str(temp)
pblogger = input("Please fill in the blogger name:")
pblogger = str(pblogger)
csvproduct = open('A1P.csv')
gc = csv.reader(csvproduct)
for line in gc:
    if not line:
        break
    if isku in line[2]:
        ptitle = line[1]
        pprice = line[3]
        plink = 'www.beautybigbang.com/products/'+line[0]
        f = open("post.txt", "a")
        f.write(ptitle+"."+"@"+pblogger+"(ins).")
        f.write('\n')
        f.write('$'+pprice+' '+'Free worldwide shipping!')
        f.write('\n')
        f.write(plink)
        f.write('\n')
        f.write('#'+isku+' '+'#'+"BeautyBigBangCom")
        f.write('\n')
        f.write('\n')
        f.close()
        break
