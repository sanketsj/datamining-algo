from itertools import combinations
global listofdata
global step1support
global supported
stepsupport = {}
listofdata = {}
supp={}


def inptdataset():
    filepath = 'input.txt'
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            listofdata[cnt] = line.strip().split(',')
            line = fp.readline()
            cnt += 1
    #print(listofdata)

def find(*fitem):
    itmcount = 0
    for i in range(2,len(listofdata)+1):
        temp = 0
        for j in range(0,len(fitem)):
            if fitem[j] in listofdata[i]:
                temp += 1
        if temp == len(fitem):
            itmcount += 1
    return itmcount


def combin(grupof,*supported):
    combos = [
        x for x in combinations(*supported, grupof)
    ]
    return combos

def apriory(support):
    inptdataset()
    supp = listofdata[1]
    for stap in range(1,5):
        y=combin(stap, supp)
        for x in y:
            i = find(*x)
            if i >= support:
                stepsupport[x] = i
        print(stepsupport)


apriory(3)
