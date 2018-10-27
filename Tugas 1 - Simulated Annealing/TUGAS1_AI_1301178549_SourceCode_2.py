import math
import random

#inisiasi nilai start x_1 dan x_2 diambil secara 'suka-suka'
x_1 = 1
x_2 = -1

def f_0(x_1,x_2):
    return -abs(math.sin(x_1)*math.cos(x_2)*math.exp(abs(1-math.sqrt(x_1**2+x_2**2)/math.pi)))

e_0 = f_0(x_1,x_2)
print(e_0)

t = 1000

#BSF berupa array yang berisi nilai x1 dan x2
BSF = [x_1,x_2]

#men-generate nilai x_1_baru dan x_2_baru dari nilai x_1 dan x_2
#x_1_baru dan x_2_baru diusahakan agar tidak pernah melebihi batas maksimal dan minimal

def generateXBaru(x_1,x_2):
    x_1_baru = x_1+random.random()
    if x_1_baru > 10:
        x_1_baru = -10
        
    x_2_baru = x_2-random.random()
    if x_2_baru < -10:
        x_2_baru = 10
        
    return (x_1_baru,x_2_baru)
	
x_1_baru,x_2_baru = generateXBaru(x_1,x_2)
print(x_1_baru,x_2_baru)

def f_0(x_1_baru,x_2_baru):
    return -abs(math.sin(x_1_baru)*math.cos(x_2_baru)*math.exp(abs(1-math.sqrt(x_1_baru**2+x_2_baru**2)/math.pi)))
	
print(x_1_baru,x_2_baru)

e_1 = f_0(x_1_baru,x_2_baru)
delta_e = e_1-e_0

print(e_1)
print(delta_e)

x1_curr = x_1
x2_curr = x_2
e_curr = e_0
i=1
while t>0 :
    x_1_baru,x_2_baru = generateXBaru(x1_curr,x2_curr)
    e_1 = f_0(x_1_baru,x_2_baru)
    delta_e = e_1-e_curr
    e_bsf = f_0(BSF[0],BSF[1])
    if delta_e<0 :
        e_curr = e_1
        if e_curr < e_bsf :
            BSF=[x_1_baru,x_2_baru]
    else :
        def f_P(delta_e,t):
            return math.exp(-delta_e/t)
        P = f_P(delta_e,t)
        r = random.random()
        if r < P:
            e_curr = e_1
    x1_curr = x_1_baru 
    x2_curr = x_2_baru
    #print(i,') x1_curr = ',x1_curr,' x2_curr = ',x2_curr)
    print('     BSF = ',BSF,' E_BSF = ',e_bsf)
    i+=1
    t-=0.1
	
#print nilai x1 dan x2 yang tersimpan sebagai BSF setelah hasil perulangan 
print(BSF)

#print nilai Energy BSF
print(e_bsf)