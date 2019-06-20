from pattern.es import parse,split
from pattern.web import Wiktionary
import sys
import PySimpleGUI as sg

def agregar_reporte1 (pal):
    with open('noCoinciden.txt','a+') as a:
        a.write("La clasificacion de la palabra {0} usando Wiktionary no coincide con la obtenida en pattern.es ".format(pal)+'\n')

def agregar_definicion(cadena,pal):
	with(open('definiciones.txt','a+'))as b:
		b.write("{0}: {1}".format(pal,cadena)+'\n')
def buscarTipo(cadena,lista):
	num=999999
	for i in range(len(lista)):
		if(cadena == lista[i]):
			num=i
		elif(cadena in lista[i]):
			num=i
	return num

def clasificar_palabra(pal,lis_5):
	w = Wiktionary(language="es")
	if(pal != ""):
		p=w.search(pal,cached=False)
		s = parse(pal).split()
		#definicion de pattern.es
		defp=s[0][0][1]
		pos2=buscarTipo(defp,lis_tipo2)
		try:
			#definicion de WIKTIONARY
			defw=(p.sections[3].title.split())[0]
			pos1=buscarTipo(defw,lis_tipo1)
			for i in range(len(lis_5)):
				if(pos1==i):
					if(pos2!=pos1):
						agregar_reporte(pal)
					if(pal not in lis_5[i]):
						lis_5[i].append(pal)
		except:
			i=0
			ok=True
			for i in range(len(lis_5)):
				if(pos2==i):
					if(pal not in lis_5[i]):
						lis_5[i].append(pal)
						ok=False
			if(not ok):
				layout2=[
					    [sg.Text("Ingrese la definicion de la palabra {0} :".format(pal))],
						[sg.Input()],
						[sg.Button("Agregar")]
						]
				window2=sg.Window("Definicion").Layout(layout2)
				event2,values2=window2.Read()
				if(event2 is None):
					window2.Close()
				elif(event2=="Agregar"):
					agregar_definicion(values2[0],pal)
					window2.Close()
	return lis_5

def eliminar_palabra(cadena,lis_5,lis_tipo1):
	i=0
	for i in range(len(lis_5)):
		if(cadena in lis_5[i]):
			lis_5[i].remove(cadena)
			sg.Popup("Se elimino un "+lis_tipo1[i])
	return lis_5
			
def configurar(lis_5,lis_tipo1):
	layout=[
	       [sg.Text('Ingrese palabras (de a una) con los signos correspondientes.     Nota: Se require tener conexion a internet.')],
	       [sg.Input(do_not_clear=False)],
	       [sg.Button('Agregar'),sg.Button('Eliminar')],
	       [sg.Button('Listo')] ]
	window = sg.Window('Ingreso de palabras.').Layout(layout)
	while True:
		event,values=window.Read()
		if event is None:
			break
		elif event == 'Agregar':
			if(values[0] == ""):
				sg.Popup('Ingresa una palabra')
			else:
				lis_5=clasificar_palabra(values[0],lis_5)
		elif event == 'Eliminar':
			if(values[0] == ""):
				sg.Popup('Ingresa una palabra')
			else:
				lis_5=eliminar_palabra(values[0],lis_5,lis_tipo1)
		elif event == 'Listo':
			break

palabras_predefinidas=["jaula","hielo","arbol","fuego","cuaderno","agua"]
lis_tipo1=['Sustantivo','Adjetivo','Verbo','Adverbio','Conjuncion']
lis_tipo2=[
         ['NN','NNS','NNP','NNPS'],              #Sustantivo
         ['JJ','JJR','JJS'],                     #Adjetivo
         ['VB','VBZ','VBP','VBD','VBN','VBG'],   #Verbo
         ['RB','RBR','RBS'],                     #Adverbio
         ['IN']                                  #Conjuncion
        ]
colores=['red','black','white','green','blue','yeloow','purple','pink','orange']
lis_sust=[]
lis_adje=[]
lis_verbo=[]
lis_adver=[]
lis_conj=[]
lis_5=[]
lis_5=[lis_sust,lis_adje,lis_verbo,lis_adver,lis_conj]
configurar(lis_5,lis_tipo1)
