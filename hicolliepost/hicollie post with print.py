import csv

ihandle = "A1"
while ihandle != "exit":
    temp = input("Please fill in the Product handle:")
    ihandle = str(temp)
    if ihandle == "exit":
        assert 1 > 2
    csvproduct = open('Hicollie.csv')
    gc = csv.reader(csvproduct)
    for line in gc:
        if ihandle in line[0]:
            ptitle = line[1]
            pprice = line[3]
            psku = line[2]
            break
    picturenumber = input("please fill in the picture number:")
    picturenumber = int(picturenumber)
    if picturenumber == 1:
        plink = 'www.hicollie.com/products/' + line[0]
        f = open("post.txt", "a")
        print(ptitle + ".")
        print('$' + pprice + ' ' + 'Free 5-7days delivery!')
        print("View more>>> "+plink)
        print('#' + psku + ' ' + '#' + "hicollieCom")
        print('\n')
        f.write(ptitle + ".")
        f.write('\n')
        f.write('$' + pprice + ' ' + 'Free 5-7days delivery!')
        f.write('\n')
        f.write('Click the picture to buy!')
        f.write('\n')
        f.write('#' + psku + ' ' + '#' + "hicollieCom")
        f.write('\n')
        plink = 'www.hicollie.com/products/' + line[0]
        f.write(plink)
        f.write('\n')
        f.write('\n')
        f.close()
    else:
        f = open("post.txt", "a")
        print(ptitle + ".")
        print('$' + pprice + ' ' + 'Free 5-7days delivery!')
        print('Click the picture to buy!')
        print('#' + psku + ' ' + '#' + "hicollieCom")
        print('\n')
        plink = 'www.hicollie.com/products/' + line[0]
        print(plink)
        f.write(ptitle + ".")
        f.write('\n')
        f.write('$' + pprice + ' ' + 'Free 5-7days delivery!')
        f.write('\n')
        f.write('Click the picture to buy!')
        f.write('\n')
        f.write('#' + psku + ' ' + '#' + "hicollieCom")
        f.write('\n')
        plink = 'www.hicollie.com/products/' + line[0]
        f.write(plink)
        f.write('\n')
        f.write('\n')
        f.close()
