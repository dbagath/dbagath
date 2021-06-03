import collections

lst1=[2,3,4,5,6,7,8,3,5,7,9]

dupl=collections.defaultdict(int)

print(dupl)

for i in lst1:
  dupl[i]+=1

print(dupl)

lst1=[22,55,33,11,44]

lst1.append(66)
lst1[2]=333

print(lst1)


dict1={"one":11,"two":22,"three":33}
dict2={"four":44,"five":55,"six":66}
dict1.update(dict2)

print(dict1)

tup1=(11,22,33,44)
tup2=("one","two","three","four")

tup3=('python',) * 3

del tup3

print(max(tup1))

a = [1, 2, 3, 4, 5, 9]
b = [9, 8, 7, 6, 5]

c = [x for x in a if x in b]

print(c)

seen=set([1,1,3,4,4,5])
print(seen)
