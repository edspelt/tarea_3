from colorama import Fore, Back, init
init(autoreset=True)
def cambio_chaco(altura, unidad_medida):
    ''' funcion para convertir la altura a cm, recibira la altura y la unidad de medida 
        @param altura: la altura que se recibe para convertir a m
        @param unidad_medida: la unidad de medida para convertir
        @return altura_m la altura en m
    '''
    if unidad_medida=='m':
        altura_m= altura
    elif unidad_medida=='cm':
        altura_m=altura/100
    elif unidad_medida=='dm':
        altura_m=altura/10
    elif unidad_medida=='mm':
        altura_m=altura/1000
    elif unidad_medida=='ft':
        altura_m=altura/39.37
    elif unidad_medida=='in':
        altura_m=altura/3.281
    return altura_m

def cambio_peso (peso,um):
    '''Funcion para convertir el peso a Kg, recibira el pego y la unidad de medidas separados por un espacio
    @param peso: El peso que se recibe para convertir a KG
    @param um: la unidad de medida  para convertir
    @return peso_um: el peso en KG'''
    if um=='g':
        peso_um=peso/1000
    elif um=='lb':
        peso_um=peso*2.205
    elif um=='kg':
        peso_um=peso
    elif um=='oz':
        peso_um=peso/35.274
    elif um=='t':
        um==peso/0.001
    return peso_um

def calc_imc (altura, peso):
    '''Funcion que calcula el Indice de masa corporal,
    @param altura= recibe la altura en Metros
    @param peso recibe el peso en kg
    @return none '''
    calc=peso//altura**2
    print ('su indice de Masa corporal es de: ',calc)
    if calc < 18.5:
        print (Fore.BLUE+'Peso inferior al normal')
    elif calc >18.5 and calc <=24.9:
        print (Fore.GREEN+'peso Normal')
    elif calc >24.9 and calc<=29.9:
        print(Fore.YELLOW+'Peso Superior al Normal')
    elif calc>29.9:
        print(Fore.RED+'Obesidad')
        
# calculo de la altura
altura=input('Ingrese su altura con unidad de medida correspondiente separada por un espacio: ')
peso= input('ingrese su peso con unidad de medida separada de un espacio: ')
altura, unidad_medida= altura.split(' ')
altura= cambio_chaco(float(altura),unidad_medida)
# calculo del peso
peso, um=peso.split(' ')
peso=cambio_peso(float(peso),um)
print('su peso es :', peso, type(peso))
print('su altura es :',altura, type(altura))
calc_imc(altura,peso)




