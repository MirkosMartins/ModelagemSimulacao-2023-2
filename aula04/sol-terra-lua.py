Web VPython 3.2
def calculaY(corpoCentral,coordx,raio):
    return sqrt(pow(raio,2)
    -pow(coordx-corpoCentral.pos.x,2))
    +corpoCentral.pos.y
    
def distancia(corpo1,corpo2):
    return sqrt(pow(corpo2.pos.x-corpo1.pos.x,2)+
    pow(corpo2.pos.y-corpo1.pos.y,2)+
    pow(corpo2.pos.z-corpo1.pos.z,2))
    
planeta = sphere(pos=vector(0,0,0),radius=1)
lua = sphere(pos=vector(-5,0,0),radius=0.2,make_trail=True)

#corpo1=corpo central, corpo2 quem orbita
def orbita(corpo1,corpo2):
    raio = distancia(corpo1,corpo2)
    extremosX = [corpo1.pos.x-raio,corpo1.pos.x+raio]
    fator = 1
    while True:
        rate(10)
        if corpo2.pos.x==extremosX[0]:
            fator=1
        if corpo2.pos.x==extremosX[1]:
            fator=-1
        corpo2.pos.x = corpo2.pos.x+1*fator
        if fator>0:
            corpo2.pos.y = calculaY(corpo1,corpo2.pos.x,raio)
        else:
            mmx = corpo1.pos.y+raio
            valor = mmx - calculaY(corpo1,corpo2.pos.x,raio)
            mix = corpo1.pos.y-raio
            corpo2.pos.y = mix+valor
        print(corpo2.pos.x,corpo1.pos.x+raio)
        
sol = sphere(pos=vector(10,10,0),radius=2.5)
orbita(planeta,lua)
