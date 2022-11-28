# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 11:18:47 2022

@author: monpa
"""
archivo=[]
nuevo_archivo=[]

codigo={"GCU":"A","GCC":"A","GCA":"A","GCG":"A","CGU":"R","CGC":"R","CGA":"R","CGG":"R","AGA":"R","AGG":"R","AAU":"N","AAC":"N",
        "GAU":"D","GAC":"D","UGU":"C","UGC":"C","CAA":"Q","CAG":"Q","GAA":"E","GAG":"E","GGU":"G","GGC":"G","GGA":"G","GGG":"G",
        "CAU":"H","CAC":"H","AUU":"I","AUC":"I","AUA":"I","UUA":"L","UUG":"L","CUU":"L","CUC":"L","CUA":"L","CUG":"L",
        "AAA":"K","AAG":"K","AUG":"M","UUU":"F","UUC":"F","CCU":"P","CCC":"P","CCA":"P","CCG":"P",
        "UCU":"S","UCC":"S","UCA":"S","UCG":"S","AGU":"S","AGC":"S","ACU":"T","ACC":"T","ACA":"T","ACG":"T","UGG":"W","UAU":"Y","UAC":"Y",
        "GUU":"V","GUC":"V","GUA":"V","GUG":"V","UAG":"STOP","UGA":"STOP","UAA":"STOP"}
print("MENÚ")
print("Ingrese 1 para leer archivo")
print("Ingrese 2 para obtener estádiscticas de secuencia")
print("Ingrese 3 para generar diagrama de relación")
print("Ingrese -1 para detener las operaciones")
a=int(input("Ingrese la opción que desea realizar: "))
while a!=-1:
    """Requerimiento1: Archivo entrada y salida"""
    if a==1:     ### Aquí intento borrar las partes del archivo de I a F ###
        data=open(input("Ingrese el nombre del archivo: "))
        nombre = data.readlines(1)
        lineas=data.read()

        i=0
        while (i<len(lineas)):
            if lineas[i]=="I":
                while lineas[i]!="F":
                    i=i+1

            else:
                archivo.append(lineas[i])
            i = i+1
            print(archivo)
                    
        for j in range (len(archivo)): ### Aquí intento cambiar las T por U ###
            if archivo[j] == "T":
                archivo[j]="U"
        print(archivo)                
        archivo ="".join(archivo)
        print(archivo)
        
        start=['AUG'] ### Aquí comienzo a contar del AUG ###
        stop =["UAG","UGA","UAA"]
        larg_archivo=len(archivo)
        i=0
        while (i<larg_archivo-2):
            if start[0]==archivo[i:i+3]:
                i=i+3

                while (i+3)<=len(archivo):

                    if stop[0] == archivo[i:i+3] or  stop[1] == archivo[i:i+3] or  stop[2] == archivo[i:i+3]:
                        i = i+larg_archivo     
                    else:
                        nuevo_archivo.append(archivo[i:i+3])
                        i=i+3
                        print(nuevo_archivo)


            i=i+1
        ultima = []
        largo = len(nuevo_archivo)
        i = 0
        while i < largo:
            if nuevo_archivo[i] in codigo:
                encontrar = codigo.get(nuevo_archivo[i])
                i+=1
                ultima.append(encontrar)

        fin = "".join(ultima)
        print(fin)
    """Requerimiento2: Número de nucleotidos"""
    if a==2:
        contadorA=0
        contadorC=0
        contadorU=0
        contadorG=0
        for i in nuevo_archivo:
            if i=="A":
                contadorA=contadorA+1
            if i=="C":
                contadorC=contadorC+1
            if i=="U":
                contadorU=contadorU+1
            if i=="G":
                contadorG=contadorG+1
            porcentajeA=len(nuevo_archivo)/contadorA
            porcentajeC=len(nuevo_archivo)/contadorC
            porcentajeU=len(nuevo_archivo)/contadorU
            porcentajeG=len(nuevo_archivo)/contadorG
        print("El número de Adenina es de ",contadorA," y su porcentaje es de ",porcentajeA)
        print("El número de Citocina es de ",contadorC," y su porcentaje es ",porcentajeC)
        print("El número de Uracilo es de ",contadorU," y su porcentaje es de ",porcentajeU)
        print("El número de Guanina es de ",contadorG," y su porcentaje es de",porcentajeG)
        """requerimiento2: Número de codones"""
        contador_codones=0
        for i in nuevo_archivo:
            i=i+3
            contador_codones=contador_codones+1
            porcentaje_codones=len(nuevo_archivo)/contador_codones
        print("El número de codones es ",contador_codones," y el porcentaje es de ",porcentaje_codones)
        """requerimiento2: Número de aminoacidos"""
        polares_sin_carga=0
        polares_positivos=0
        polares_negativos=0
        apolares=0
        aminoacidos={"S":"polar sin carga","T":"polar sin carga","C":"polar sin carga","Y":"polar sin carga","N":"polar sin carga","Q":"polar sin carga",
                     "H":"polar positivo","R":"polar positivo","K":"polar positivo","D":"polar negativo","E":"polar negativo",
                     "G":"apolar","A":"apolar","V":"apolar","L":"apolar","I":"apolar","F":"apolar","W":"apolar","M":"apolar","P":"apolar"}
        for i in nuevo_archivo:
            for j in aminoacidos:
                if i==j:
                    c=dict.get(j)
                    if c=="polar sin carga":
                        polares_sin_carga=polares_sin_carga+1
                    if c=="polar positivo":
                        polares_positivos=polares_positivos+1
                    if c=="polar negativo":
                        polares_negativos=polares_negativos+1
                    if c=="apolares":
                        apolares=apolares+1
    
        
    a=int(input("Ingrese la operación que desea realizar: "))
