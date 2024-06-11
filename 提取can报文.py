#f = open('ecu_can_log.asc', 'r')
#f1 = open ('result.txt', 'w')
with open('ecu_can_log.asc', 'r') as f, open('result', 'wb') as f1:

    list1 = f.readlines()

    data=[]
    count=1

    for i in list1:
        if(count%19 == 0):
            data=i[43:57]
        elif(count%19 == 1):
            data=i[52:63]
        else:
            data=i[43:63]
        data = bytes.fromhex(data)
        f1.write(data)
        count+=1