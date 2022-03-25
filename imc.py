def run():
   
    um= int(input ("""
                Elija opcion de forma de medida
                1. Kilogramos y Metros
                2. Libras y Pulgadas
                """))
    if um == 1 :
        altura_metro=float(input('Favor ingrese su altura en metros: '))
        peso_kg=float (input('Favor ingrese su peso en kg: '))
        print ('su indice de masa musular es: ')
        calc=peso_kg//altura_metro**2
        print (calc)
        if calc < 18.5:
            print ('Peso inferior al normal')
        elif calc >18.5 and calc <=24.9:
            print ('peso NOrmal')
        elif calc >24.9 and calc<=29.9:
            print('Peso SUperior al Normal')
        else:
            print('Obesidad')

    elif um==2:   
        estatura=float(input('Favor ingrese su altura en Pulgadas: '))
        peso=float (input('Favor ingrese su peso en Libras: '))
        print ('su indice de masa muscular es: ')
        calc=peso/estatura**2
        calc2=calc*703
        print (calc2)
        if calc2 < 18.5:
            print ('Peso inferior al normal')
        elif calc2 >18.5 and calc2 <=24.9:
            print ('peso NOrmal')
        elif calc2 >24.9 and calc2<=29.9:
            print('Peso SUperior al Normal')
        else:
            print('Obesidad')



if __name__ == '__main__':
    run()