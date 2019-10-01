n=int(input())
#arr=input().split()#['2','54','67','5','5','4']
res = list(map(int, input().split()))#for number
print(max([res.count(i) for i in res]))
