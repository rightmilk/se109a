per_result = []
def per(lst,s,e):
    if s == e:
        per_result.append(list(lst))
    else:
        for i in range(s,e):
            lst[i],lst[s] = lst[s],lst[i]
            per(lst,s+1,e)#遞迴
            lst[i],lst[s] = lst[s],lst[i]

def shear(lst):
    result = 0
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if(abs(lst[j] - lst[i]) == abs(j-i)):
                result += 1
    if(result > 0):
        return True
    else:
        return False

def stamp(st):
    for i in st:
        for j in range(len(i)):
            a = ("."*(i[j]-1)+"#"+"."*(len(i)-i[j]))
            print(a,"\t")
        print(" ")
num = eval(input("請輸入皇后的個數："))
lst = [i+1 for i in range(num)]
per(lst,0,num)
queen_lst = []
for i in per_result:
    if(shear(i) == False):
        queen_lst.append(i)
stamp(queen_lst)
print("共{:d}種可能".format(len(queen_lst)))