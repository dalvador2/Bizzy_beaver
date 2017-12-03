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

def run_beaver(tape,instruction,beaver_position,current_card,reps):
    for i in range(reps):
        if current_card==0:
            break
        value=tape[beaver_position]
        tape[beaver_position]=instruction[current_card][value][0]
        if instruction[current_card][value][1]==0:
            beaver_position=beaver_position-1
        else:
            beaver_position+=1
        current_card=instruction[current_card][value][2]
    return tape,instruction,beaver_position,current_card
file=open("input.txt","r")
instruction_array=txt_array(file)
tape=[]
card_no=1
for i in range(1000):
    tape.append(0)
beaver_position=500
tape,instruction_array,beaver_position,card_no=run_beaver(tape,instruction_array,beaver_position,card_no,10000)

