from graphviz import Graph
from graphviz import Digraph

def contador_elementos(lista, e):
   contador=0
   for i in lista:
      if i == e:
         contador+=1
   return contador

archivo=[]
nuevo_archivo=[]
codigo={"GCU":"A","GCC":"A","GCA":"A","GCG":"A","CGU":"R","CGC":"R","CGA":"R","CGG":"R","AGA":"R","AGG":"R","AAU":"N","AAC":"N",
        "GAU":"D","GAC":"D","UGU":"C","UGC":"C","CAA":"Q","CAG":"Q","GAA":"E","GAG":"E","GGU":"G","GGC":"G","GGA":"G","GGG":"G",
        "CAU":"H","CAC":"H","AUU":"I","AUC":"I","AUA":"I","UUA":"L","UUG":"L","CUU":"L","CUC":"L","CUA":"L","CUG":"L",
        "AAA":"K","AAG":"K","AUG":"M","UUU":"F","UUC":"F","CCU":"P","CCC":"P","CCA":"P","CCG":"P",
        "UCU":"S","UCC":"S","UCA":"S","UCG":"S","AGU":"S","AGC":"S","ACU":"T","ACC":"T","ACA":"T","ACG":"T","UGG":"W","UAU":"Y","UAC":"Y",
        "GUU":"V","GUC":"V","GUA":"V","GUG":"V","UAG":"STOP","UGA":"STOP","UAA":"STOP"}
dic={"CAU":"His","CGC":"Arg","GCU":"Ala","GCC":"Ala", "GCA":"Ala","GCC":"Ala", "CGU":"Arg", "GCG":"Arg", "CGA":"Arg", "CGG":"Arg", "AGA":"Arg",
    "AGG":"Arg", "AAU":"Asn", "AAC":"Asn", "GAU":"Asp", "GAC":"Asp", "UGU":"Cys", "UGC":"Cys", "CAA":"Gln","CAG":"Gln", "GAA":"Glu", "GAC":"Glu",
    "GGU":"Gly","GGC":"Gly","GGA":"Gly","GGG":"Gly", "GAU":"His", "CAC":"His",  "AUU":"He", "AUG":"He", "AUA":"He", "UUA":"Leu","UUG":"Leu","CUU":"Leu",
    "CUC":"Leu","CUA":"Leu","CUG":"Leu", "AAA":"Lys","AAG":"Lys", "AUG":"Met", "UUU":"Phe","UUC":"Phe", "CCU":"Pro","CCC":"Pro","CCA":"Pro","CCG":"Pro",
    "UCU":"Ser","UCC":"Ser","UCA":"Ser","UCG":"Ser","AGU":"Ser","AGC":"Ser", "ACU":"Thr","ACC":"Thr","ACA":"Thr","ACG":"Thr", "UGG":"Trp", "UAU":"Tyr","UAC":"Tyr",
    "GUU":"Val","GUC":"Val","GUA":"Val","GUG":"Val", "UAG":"STOP", "UGA":"STOP", "UAA":"STOP"}
print("MENÚ")
print("Ingrese 1 para leer archivo")
print("Ingrese 2 para obtener estádiscticas de secuencia")
print("Ingrese 3 para generar diagrama de relación")
print("Ingrese -1 para detener las operaciones")
a=int(input("Ingrese la opción que desea realizar: "))
while a!=-1:
    #Requerimiento1: Archivo entrada y salida
    if a==1:
        data=open(input("Ingrese el nombre el archivo: "))
 
        nombre=data.readlines(1)
        lineas=data.read()
        i=0
        while (i<len(lineas)):
            if lineas[i]=="I":
                while lineas[i]!="F":
                    i=i+1

            else:
                archivo.append(lineas[i])
            i = i+1

                    
        for j in range (len(archivo)): 
            if archivo[j] == "T":
                archivo[j]="U"
        print(archivo)                
        archivo ="".join(archivo)
        print(archivo)
        
        start=['AUG'] 
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
        ultima.append("M")
        i = 0
        while i < largo:
            if nuevo_archivo[i] in codigo:
                encontrar = codigo.get(nuevo_archivo[i])
                i+=1
                ultima.append(encontrar)
        print("".join(ultima))
        with open("secuencia_1_proteinas.txt","w") as f:
            f.write(nombre[0])
            f.write("".join(ultima))

    """Requerimiento2: Número de nucleotidos"""
    if a==2:
        contadorA=0
        contadorC=0
        contadorU=0
        contadorG=0
        largo=len(archivo)

        for i in archivo:
            if i=="A":
                contadorA=contadorA+1

            if i=="C":
                contadorC=contadorC+1

            if i=="U":
                contadorU=contadorU+1

            if i=="G":
                contadorG=contadorG+1

        porcentajeA=(contadorA*100)/largo
        porcentajeC=(contadorC*100)/largo
        porcentajeU=(contadorU*100)/largo
        porcentajeG=(contadorG*100)/largo
        print("El número de nucleotidos A es de ",contadorA," y el porcentaje es de ",porcentajeA)
        print("El número de nucleotidos C es de ",contadorC," y el porcentaje es de ",porcentajeC)
        print("El número de nucleotidos U es de ",contadorU," y el porcentaje es de ",porcentajeU)
        print("El número de nucleotidos G es de ",contadorG," y el porcentaje es de ",porcentajeG)

       
        """requerimiento2: Número de codones"""
        for i in nuevo_archivo:
            contador1=contador_elementos(nuevo_archivo, i)
            print("El codon ",i," y su porcentaje es de ",contador1," entre ",len(nuevo_archivo))
        
        """requerimiento2: Número de aminoacidos"""
        polares_sin_carga=0
        polares_positivos=0
        polares_negativos=0
        apolares=0
        polar_sin_carga=["S","T","C","Y","N","Q"]
        polar_positivo=["H","R","K"]
        polar_negativo=["D","E"]
        apolar=["G","A","V","L","I","F","W","M","P"]
       
        for i in ultima:
            if i in polar_sin_carga:
                polares_sin_carga=polares_sin_carga+1
            if i in polar_positivo:
                polares_positivos=polares_positivos+1
            if i in polar_negativo:
                polares_negativos=polares_negativos+1
            if i in apolar:
                apolares=apolares+1
        print("El número de aminoácidos polares sin carga es de ",polares_sin_carga)
        print("El número de aminoácidos polares positivos es de ",polares_positivos)
        print("El número de aminoácidos polares negativos es de ",polares_negativos)
        print("El número de aminoácidos apolares es de ",apolares) 
    if a==3:
        print(nuevo_archivo)
        g = Digraph('G', filename='grafico.gv',format='png')
        
        g.attr('node', shape='circle')
        g.edge("AUG", nuevo_archivo[0])
        for i in range (len(nuevo_archivo)-1):
            g.attr('node', shape='circle')
            g.edge(nuevo_archivo[i], nuevo_archivo[i+1])

        for i in range (len(nuevo_archivo)):
            g.attr('node', shape=('rectangle'))
            g.edge(nuevo_archivo[i], str(dic.get(nuevo_archivo[i])), color='red')


        g.attr('node', shape='circle')
        g.edge(nuevo_archivo[len(nuevo_archivo)-1], "STOP")
        g.view()

           
               
    
        
    a=int(input("Ingrese la operación que desea realizar: "))
