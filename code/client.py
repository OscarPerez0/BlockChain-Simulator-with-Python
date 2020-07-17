# Python program to implement client side of chat room.
import socket
import select
import sys
import curses 
import time
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
import csv
import os
from random import randint
from datetime import datetime
import hashlib
import json

###PROGRAMA MAIN




#Lista Simple recorridos

class NodoListaR:
    def __init__(self, carnet, nombre):
        self.carnet=carnet
        self.nombre=nombre
     
        
        
        self.siguiente= None
        self.anterior = None
class ListaRecorrido:
    def __init__(self):
        self.primero=None
        self.ultimo= None
        
    def vacia(self):
        if self.primero == None:
            return True
        else:
            return False
    
    def agregar(self,carnet, nombre):
        if self.vacia():
            self.primero = self.ultimo = NodoListaR(carnet, nombre)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = NodoListaR(carnet, nombre)
            self.ultimo.anterior = aux
        
    def imprimirINORDER(self):
        cadena=""
        aux= self.primero
        r= True
        contador = 1
        while aux!=None:
            
            cadena +="nodo"+ str(aux.carnet) +"[label= \"" +  str(aux.carnet) +"\n"+str(aux.nombre)+"\"];\n"
            cadena+= "\n"
            if(aux.siguiente):
                cadena +="nodo"+ str(aux.carnet)
                aux1 =aux.siguiente
                cadena+= "->"
                cadena +="nodo"+ str(aux1.carnet)
                cadena+= "\n"
            aux =aux.siguiente
         
        archivo=open('recorridoINORDER.dot', 'w')
        archivo.write('digraph G{\n   rankdir=LR;')
        archivo.write('subgraph cluster_0 {')
        archivo.write('style=filled; color=grey; node [style=filled,color=white]; \n')
        
        
        archivo.write(cadena)
        archivo.write('}')
        archivo.write('}')
        archivo.close() 
        os.system('dot -Tpng  recorridoINORDER.dot -o recorridoINORDER.png')
        os.system('recorridoINORDER.png')


    def imprimirPREORDER(self):
        cadena=""
        aux= self.primero
        r= True
        contador = 1
        while aux!=None:
            
            cadena +="nodo"+ str(aux.carnet) +"[label= \"" +  str(aux.carnet) +"\n"+str(aux.nombre)+"\"];\n"
            cadena+= "\n"
            if(aux.siguiente):
                cadena +="nodo"+ str(aux.carnet)
                aux1 =aux.siguiente
                cadena+= "->"
                cadena +="nodo"+ str(aux1.carnet)
                cadena+= "\n"
            aux =aux.siguiente
         
        archivo=open('recorridoPREORDER.dot', 'w')
        archivo.write('digraph G{\n   rankdir=LR;')
        archivo.write('subgraph cluster_0 {')
        archivo.write('style=filled; color=lightgrey; node [style=filled,color=white]; \n')
        
        
        archivo.write(cadena)
        archivo.write('}')
        archivo.write('}')
        archivo.close() 
        os.system('dot -Tpng  recorridoPREORDER.dot -o recorridoPREORDER.png')
        os.system('recorridoPREORDER.png')

    def imprimirPOSTORDER(self):
        cadena=""
        aux= self.primero
        r= True
        contador = 1
        while aux!=None:
            
            cadena +="nodo"+ str(aux.carnet) +"[label= \"" +  str(aux.carnet) +"\n"+str(aux.nombre)+"\"];\n"
            cadena+= "\n"
            if(aux.siguiente):
                cadena +="nodo"+ str(aux.carnet)
                aux1 =aux.siguiente
                cadena+= "->"
                cadena +="nodo"+ str(aux1.carnet)
                cadena+= "\n"
            aux =aux.siguiente
         
        archivo=open('recorridoPOSTORDER.dot', 'w')
        archivo.write('digraph G{\n   rankdir=LR;')
        archivo.write('subgraph cluster_0 {')
        archivo.write('style=filled; color=green; node [style=filled,color=white]; \n')
        
        
        archivo.write(cadena)
        archivo.write('}')
        archivo.write('}')
        archivo.close() 
        os.system('dot -Tpng  recorridoPOSTORDER.dot -o recorridoPOSTORDER.png')
        os.system('recorridoPOSTORDER.png')


#AVL

class NodoAVL():
    def __init__(self, carnet, nombre):
        self.carnet = carnet
        self.nombre= nombre
      
        #nodos
        self.izq = None 
        self.der = None 

class arbolAVL():
    def __init__(self, *args):
        self.nodoAvl = None 
        self.altura = -1  
        self.factorBalance = 0; 
        
       
        
    #altura            
    def altura(self):
        if self.nodoAvl: 
            return self.nodoAvl.altura 
        else: 
            return 0 
    
        #hoja
    def nodoHoja(self):
        return (self.altura == 0) 


    #insertar
    def insertarAVL(self, carnet,nombre):
        raizAVL = self.nodoAvl
        
        nodoAVLnuevo = NodoAVL(carnet,nombre)
            
        #print("carnetXXX: "+ carnet)
        if(raizAVL != None):
         #print("carnet111: "+raizAVL.carnet)
        
        if raizAVL == None:
            self.nodoAvl = nodoAVLnuevo 
            self.nodoAvl.izq = arbolAVL() 
            self.nodoAvl.der = arbolAVL()
           
       

        elif carnet < raizAVL.carnet: 
            self.nodoAvl.izq.insertarAVL(carnet,nombre)
            
        elif carnet > raizAVL.carnet: 
            self.nodoAvl.der.insertarAVL(carnet,nombre)
        if(raizAVL != None):
            if carnet== raizAVL.carnet: 
                print("FUUUUUCK")

        
        self.balancearAVL() 


        
    def balancearAVL(self):
        
        self.calculoAltura(False)
        self.calculoFactorBalance(False)

        while self.factorBalance < -1 or self.factorBalance > 1: 
            if self.factorBalance > 1:
                if self.nodoAvl.izq.factorBalance < 0:  
                    self.nodoAvl.izq.rotacionIzquierda() 
                    self.calculoAltura()
                    self.calculoFactorBalance()

                self.rotacionDerecha()
                self.calculoAltura()
                self.calculoFactorBalance()
                
            if self.factorBalance < -1:
                if self.nodoAvl.der.factorBalance > 0:  
                    self.nodoAvl.der.rotacionDerecha() 
                    self.calculoAltura()
                    self.calculoFactorBalance()

                self.rotacionIzquierda()
                self.calculoAltura()
                self.calculoFactorBalance()


            
    def rotacionDerecha(self):
         
        tmpR = self.nodoAvl 
        tmpIzq = self.nodoAvl.izq.nodoAvl 
        IzqDer = tmpIzq.der.nodoAvl 
        
        self.nodoAvl = tmpIzq 
        tmpIzq.der.nodoAvl = tmpR 
        tmpR.izq.nodoAvl = IzqDer 

    
    def rotacionIzquierda(self):
        
        tmpR = self.nodoAvl 
        tmpDer = self.nodoAvl.der.nodoAvl 
        DerIzq = tmpDer.izq.nodoAvl 
        
        self.nodoAvl = tmpDer 
        tmpDer.izq.nodoAvl = tmpR 
        tmpR.der.nodoAvl = DerIzq 
        
            
    def calculoAltura(self, calcular=True):
        if not self.nodoAvl == None: 

            if calcular: 
                if self.nodoAvl.izq != None: 
                    self.nodoAvl.izq.calculoAltura()

                if self.nodoAvl.der != None:
                    self.nodoAvl.der.calculoAltura()
            
            self.altura = max(self.nodoAvl.izq.altura,
                              self.nodoAvl.der.altura) + 1 
        else: 
            self.altura = -1 
            


    def calculoFactorBalance(self, calcular=True):
        if not self.nodoAvl == None: 

            if calcular: 
                if self.nodoAvl.izq != None: 
                    self.nodoAvl.izq.calculoFactorBalance()

                if self.nodoAvl.der != None:
                    self.nodoAvl.der.calculoFactorBalance()

            self.factorBalance = self.nodoAvl.izq.altura - self.nodoAvl.der.altura 
        else: 
            self.factorBalance = 0 

    

   

    #recorridos
        
    def InOrder(self):
        if self.nodoAvl == None:
            return [] 
        
        recorrido = [] 
        iz = self.nodoAvl.izq.InOrder()
        for nodo in iz : 
            recorrido.append(nodo) 

        recorrido.append(self.nodoAvl.carnet+'-'+self.nodoAvl.nombre)


        de = self.nodoAvl.der.InOrder()
        for nodo in de: 
            recorrido.append(nodo) 
    
        return recorrido

    def PostOrder(self ):
        if self.nodoAvl == None:
            return [] 
        
        recorrido = [] 
        iz = self.nodoAvl.izq.PostOrder()
        for no in iz: 
            recorrido.append(no) 

        
        de = self.nodoAvl.der.PostOrder()
        for no in de: 
            recorrido.append(no) 
        recorrido.append(self.nodoAvl.carnet+'-'+self.nodoAvl.nombre)
    
        return recorrido

    def PreOrder(self):
        if self.nodoAvl == None:
            return [] 
        
        recorrido = [] 
        recorrido.append(self.nodoAvl.carnet+'-'+self.nodoAvl.nombre)

        iz = self.nodoAvl.izq.PreOrder()
        for no in iz: 
            recorrido.append(no) 

        
        de = self.nodoAvl.der.PreOrder()
        for no in de: 
            recorrido.append(no) 
        
    
        return recorrido





    def imprimirDOT(self):
        
             
        
        cadena=''
        if(self.nodoAvl.izq.nodoAvl != None):
               
                cadena+= self.nodoAvl.carnet+"[label= \"Carne: " +  str(self.nodoAvl.carnet)+ "\n Nombre: " + str(self.nodoAvl.nombre) +"\n Altura: "+ str(self.altura)+ "\n FE: "+str(self.factorBalance)+ "\"];\n"
                cadena+=self.nodoAvl.izq.nodoAvl.carnet+"[label= \"Carne: " +  str(self.nodoAvl.izq.nodoAvl.carnet)+ "\n Nombre: " + str(self.nodoAvl.izq.nodoAvl.nombre) +"\n Altura: "+ str(self.nodoAvl.izq.altura)+ "\n FE: "+str(self.nodoAvl.izq.factorBalance)+"\"];\n"
                cadena+= self.nodoAvl.carnet +"->"+ self.nodoAvl.izq.nodoAvl.carnet +" [label=\"Iz\" color=\"dodgerblue\" ]"
                cadena+= self.nodoAvl.izq.imprimirDOT()
               

        if(self.nodoAvl.der.nodoAvl != None):
                
                cadena+= self.nodoAvl.carnet+"[label= \"Carne: " +  str(self.nodoAvl.carnet)+ "\n Nombre: " + str(self.nodoAvl.nombre) +"\n Altura: "+ str(self.altura)+ "\n FE: "+str(self.factorBalance)+ "\"];\n"
                cadena+=self.nodoAvl.der.nodoAvl.carnet+"[label= \"Carne: " +  str(self.nodoAvl.der.nodoAvl.carnet)+ "\n Nombre: " + str(self.nodoAvl.der.nodoAvl.nombre) +"\n Altura: "+ str(self.nodoAvl.der.altura)+ "\n FE: "+str(self.nodoAvl.der.factorBalance)+ "\"];\n"
                cadena+= self.nodoAvl.carnet +"->"+ self.nodoAvl.der.nodoAvl.carnet +" [label=\"De\" color=\"red\" ]"
                cadena+= self.nodoAvl.der.imprimirDOT()

            
        return cadena    
                
                
        
                   
               
    

    def graficarAVL(self):
        archivo=open('avl.dot', 'w')
        archivo.write('digraph G{\n')
        archivo.write("node [fontname=\"Arial\"];\n")
        
        archivo.write(avl.imprimirDOT())
        archivo.write('}')
        archivo.close() 
        os.system('dot avl.dot -o avl.png -Tpng ')
        os.system('avl.png')


#LISTA DOBLE



class NodoLDC():
   
    def __init__(self,index, tms, clase, data,  phash, hash):
        self.siguiente = None
        self.anterior = None
        self.index=index
        self.tms = tms
        self.clase = clase
        self.data = data
        self.phash = phash
        self.hash = hash
    def imprimirPantalla(self, bloque):
    	JSONENVIO ='{'\
    	'"INDEX":"'+bloque.index+'",\n'\
    	'"TIMESTAMP": "'+bloque.tms+'"\n,'\
    	'"CLASS": "'+bloque.clase+'"\n,'\
    	'"DATA": '+bloque.data+'\n,'\
    	'"PREVIOUSHASH": "'+bloque.phash+'",\n'\
    	'"HASH": "'+bloque.hash+'"\n'\
    	'}'
    	return JSONENVIO
       
    

class ListaDoble():

    def __init__(self):
        self.primero = None
        self.ultimo = None
        
    
    def vacia(self):
        if self.primero == None:
            return True
        else:
            return False
    def agregar(self, index, tms, clase, data, phash, hash):
        if self.vacia():
            self.primero = self.ultimo = NodoLDC(index, tms, clase, data,  phash, hash)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = NodoLDC(index, tms, clase, data,   phash, hash)
            self.ultimo.anterior = aux
        
    def imprimir(self):
        cadena=""
        aux= self.primero
        r= True
        contador = 1
        while aux!=None:
            
            cadena +="nodo"+ str(aux.index) +"[label= \"Class: "+str(aux.clase) +"\n TimeStamp: " +str(aux.tms)+ " \n PHASH: "+str(aux.phash) +"\n HASH: "+str(aux.hash)+"\"];\n"
            cadena+= "\n"
            if(aux.siguiente):
                cadena +="nodo"+ str(aux.index)
                aux1 =aux.siguiente
                cadena+= "->"
                cadena +="nodo"+ str(aux1.index)
                cadena+= "\n"
            if(aux.anterior):
                cadena +="nodo"+ str(aux.index)
                aux2 =aux.anterior
                cadena+= "->"
                cadena +="nodo"+ str(aux2.index)
                cadena+= "\n"
            aux =aux.siguiente
               
        
            
            
               
        
          
                
        archivo=open('blockchain.dot', 'w')
        archivo.write('digraph G{\n')
        archivo.write('subgraph cluster_0 {')
        archivo.write('style=filled; color=lightgrey; node [shape=box style=filled,color=white]; \n')
        
        
        archivo.write(cadena)
        archivo.write('}')
        archivo.write('}')
        archivo.close() 
        os.system('dot -Tpng  blockchain.dot -o blockchain.png')   
        


    
   

    def siguiente(self, user):

        
         
            
         return user.siguiente
    
    def anterior(self, user):

        
         
            
         return user.anterior
         
                   
            
     
        


   #GENERAL VARIABLES     
blockchain = ListaDoble()
avl= arbolAVL()

contadorBloques =0
hashg="0000"
ts =""
phash=""
hash=""
clasee=""
arboldata=""
ultimoHashInsertado='0000'



#MENU





def pintamenu(win):
    pintaTitulo(win,' BLOCKCHAIN ')          
                
    win.addstr(8,15, '2. SELECT BLOCK')      
    win.addstr(9,15, '3. REPORTS')   
    win.addstr(10,15, '')         
    win.addstr(11,15, '')    
    win.addstr(12,15, '6. SALIDA')           
    win.timeout(-1)             #ESPERA SALIDA 
def pintamenu2(win):
    pintaTitulo(win,' REPORTS ')          
                
    win.addstr(8,15, '1. BLOCKCHAIN REPORT')      
    win.addstr(9,15, '2. AVL REPORTS')   
    win.addstr(10,15, '')         
    win.addstr(11,15, '')    
    win.addstr(12,15, '6. SALIDA')           
    win.timeout(-1)             #ESPERA SALIDA           
    
def pintaTitulo(win,var):
    win.clear()                         
    win.border(0)                       
    xScreen = round((60-len(var))/2)    #mitad de pantalla
    win.addstr(0,xScreen,var)           

def esperaEspacio(win):
    key = ventana.getch()
    while key!=27:
        key = ventana.getch()

def rulS(us):
	if(blockchain.siguiente(us)):
		newuse = blockchain.siguiente(us)
		dato= newuse.index
		pintaTitulo(ventana, 'SELECCION BLOQUE .. ')
		ventana.addstr(2,5, '<<<<')
		ventana.addstr(3,2, 'INDEX:' +newuse.index)
		ventana.addstr(4,2,'TIMESTAMP:' +newuse.tms)
		ventana.addstr(5,2,'CLASS:' +newuse.clase)
		ventana.addstr(6,2,'HASH:' +newuse.hash)
		ventana.addstr(7,2,'PHASH:' +newuse.phash)
		ventana.addstr(8,2,'DATA:' +str(newuse.data)[:50])

		
		
		
		
		ventana.addstr(2,40, '>>>>')
    
def rulB(us):
	if(blockchain.anterior(us)  != None):
	    newuse = blockchain.anterior(us)
	    dato = newuse.index
	    pintaTitulo(ventana, 'SELECCION BLOQUE .. ')
	    ventana.addstr(2,5, '<<<<')
	    ventana.addstr(3,2, 'INDEX:' +newuse.index)
	    ventana.addstr(4,2,'TIMESTAMP:' +newuse.tms)
	    ventana.addstr(5,2,'CLASS:' +newuse.clase)
	    ventana.addstr(6,2,'HASH:' +newuse.hash)
	    ventana.addstr(7,2,'PHASH:' +newuse.phash)
	    ventana.addstr(8,2,'DATA:' +str(newuse.data)[:50])
	    ventana.addstr(2,40, '>>>>')


    ##RECORRER AVL EN JSON  IN ORDERinde
def avlmetodo(raiz):
    
    

    if(raiz['left']):
        avlmetodo(raiz['left'])

    
    val = raiz['value']
    x = val.split("-")
    car = x[0]
    nom = x[1]

    avl.insertarAVL(car,nom)
    
    if(raiz['right']):
        avlmetodo(raiz['right'])






###############clienteeeeeeee

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
	print ("Correct usage: script, IP address, port number")
	exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.connect((IP_address, Port))

tu =  'true'


##JSON
jas = '' #JSON RECIBIDO
jsonEnviado='' #bloque creado para enviar
jsonTrue=False
jsonCreado=False
BLOQUESELECCIONADO=''


bloquecorrecto = False

while True:


	read_sockets = select.select([server], [], [], 1)[0]
	import msvcrt
	if msvcrt.kbhit(): read_sockets.append(sys.stdin)

	for socks in read_sockets:
		if socks == server:
			message = socks.recv(2048)
			
			
			#print (message.decode('utf-8'))
			deco = message.decode('utf-8')
			if deco!='Welcome to [EDD]Blockchain Project!':
				if(deco!='true' and deco != 'false'):
					deco = message.decode('utf-8')
					#print(deco)
					try:
						print('\n-CADENA JSON correcto-')
						
						jas = json.loads(deco)
						#print(jas)
						jsonTrue = True
						jsonCreado=False

						cadena256 = (jas['PREVIOUSHASH'])
						print('\n-PHSASH-: '+cadena256)
						
						if(blockchain.vacia()):
							ultimoHashInsertado ='0000'
						else:
							ultimoHashInsertado=blockchain.ultimo.hash


						if(str(cadena256) == str(ultimoHashInsertado)):
							print('--BLOQUECORRECTO--')
							texto_a_enviar = 'true'

							#texto_a_enviar = 'asdf'
							server.sendall(texto_a_enviar.encode('utf-8'))
							sys.stdout.write("<You>")
							sys.stdout.write(texto_a_enviar)
							sys.stdout.flush()
							#bloquecorrecto==True
						else:
							texto_a_enviar = 'false'

							#texto_a_enviar = 'asdf'
							server.sendall(texto_a_enviar.encode('utf-8'))
							sys.stdout.write("<You>")
							sys.stdout.write(texto_a_enviar)
							sys.stdout.mflush()



						
					except:
						print('\n--JSON INCORRECTO--')
						#print(deco)
						jas=''
					continue

				elif(deco=='true'):
						print('\n--Se recibio un true del servidor para agregar')
						#se agrega el mensaje JSON
						if(jsonTrue == True and jsonCreado==False):
							
							
							print('si hay json que agregar')
							contadorBloques=contadorBloques+1 
							indJ =jas['INDEX']
							tmJ=jas['TIMESTAMP']
							dataJ= jas['DATA']
							hashJ=jas['HASH']
							phashJ=jas['PREVIOUSHASH']
							classJ=jas['CLASS']

							blockchain.agregar(indJ, tmJ, classJ, dataJ, phashJ, hashJ)
							blockchain.imprimir()
							os.system('blockchain.png')	






							
						
							
						elif(jsonCreado == True and jsonTrue==False):
									print('no hay Json, JsonCreado desde aqui')
									je = json.loads(jsonEnviado)
									#contadorBloques=contadorBloques+1 
									indJ =je['INDEX']
									tmJ=je['TIMESTAMP']
									dataJ= je['DATA']
									hashJ=je['HASH']
									phashJ=je['PREVIOUSHASH']
									classJ=je['CLASS'] 

									blockchain.agregar(indJ, tmJ, classJ, dataJ,phashJ, hashJ)
									blockchain.imprimir()
									os.system('blockchain.png')	

 

				elif(deco=='false'):
					print('\n--Se recibio un FALSE NO HACE NADA')
					 #se agrega el mensaje JSON
					




					
				

		else:

			print('>>>-----------MENU---------------<<<')
			print('>>>--1.Ingresar Bloque-------<<<')
			print('>>>--2.Seleccionar Bloque-------<<<')
			print('>>>--3.Reportes-------<<<')
			opcion=str(input()) 

			if(opcion=='1'):
				print('>>>--nombre de archivo-------<<<')
				archivocsv = ''
				archivocsv =str(input()) 
				if(archivocsv!=''):
						now = datetime.now().strftime("%d-%m-%y::%H:%M:%S")
						archivo = open("bloques/"+archivocsv)
						reader = csv.reader(archivo,delimiter=',')
						for linea in reader:
							if(linea[0] =="class" or linea[0] =="CLASS"):
								clasee=str(linea[1])
							elif(linea[0] =="data" or linea[0] =="DATA"):
								arboldata=str(linea[1])
				             
				                #print (arbolj)
						if(blockchain.vacia()):
							phash="0000"
						else:
							phash=blockchain.ultimo.hash


						contadorBloques=contadorBloques+1 
						cadenaFUN = (str(contadorBloques)+str(now)+str(clasee)+str(arboldata)+str(phash)).encode("utf-8")
						hash = hashlib.new("sha256", cadenaFUN)
						hash = hash.hexdigest()
						print("\n---FUNCION256  "+str(hash))

			        	#json para enviar
						JSONENVIO ='{'\
						'"INDEX":"'+str(contadorBloques)+'",'\
						'"TIMESTAMP": "'+str(now)+'",'\
						'"CLASS": "'+clasee+'",'\
						'"DATA": '+arboldata+','\
						'"PREVIOUSHASH": "'+str(phash)+'",'\
						'"HASH": "'+str(hash)+'"'\
						'}'
						#print(JSONENVIO)
						jsonEnviado =JSONENVIO
						jsonCreado = True
						jsonTrue = False


						texto_a_enviar = jsonEnviado

						#texto_a_enviar = 'asdf'
						server.sendall(texto_a_enviar.encode('utf-8'))
						sys.stdout.write("<You>")
						sys.stdout.write(texto_a_enviar)
						sys.stdout.flush()

			elif(opcion=='2'):
					stdscr = curses.initscr() 
					ventana = curses.newwin(20,100,0,0)  
					ventana.keypad(True)     
					        
					curses.curs_set(0)      #sin cursor
					pintamenu(ventana)      

					keystroke = -1
					while(keystroke==-1):
						
					    keystroke = ventana.getch()  
					    
					    if(keystroke==50):  ##ruleta 
					    	if(blockchain.vacia()):
					    		pintaTitulo(ventana, ' BLOQUES DE BLOCKCHAIN ')

					    		ventana.addstr(3,5, 'VACIO')
					    		esperaEspacio(ventana)
					    		pintamenu(ventana)
					    		keystroke=-1
					    	else:
					    		us =blockchain.primero
					    		dato = us.index
					    		pintaTitulo(ventana, ' BLOQUES DE BLOCKCHAIN ')
					    		ventana.addstr(2,5, '<<<<')
					    		ventana.addstr(3,2, 'INDEX:' +us.index)
					    		ventana.addstr(4,2,'TIMESTAMP:' +us.tms)
					    		ventana.addstr(5,2,'CLASS:' +us.clase)
					    		ventana.addstr(6,2,'HASH:' +us.hash)
					    		ventana.addstr(7,2,'PHASH:' +us.phash)
					    		ventana.addstr(8,2,'DATA:' +str(us.data)[:50])
					    		ventana.addstr(2,40, '>>>>')
					    		keystroke = ventana.getch()
					    		while  keystroke != 27:
					    			key = ventana.getch()
					    			if( key==KEY_RIGHT):
					    				if(us.siguiente):
					    					rulS(us)
					    					us = us.siguiente
					    					dato = us.index
					    				
					    				
					    			if( key==KEY_LEFT):
					    				if(us.anterior):
					    					rulB(us)
					    					us = us.anterior
					    					dato = us.index
					    				
					    				
					    			if( key==KEY_DOWN):
					    				BLOQUESELECCIONADO=us
					    				break
					    				
					    		ventana.addstr(1,10, 'bloque seleccionado: '+BLOQUESELECCIONADO.clase)
					    		esperaEspacio(ventana)
						    	pintamenu(ventana)
						    	keystroke=-1
						  
					    elif(keystroke==51):  #Reportes
					        pintaTitulo(ventana, ' REPORTS ')

					        ventana.addstr(5,5, '1. BLOCKCHAIN REPORT') 
					        ventana.addstr(6,5, '2. REPORTES AVL')  
					        keystroke = ventana.getch()
					        
				        	key = ventana.getch()

					        if(keystroke==49):
					        	pintaTitulo(ventana, ' BLOCKCHAIN EN PANTALLA')
					        	os.system('blockchain.png')
					        	esperaEspacio(ventana)
				        		pintamenu2(ventana)
				        		keystroke=-1
					        elif(keystroke==50):
					        	avl =arbolAVL()
					        	recorridoInOrden = ListaRecorrido()
					        	recorridoPostOrden = ListaRecorrido()
					        	recorridopreOrden = ListaRecorrido()
					        	pintaTitulo(ventana, ' REPORTES AVL')
					        	ventana.addstr(1,1, 'RECORRIDOS')
					        	archivoAVL = str(BLOQUESELECCIONADO.data)
					        	archivoAVL = archivoAVL.replace("\'", "\"")
					        	archivoAVL = archivoAVL.replace("None", "null")
					        	print(archivoAVL)
					        	re =json.loads(archivoAVL)
					        	avlmetodo(re)
					        	arbolNuevo = arbolAVL()
					        	arbolNuevo= avl
					        	avl.graficarAVL()
					        	arbolNuevo.graficarAVL()

					        	ino = avl.InOrder()
					        	inoC = 'INICIO-> '
					        	for no in ino:
					        		valin = no.split("-")
					        		carin = valin[0]
					        		nomin = valin[1]
					        		recorridoInOrden.agregar(carin, nomin)
					        		inoC+=no+' -> '
					        	inoC+= "FIN"
					        	ventana.addstr(3,2, '---------INORDEN:--------')
					        	ventana.addstr(4,2, inoC) 
					        	recorridoInOrden.imprimirINORDER()
					        	#postorden

					        	pso =avl.PostOrder()
					        	psoC = 'INICIO-> '
					        	for nop in pso:
					        		valp = nop.split("-")
					        		carp = valp[0]
					        		nomp = valp[1]
					        		recorridoPostOrden.agregar(carp, nomp)
					        		psoC+=nop+' -> '
					        	psoC+= "FIN"
					        	ventana.addstr(7,2, '-------POSTORDEN:----------')
					        	ventana.addstr(8,2, psoC) 
					        	recorridoPostOrden.imprimirPOSTORDER()
					        	#PREORDEN
					        	preo=avl.PreOrder()
					        	preoC = 'INICIO-> '
					        	for nopr in preo:
					        		valpr = nopr.split("-")
					        		carpr = valpr[0]
					        		nompr = valpr[1]
					        		recorridopreOrden.agregar(carpr, nompr)
					        		preoC+=nopr+' -> '
					        	preoC+= "FIN"
					        	ventana.addstr(11,2, '------PREORDEN:-------')
					        	ventana.addstr(12,2, preoC) 
					        	recorridopreOrden.imprimirPREORDER()
					        	esperaEspacio(ventana)
				        		pintamenu2(ventana)
				        		keystroke=-1
					        esperaEspacio(ventana)
				        	pintamenu(ventana)
				        	keystroke=-1
						    

					        



					        
					    elif(keystroke==53): #
					       pass
					    elif(keystroke==54):
					        pass
					    else:
					        keystroke=-1

					curses.endwin()





server.close()
