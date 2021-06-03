import fileinput
for line in fileinput.FileInput("samplecontent.txt", inplace=True):
    line=line.replace("four","new")
    print(line,end="")

print("Inplace editing completed")