from pattern.es import parse,split
from pattern.web import Wiktionary
import sys
w = Wiktionary(language="es")
palabras_predefinidas=["jaula","hielo","arbol","fuego","cuaderno","pantalla","agua"]

#print(help(w))
#print("ingrese una palabra: ")
lisTipo1=['Sustantivo','Adjetivo','Verbo','Adverbio','Conjuncion']
lisTipo2=[
         ['NN','NNS','NNP','NNPS'],              #Sustantivo
         ['JJ','JJR','JJS'],                     #Adjetivo
         ['VB','VBZ','VBP','VBD','VBN','VBG'],   #Verbo
         ['RB','RBR','RBS'],                     #Adverbio
         ['IN']                                  #Conjuncion
        ]
pal="casa"
p=w.search(pal,cached=True) #CAMBIAR A FALSE
#print(dir(p))
print('##############')
lisSust=[]
lisAdje=[]
lisVerbo=[]
lisAdver=[]

def buscarTipo(cadena,lista):
	num=999999
	for i in range(len(lista)):
		if(cadena == lista[i]):
			num=i
		elif(cadena in lista[i]):
			num=i
	return num
try:
	
	#definicion de WIKTIONARY
	defw=(p.sections[3].title.split())[0]
	pos1=buscarTipo(defw,lisTipo1)
	s = parse(pal).split()
	defp=s[0][0][1]
	pos2=buscarTipo(defp,lisTipo2)
	if(pos1==pos2==0):
		lisSust.append(pal)
	elif(pos1==pos2==1):
		if(pal not in lisAdje):
			lisAdje.append(pal)
	elif(pos1==pos2==2):
		if(pal not in lisVerbo):
			lisVerbo.append(pal)
	elif(pos1==pos2==3):
		if(pal not in lisAdver):
			lisAdver.append(pal)		             
except:
	None
print(lisSust)
#try:
#except:
#print('La palabra no existe')
print()
