import csv

fh=open('content.csv','w')

csvdata=[['ID', 'Name', 'mark1', 'mark2', 'mark3'],['11', 'bagath', '180', '187','180'],['22', 'vimal', '187', '150', '180'],['33', 'mithun', '190', '195', '195']]

writer=csv.writer(fh,delimiter=":")

writer.writerow(['a','b','c',1,2,3])

writer.writerows(csvdata)

fh=open('content.txt','r')

reader=csv.reader(fh,delimiter=":")

for row in reader:
  for cell in row:
    print(cell,end=" ")
  print()