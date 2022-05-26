def lavadora():
     # 'Casa' es las locaciones en donde se encuentran la lavadora 
    Casa = input("Casa donde de encuentra la lavadora : \n  Playa, Campo, Cuidad \n")
    #Se pide el estado de la lavadora 
    Estado = int(input("Ingrese estado de la lavadora : "))
    #Se le asigana un numero a cada estado de la lavadora 
    lava = 1
    centrifuga = 2
    Seca=3

    if lava == 1 : # si la lava es igual a 1 
        print("Desea lavar la ropa  " + Casa) #imprima si desea lavar la ropa 
        decide = input(" si / no\n") #decide Si o No 
        if decide == 'si': # si decide si entonces del estado aumentara un cost 
            cost = str(Estado + lava) # aumenta un costo 
            print("Se lavo ropa de Casa de: "+Casa) # finaliza e imprime que la ropa se lavo 
            print("El proceso de lavado finalizado en :"+cost)#proceso de lavado termina 
        else: # caso contrario 
            print("no se lavo la ropa de casa de :"+Casa) # no se lava la ropa y concatenamos el nombre de la casa 
            print("El proceso de lavado a finalizado en :"+cost) #proceso finaliza y suma el cost

    if centrifuga == 2 : #si centrifuga es igual a 2
        print("Desea centrigurgar la ropa de casa de :  " + Casa)# imprima si desea centrifugar
        decide  = input(" si / no\n")#Afirma si se desea centrifugar 
        if decide  == 'si': # si la decision es si 
            cost = str(Estado  + centrifuga)# el estado aumenta su costo 

            print("se centrifugo  " + Casa) #imprime que ya centrifugo y concatena con la casa 
            print("El proceso de centrifugado  finalizo en :"+cost)#termina el proceso y aumenta el cost
        else: #caso contrario :
            print("no se lavo la ropa de casa de"+Casa)# imprime que no lavo concatenado con la casa 
            print("El proceso de centrifugado a finalizo en :"+cost) #termina el proceso de centrifugado 

    if Seca == 3 : # si seca es igual a 3 
        print("Desea secar la ropa de casa de :  " + Casa) # imprimir + concatena casa
        decide  = input(" si / no\n") # pregunta si se desea secar la ropa 
        if decide  == 'si': #si decide si entonces 
            cost = str(Estado  + Seca) #aunmentara un costo 

            print("se  seco la ropa  de casa de :" + Casa) # lava la ropa 
            print("La lavadora termino sus procesos:"+cost) # termina el proces y concatena el cost
        else:
            print("no se lavo la ropa de casa de: "+ Casa) # no lava la ropa
            print("La lavadora termino sus proceso  :"+cost) # termina el proceso y concatena el cost al finalizar 
      
lavadora()