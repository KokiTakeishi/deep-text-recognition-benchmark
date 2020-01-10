gtFile = './train/gt.txt'

with open(gtFile, 'r', encoding='utf-8') as data:
    datalist = data.readlines()

nSamples = len(datalist)

labels = '0123456789abcdefghijklmnopqrstuvwxyz'

for i in range(nSamples):
    imagePath, label = datalist[i].strip('\n').split()
    print(imagePath + ":" + label)
    labels += label


from collections import OrderedDict

unique_str = ''.join(OrderedDict.fromkeys(labels))

# print(unique_str)

f = open('char_list.txt', 'w')

f.write(unique_str)
 
f.close()

with open('char_list.txt', 'r', encoding='utf-8') as data:
    datalist = data.readlines()

print(datalist)