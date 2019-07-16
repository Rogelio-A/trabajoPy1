from pattern.es import parse,split
from pattern.web import Wiktionary
import PySimpleGUI as sg

def agregar_reporte1 (pal):
    with open('noCoinciden.txt','a+') as a:
        a.write("La clasificacion de la palabra {0} usando Wiktionary no coincide con la obtenida en pattern.es ".format(pal)+'\n')

def agregar_definicion(cadena,pal):
	with(open('definiciones.txt','a+'))as b:
		b.write("{0}: {1}".format(pal,cadena)+'\n')

#Busqueda en el diccionario		
def buscar_tipo1(cadena,dic_tipo1):
	for clave in (list(dic_tipo1.keys())):
		if(clave==cadena):
			return clave

#Busqueda en la lista				
def buscar_tipo2 (cadena,lista):
	num=9999								
	for i in range(len(lista)):
		if(cadena in lista[i]):
			num=i
	return num

def clasificar_palabra(pal,dic_tipo1,lis_tipo2):
	w = Wiktionary(language="es")
	ok=False
	for clave in (list(dic_tipo1.keys())):
		if (pal in dic_tipo1[clave]):
			ok=True
			sg.Popup(pal+' ya fue ingresada')
	if(not ok):
		p=w.search(pal,cached=False)
		s = parse(pal).split()
		#definicion de pattern.es
		defp=s[0][0][1]
		posL=buscar_tipo2(defp,lis_tipo2)
		try:
			#definicion de WIKTIONARY
			defw=(p.sections[3].title.split())[0]
			claveD=buscar_tipo1(defw,dic_tipo1)
			for i in range(len((list(dic_tipo1.keys())))):
				if(posL==i):
					if(posL!=i):
						agregar_reporte(pal)
					if(pal not in dic_tipo1[claveD]):
						dic_tipo1[claveD].append(pal)
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
	return dic_tipo1

def eliminar_palabra(cadena,dic_tipo1):
	i=0
	for i in (list(dic_tipo1.keys())):
		if(cadena in dic_tipo1[i]):
			dic_tipo1[i].remove(cadena)
			sg.Popup("Se elimino un "+i)
	return dic_tipo1

def cantidad_palabras(dic_tipo1):
	dic_cant={}
	for clave in (list(dic_tipo1.keys())):
		dic_cant[clave]=len(dic_tipo1[clave])
	return dic_cant
			
def configurar():
	dic_tipo1={
		  'Sustantivo':[],
		  'Adjetivo':[],
		  'Verbo':[]
		  }
	lis_tipo2=[
					['NN','NNS','NNP','NNPS'],              #Sustantivo
					['JJ','JJR','JJS'],                     #Adjetivo
					['VB','VBZ','VBP','VBD','VBN','VBG'],   #Verbo
					]
	pedirPalabra=[
							[sg.InputText(key='palabra',do_not_clear=False)]
							]
	color_pal = [
					[sg.Text('Color Sustantivos: '), sg.Input(change_submits=True, size=(10,1), do_not_clear=True, key='ColorSus'), sg.ColorChooserButton('Elegir', target=(sg.ThisRow, -1))],
					[sg.Text('Color Adjetivos:     '), sg.Input(change_submits=True, size=(10,1), do_not_clear=True, key='ColorAdj'), sg.ColorChooserButton('Elegir', target=(sg.ThisRow, -1))],
					[sg.Text('Color Verbos:        '), sg.Input(change_submits=True, size=(10,1), do_not_clear=True, key='ColorVer'), sg.ColorChooserButton('Elegir', target=(sg.ThisRow, -1))]
				]
				
	layout=[
				[sg.Text('Configuracion (Parte 1/2)', size=(50, 1), justification='center', font=('arial', 16,))],
				[sg.Frame('Ingrese palabras (de a una) con los signos de correspondientes.	Nota: Se requiere conexion a internet.',pedirPalabra)],
				[sg.Button('Agregar'),sg.Button('Eliminar')],
				[sg.Text('')],
				[sg.Frame('Color de los tipos de palabras', color_pal)],
				[sg.Checkbox('Habilitar boton de ayuda',key='ayuda')],
				[sg.Button('Siguiente Parte')]
				]
	
	window = sg.Window('Ingreso de palabras.').Layout(layout)
	while True:
		boton,values=window.Read()
		if boton is None:
			break
		elif boton == 'Agregar':
			if(values['palabra'] == ""):
				sg.Popup('Ingresa una palabra')
			else:
				palabra1=values['palabra']
				if not palabra1.isalpha():
					sg.Popup(palabra1 + ' no es una palabra.')
				else:
					dic_tipo1=clasificar_palabra(palabra1,dic_tipo1,lis_tipo2)
				
		elif boton == 'Eliminar':
			palabra1=values['palabra']
			if(palabra1 == ""):
				sg.Popup('Ingresa una palabra')
			else:
				dic_tipo1=eliminar_palabra(palabra1,dic_tipo1)
		elif boton == 'Siguiente Parte':
			dic_cant=cantidad_palabras(dic_tipo1)
			window.Hide()
			layout2=[
				[sg.Text('Configuracion (Parte 2/2)', size=(50,1), justification='center', font=('arial',16))],
				[sg.Text('Elija para cada tipo de palabra la cantidad que desea que este en la sopa de letras')],
				[sg.Text('Cantidad de sustantivos', font=('arial',12)), sg.Slider(range=(0, dic_cant['Sustantivo']), change_submits=True,orientation='h', size=(34, 20), default_value=0, key='cSus')],
				[sg.Text('Cantidad de adjetivos', font=('arial',12)), sg.Slider(range=(0, dic_cant['Adjetivo']),change_submits=True, orientation='h', size=(34, 20), default_value=0,key='cAdj')],
				[sg.Text('Cantidad de verbos', font=('arial',12)), sg.Slider(range=(0,dic_cant['Verbo']),change_submits=False, orientation='h', size=(34, 20), default_value=0, key='cVer')],
				[sg.Button('Listo')]
				]
			window2=sg.Window('Elegir cantidad').Layout(layout2)
			while True:
				boton2,values2=window2.Read()
				if boton2 is None:
					break
				elif boton2 is 'Listo':
					break
			Cpalabras_elegidas={}
			Cpalabras_elegidas['Sustantivos']=int(values2['cSus'])
			Cpalabras_elegidas['Adjetivos']=int(values2['cAdj'])
			Cpalabras_elegidas['Verbos']=int(values2['cVer'])
			break
	colores={}
	colores['Sustantivo']=values['ColorSus']
	colores['Adjetivo']=values['ColorAdj']
	colores['Verbo']=values['ColorVer']
	ayuda=values['ayuda']
	print(dic_tipo1)
	print(Cpalabras_elegidas)
	print(colores)
	print(ayuda)
	return (dic_tipo1,Cpalabras_elegidas,colores,ayuda)
if __name__=='__main__':
	configurar()
