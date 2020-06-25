l1 = [1,2,39,5,3]
toplam=0
for i in l1:
    toplam = toplam +i
    print(i)
print(toplam) 

for x in range(5):
    print(x)
    
l2=list(range(15,2,-2))
print(l2)

#CONTINUE
for x in list(range(1,20)):
    if(x%3==0):
        continue
    print(x)
#BREAK
for x in list(range(1,20)):
    if(x%3==0):
        break
    print(x)    

print("new line")

#PASS
while True:
    pass

