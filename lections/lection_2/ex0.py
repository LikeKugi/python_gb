# a - add data - add data to current file
# r - read data
# w - write data - create new file or clear file and write data

colors = ['red', 'green', 'blue']
data = open('file.txt','w')
data.writelines(colors)
data.close()

with open('file.txt','a') as ouf:
    for _ in range(5):
        ouf.write(f'{_}\n')