size = [5,7,300,90,24,50,75]
print('Hello, my name is Hiep and these are my sheep sizes',size)

print('Now my biggest sheep has size',max(size),'let shear it')

for i in range(len(size)):
    if size[i]==max(size):
        size[i]=8
        break
print('After shearing, here is my flock',size)
j=0
while j<3:
    j += 1
    print('MONTH',j,':')
    for i in range(len(size)):
        size[i]=size[i]+50
    print('One month has passed, now here is my flock',size)
    print('Now my biggest sheep has size',max(size),'let shear it')

    for i in range(len(size)):
        if size[i]==max(size):
            size[i]=8
            break
        if j==3:
            break
    print('After shearing, here is my flock',size)
sum=sum(size)
print('My flock has size in total:',sum)
money=sum*2
print('I would get',sum,'*',2,'$','=',money,'$')
