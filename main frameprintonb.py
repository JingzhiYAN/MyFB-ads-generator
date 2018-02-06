import csv

isku = "A1"
while isku != "exit":
    temp = input("Please fill in the SKU:")
    isku = str(temp)
    if isku == "exit":
        assert 1 > 2
    csvproduct = open('A1P.csv')
    gc = csv.reader(csvproduct)
    for line in gc:
        if isku in line[2]:
            ptitle = line[1]
            pprice = line[3]
            break
    pblogger = input("Please fill in the blogger name:")
    pblogger = str(pblogger)
    picturenumber = input("please fill in the picture number:")
    picturenumber = int(picturenumber)
    bloggerversion = input("Please fill in the blogger version(1,2):")
    bloggerversion = int(bloggerversion)
    if bloggerversion == 1:
        lb = "(ins)."
    else:
        lb = "(blog)."
    if picturenumber == 1:
        plink = 'www.beautybigbang.com/products/' + line[0]
        f = open("post.txt", "a")
        print(ptitle + "." + "@" + pblogger + lb)
        print('$' + pprice + ' ' + 'Use code ' + 'FOREVERLOVE10' + ' to get another 10% off!!')
        print("View more>>> "+plink)
        print('#' + isku + ' ' + '#' + "BeautyBigBangCom")
        print('\n')
        f.write(ptitle + "." + "@" + pblogger + lb)
        f.write('\n')
        f.write('$' + pprice + ' ' + 'Use code ' + 'FOREVERLOVE10' + ' to get another 10% off!!')
        f.write('\n')
        f.write('Click the picture to buy!')
        f.write('\n')
        f.write('#' + isku + ' ' + '#' + "BeautyBigBangCom")
        f.write('\n')
        plink = 'www.beautybigbang.com/products/' + line[0]
        f.write(plink)
        f.write('\n')
        f.write('\n')
        f.close()
    else:
        f = open("post.txt", "a")
        print(ptitle + "." + "@" + pblogger + lb)
        print('$' + pprice + ' ' + 'Use code ' + 'FOREVERLOVE10' + ' to get another 10% off!!')
        print('Click the picture to buy!')
        print('#' + isku + ' ' + '#' + "BeautyBigBangCom")
        print('\n')
        plink = 'www.beautybigbang.com/products/' + line[0]
        print(plink)
        f.write(ptitle + "." + "@" + pblogger + lb)
        f.write('\n')
        f.write('$' + pprice + ' ' + 'Use code ' + 'FOREVERLOVE10' + ' to get another 10% off!!')
        f.write('\n')
        f.write('Click the picture to buy!')
        f.write('\n')
        f.write('#' + isku + ' ' + '#' + "BeautyBigBangCom")
        f.write('\n')
        plink = 'www.beautybigbang.com/products/' + line[0]
        f.write(plink)
        f.write('\n')
        f.write('\n')
        f.close()
