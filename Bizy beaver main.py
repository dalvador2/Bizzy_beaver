def txt_array(file):
    lines=0
    for line in file:
        lines+=1
    array=[]
    array.append(1)
    for i in range(round(lines/4)):
        array.append([])
    file.seek(0)
    counter=0
    for line in file:
        if counter==0:
            card_no=int(line[5])
        elif counter in [1,2]:
            subarray=line.split(" ")
            subarray=list(map(int,subarray))
            array[card_no].append(subarray)
        else:
            pass
        counter=(counter+1)%4
    return array
        
file=open("input.txt","r")
array=txt_array(file)
print(array)
