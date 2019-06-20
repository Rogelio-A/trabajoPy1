from pattern.es import parse,split
from pattern.web import Wiktionary
import sys
import PySimpleGUI as sg

def buscarTipo(cadena,lista):
	num=999999
	for i in range(len(lista)):
		if(cadena == lista[i]):
			num=i
		elif(cadena in lista[i]):
			num=i
	return num

def clasificar_palabras(lis_sust,lis_adje,lis_verbo,lis_adver,lis_conj):
	pal=input('Ingrese una palabra: ')
	while(pal!='Terminar'):
		p=w.search(pal,cached=False) #CAMBIAR A FALSE
		try:
			#definicion de WIKTIONARY
			defw=(p.sections[3].title.split())[0]
			pos1=buscarTipo(defw,lis_tipo1)
			s = parse(pal).split()
			defp=s[0][0][1]
			pos2=buscarTipo(defp,lis_tipo2)
			if(pos1==0):
				if(pos2!=pos1):
					agregar_reporte(pal)
				if(pal not in lis_sust):
					lis_sust.append(pal)
			elif(pos1==1):
				if(pos2!=pos1):
					agregar_reporte(pal)
				if(pal not in lis_adje):
					lis_adje.append(pal)
			elif(pos1==2):
				if(pos2!=pos1):
					agregar_reporte(pal)
				if(pal not in lis_verbo):
					lis_verbo.append(pal)
			elif(pos1==3):
				if(pos2!=pos1):
					agregar_reporte(pal)
				if(pal not in lis_adver):
					lis_adver.append(pal)
			elif(pos1==4):
				if(pos2!=pos1):
					agregar_reporte(pal)
				if(pal not in lis_conj):
					lis_conj.append(pal)
		except:
			if(pos2==0):
				if(pal not in lis_sust):
					lis_sust.append(pal)
			elif(pos2==1):
				if(pal not in lis_adje):
					lis_adje.append(pal)
			elif(pos2==2):
				if(pal not in lis_verbo):
					lis_verbo.append(pal)
			elif(pos2==3):
				if(pal not in lis_adver):
					lis_adver.append(pal)
			pedido="Ingresar definicion de palabra {0} :".format(pal)
		pal=input('Ingrese una palabra: ')
	return(lis_sust,lis_adje,lis_verbo,lis_adver,lis_conj)

w = Wiktionary(language="es")
palabras_predefinidas=["jaula","hielo","arbol","fuego","cuaderno","agua"]

#print(help(w))
#print("ingrese una palabra: ")
lis_tipo1=['Sustantivo','Adjetivo','Verbo','Adverbio','Conjuncion']
lis_tipo2=[
         ['NN','NNS','NNP','NNPS'],              #Sustantivo
         ['JJ','JJR','JJS'],                     #Adjetivo
         ['VB','VBZ','VBP','VBD','VBN','VBG'],   #Verbo
         ['RB','RBR','RBS'],                     #Adverbio
         ['IN']                                  #Conjuncion
        ]
pal="casa"

#print(dir(p))
print('##############')
lis_sust=[]
lis_adje=[]
lis_verbo=[]
lis_adver=[]
lis_conj=[]

print(lis_sust)
print(lis_adje)
print(lis_verbo)
