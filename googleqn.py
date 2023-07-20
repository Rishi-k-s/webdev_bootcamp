
getNum = int(input("ENter number"))
strGetArry = input("ENter Array")

ArrGetArray = list(strGetArry)
print(ArrGetArray)

for each_elem in range(len(ArrGetArray)):
    if(int(ArrGetArray[1])+int(ArrGetArray[each_elem])== getNum):
        print(getNum)