chave=True
cadeado=True
l1=[1,2,3,4,5,6,7,8,9,0]
l2=[1,2,3,4,5,6,7,8,9,0]
l3=[1,2,3,4,5,6,7,8,9,0]
tl1=0
tl2=0
tl3=0
v1=1
v2=1
v3=1
v4=tl1,tl2,tl3
def linhas():
    global esc
    if esc==3:
        return ["linha 3:",l3,tl3]
    elif esc==2:
        return ["linha 2:",l2,tl2]
    elif esc==1:
        return ["linha 1:",l1,tl1]
    elif esc==-1:
        esc=3
        return ["linha 3:",l3,tl3]
    elif esc==4:
        esc=1
        return ["linha 1:",l1,tl1]
def numero(atual):
    if atual==9:
        atual=0
    elif atual==-1:
        atual=8
    return atual
def salva(esc,tela):
    global tl1,tl2,tl3
    if esc==1:
        tl1=tela
    elif esc==2:
        tl2=tela
    elif esc==3:
        tl3=tela
fechado=False
esc=3
print(v4)
print("senha inicial 1 1 1")
while True:
    nome,num,tela=linhas()
    print(f"{nome}{num[tela]}")
    mudar=input().upper()
    if mudar=="W":
        esc=esc+1
    elif mudar=="S":
        esc=esc-1
        if esc==0:
            esc=-1
    elif mudar=="A":
        tela=tela-1
        tela=numero(tela)
        salva(esc,tela)
    elif mudar=="D":
        tela=tela+1
        tela=numero(tela)
        salva(esc,tela)
    elif mudar=="E" and chave==True and fechado==False and v4==(tl1,tl2,tl3):
        print("Senha certa")
        print("[E] para fecha o cadeado")
        fechado=True
    elif mudar=="E" and chave==True and fechado==True:
        print("Cadeado fechado")
        v4=tl1,tl2,tl3
        print(tl1,tl2,tl3)
        fechado=False
    elif mudar=="E" and chave==True and fechado==False and v4!=(tl1,tl2,tl3):
        print("fechado")