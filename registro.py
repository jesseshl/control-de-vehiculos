from tkinter import *
from tkinter import messagebox
import sqlite3







#--------------Funciones----------------
def conexionBBDD():
	miConexion=sqlite3.connect("Vehiculos")

	miCursor=miConexion.cursor()
	
	try:
		miCursor.execute('''
			CREATE TABLE DATOSVEHICULOS(
    		ID INTEGER PRIMARY KEY,
			PLACA VARCHAR(6),
			FECHA INTEGER(10),
			MARCA VARCHAR(50),
			AÑO INTEGER(4),
			COLOR VARCHAR(50),
			TIPO VARCHAR(50),
			NOMBRE VARCHAR(50),
			CEDULA NUMERIC(8),
			DESTINOINICIAL VARCHAR(50),
			DESTINOFINAL VARCHAR(50),
			COMBUSTIBLE REAL(5),
			MONTOCOMBUSTIBLE REAL(5),
			VIATICO REAL(10),
			GASTOS REAL(10),
			KILOMETRAJEINICIAL NUMERIC(20),
			KILOMETRAJEFINAL NUMERIC(20),
			COMENTARIO VARCHAR (100))
			''')

		messagebox.showinfo("BBDD","BBDD creada con éxito")

	except:
		messagebox.showwarning("¡Atención!", "La base de datos ya existe")

def salirAplicacion():
	valor=messagebox.askquestion("Salir","¿Desea salir de la aplicación?")

	if valor=="yes":
		root.destroy()

def limpiarCampos():
	miId.set("")

	miPlaca.set("")

	miFecha.set("")
	
	miMarca.set("")
	
	miAño.set("")
	
	miColor.set("")

	miTipo.set("")

	miNombre.set("")

	miCedula.set("")

	miDestinoInicial.set("")

	miDestinoFinal.set("")

	miCombustible.set("")

	miMontoCombustible.set("")

	miViatico.set("")

	miGastos.set("")

	miKilometrajeInicial.set("")

	miKilometrajeFinal.set("")
	
	textoComentario.delete(1.0,END)

def crear():
	miConexion=sqlite3.connect("Vehiculos")

	miCursor=miConexion.cursor()

	datos=miPlaca.get(),miFecha.get(),miMarca.get(),miAño.get(),miColor.get(),miTipo.get(),miNombre.get(),miCedula.get(),miDestinoInicial.get(),miDestinoFinal.get(),miCombustible.get(),miMontoCombustible.get(),miViatico.get(),miGastos.get(),miKilometrajeInicial.get(),miKilometrajeFinal.get(),textoComentario.get("1.0", END)
	
	miCursor.execute("INSERT INTO DATOSVEHICULOS VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(datos))

	miConexion.commit()

	messagebox.showinfo("BBDD", "Registro insertado con éxito")

def leer():
	miConexion=sqlite3.connect("Vehiculos")
	miCursor=miConexion.cursor()

	miCursor.execute("SELECT * FROM DATOSVEHICULOS WHERE ID=" + miId.get())
	elUsuario=miCursor.fetchall()

	for usuario in elUsuario:

		miId.set(usuario[0])
		miFecha.set(usuario[1])
		miPlaca.set(usuario[2])
		miMarca.set(usuario[3])
		miAño.set(usuario[4])
		miColor.set(usuario[5])
		miTipo.set(usuario[6])
		miNombre.set(usuario[7])
		miCedula.set(usuario[8])
		miDestinoInicial.set(usuario[9])
		miDestinoFinal.set(usuario[10])
		miCombustible.set(usuario[11])
		miMontoCombustible.set(usuario[12])
		miViatico.set(usuario[13])
		miGastos.set(usuario[14])
		miKilometrajeInicial.set(usuario[15])
		miKilometrajeFinal.set(usuario[16])
		textoComentario.insert(1.0,usuario[17])
	
	miConexion.commit()

def actualizar():
	miConexion=sqlite3.connect("Vehiculos")

	miCursor=miConexion.cursor()

	datos=('''
		miPlaca.get(),
		miFecha.get(),
		miMarca.get(),
		miAño.get(),
		miColor.get(),
		miTipo.get(),
		miNombre.get(),
		miCedula.get(),
		miDestinoInicial.get(),
		miDestinoFinal.get(),
		miCombustible.get(),
		miMontoCombustible.get(),
		miDestino.get(),
		miViatico.get(),
		miGastos.get(),
		miKilometrajeInicial.get(),
		miKilometrajeFinal.get(),
		textoComentario.get("1.0", END)
		''')

	
	miCursor.execute("UPDATE DATOSVEHICULOS SET PLACA=?,AÑO=?,MARCA=?,FECHA=?,COLOR=?,TIPO=?,NOMBRE=?,CEDULA=?,DESTINOINICIAL=?,DESTINOFINAL=?,COMBUSTIBLE=?,MONTOCOMBUSTIBLE=?,VIATICO=?,GASTOS=?,KILOMETRAJEINICIAL=?,KILOMETRAJEFINAL=?,COMENTARIO=?" + 
		"WHERE ID=" + miId.get(),(datos))
	
	
	miConexion.commit()

	messagebox.showinfo("BBDD","Registro actualizado con éxito")

def eliminar():

	miConexion=sqlite3.connect("Vehiculos")

	miCursor=miConexion.cursor()

	#datos=miPlaca.get(),miAño.get(),miMarca.get(),miSerial.get(),miColor.get(),textoComentario.get("1.0", END)

	miCursor.execute("DELETE FROM DATOSVEHICULOS WHERE ID=" + miId.get())


	miConexion.commit()

	messagebox.showinfo("BBDD","Registro borrado con éxito")


root=Tk()
root.title("CONTROL DE VEHICULOS")


barraMenu=Menu(root)
root.config(menu=barraMenu,width=500,height=500)

bbddMenu=Menu(barraMenu,tearoff=0)
bbddMenu.add_command(label="Conectar",command=conexionBBDD)
bbddMenu.add_command(label="Salir",command=salirAplicacion)

borrarMenu=Menu(barraMenu,tearoff=0)
borrarMenu.add_command(label="Limpiar campos",command=limpiarCampos)

crudMenu=Menu(barraMenu,tearoff=0)
crudMenu.add_command(label="Crear",command=crear)
crudMenu.add_command(label="Leer",command=leer)
crudMenu.add_command(label="Actualizar",command=actualizar)
crudMenu.add_command(label="Eliminar",command=eliminar)

ayudaMenu=Menu(barraMenu,tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de ...")

barraMenu.add_cascade(label="BBDD",menu=bbddMenu)
barraMenu.add_cascade(label="BORRAR",menu=borrarMenu)
barraMenu.add_cascade(label="CRUD",menu=crudMenu)
barraMenu.add_cascade(label="AYUDA",menu=ayudaMenu)

#------------------comienzo de campos-----------------

miFrame=Frame(root)
miFrame.pack() #Enpaquetado


miId=StringVar()
miPlaca=StringVar()
miFecha=StringVar()
miMarca=StringVar()
miAño=StringVar()
miColor=StringVar()
miTipo=StringVar()
miNombre=StringVar()
miCedula=StringVar()
miDestinoInicial=StringVar()
miDestinoFinal=StringVar()
miCombustible=StringVar()
miMontoCombustible=StringVar()
miViatico=StringVar()
miGastos=StringVar()
miKilometrajeInicial=StringVar()
miKilometrajeFinal=StringVar()


cuadroId=Entry(miFrame,textvariable=miId)
cuadroId.grid(row=0,column=1,padx=10,pady=10)

cuadroFecha=Entry(miFrame,textvariable=miFecha)
cuadroFecha.grid(row=1,column=1,padx=10,pady=10)

cuadroPlaca=Entry(miFrame,textvariable=miPlaca)
cuadroPlaca.grid(row=2,column=1,padx=10,pady=10)

cuadroAño=Entry(miFrame,textvariable=miAño)
cuadroAño.grid(row=3,column=1,padx=10,pady=10)

cuadroMarca=Entry(miFrame,textvariable=miMarca)
cuadroMarca.grid(row=4,column=1,padx=10,pady=10)

cuadroColor=Entry(miFrame,textvariable=miColor)
cuadroColor.grid(row=5,column=1,padx=10,pady=10)

cuadroTipo=Entry(miFrame,textvariable=miTipo)
cuadroTipo.grid(row=6,column=1,padx=10,pady=10)

cuadroNombre=Entry(miFrame,textvariable=miNombre)
cuadroNombre.grid(row=7,column=1,padx=10,pady=10)

cuadroCedula=Entry(miFrame,textvariable=miCedula)
cuadroCedula.grid(row=8,column=1,padx=10,pady=10)

cuadroDestinoInicial=Entry(miFrame,textvariable=miDestinoInicial)
cuadroDestinoInicial.grid(row=9,column=1,padx=10,pady=10)

cuadroDestinoFinal=Entry(miFrame,textvariable=miDestinoFinal)
cuadroDestinoFinal.grid(row=10,column=1,padx=10,pady=10)

cuadroCombustible=Entry(miFrame,textvariable=miCombustible)
cuadroCombustible.grid(row=11,column=1,padx=10,pady=10)

cuadroMonto=Entry(miFrame,textvariable=miMontoCombustible)
cuadroMonto.grid(row=12,column=1,padx=10,pady=10)

cuadroViatico=Entry(miFrame,textvariable=miViatico)
cuadroViatico.grid(row=13,column=1,padx=10,pady=10)

cuadroGastos=Entry(miFrame,textvariable=miGastos)
cuadroGastos.grid(row=14,column=1,padx=10,pady=10)

cuadroKilometrajeInicial=Entry(miFrame,textvariable=miKilometrajeInicial)
cuadroKilometrajeInicial.grid(row=15,column=1,padx=10,pady=10)

cuadroKilometrajeFinal=Entry(miFrame,textvariable=miKilometrajeFinal)
cuadroKilometrajeFinal.grid(row=16,column=1,padx=10,pady=10)

textoComentario=Text(miFrame,width=20,height=5)
textoComentario.grid(row=17,column=1,padx=10,pady=10)

scrollVert=Scrollbar(miFrame,command=textoComentario.yview)
scrollVert.grid(row=17,column=2,sticky="nsew")

textoComentario.config(yscrollcommand=scrollVert.set)

#-----------------aquí comienza los label---------------------

idLabel=Label(miFrame,text="ID:")
idLabel.grid(row=0,column=0,sticky="w",padx=10,pady=10)

fechaLabel=Label(miFrame,text="FECHA:")
fechaLabel.grid(row=1,column=0,sticky="w",padx=10,pady=10)

placaLabel=Label(miFrame,text="PLACA:")
placaLabel.grid(row=2,column=0,sticky="w",padx=10,pady=10)

añoLabel=Label(miFrame,text="AÑO:")
añoLabel.grid(row=3,column=0,sticky="w",padx=10,pady=10)

marcaLabel=Label(miFrame,text="MARCA:")
marcaLabel.grid(row=4,column=0,sticky="w",padx=10,pady=10)

colorLabel=Label(miFrame,text="COLOR:")
colorLabel.grid(row=5,column=0,sticky="w",padx=10,pady=10)

tipoLabel=Label(miFrame,text="TIPO DE VEHICULO:")
tipoLabel.grid(row=6,column=0,sticky="w",padx=10,pady=10)

nombreLabel=Label(miFrame,text="NOMBRE DEL CONDUCTOR:")
nombreLabel.grid(row=7,column=0,sticky="w",padx=10,pady=10)

cedulaLabel=Label(miFrame,text="CEDULA DEL CONDUCTOR:")
cedulaLabel.grid(row=8,column=0,sticky="w",padx=10,pady=10)

destinoInicial=Label(miFrame,text="DESTINO INICIAL:")
destinoInicial.grid(row=9,column=0,sticky="w",padx=10,pady=10)

destinoFinal=Label(miFrame,text="DESTINO FINAL:")
destinoFinal.grid(row=10,column=0,sticky="w",padx=10,pady=10)

combustible=Label(miFrame,text="LITROS DE COMBUSTIBLE:")
combustible.grid(row=11,column=0,sticky="w",padx=10,pady=10)

Monto=Label(miFrame,text="MONTO DE COMBUSTIBLE EN DOLARES:")
Monto.grid(row=12,column=0,sticky="w",padx=10,pady=10)

viaticos=Label(miFrame,text="MONTO DE VIATICOS EN DOLARES:")
viaticos.grid(row=13,column=0,sticky="w",padx=10,pady=10)

gastos=Label(miFrame,text="GASTOS EN DOLARES:")
gastos.grid(row=14,column=0,sticky="w",padx=10,pady=10)

KilometrajeInicialLabel=Label(miFrame,text="KILOMETRAJE INICIAL:")
KilometrajeInicialLabel.grid(row=15,column=0,sticky="w",padx=10,pady=10)

KilometrajeFinalLabel=Label(miFrame,text="KILOMETRAJE FINAL:")
KilometrajeFinalLabel.grid(row=16,column=0,sticky="w",padx=10,pady=10)

comentarioLabel=Label(miFrame,text="COMENTARIOS:")
comentarioLabel.grid(row=17,column=0,sticky="w",padx=10,pady=10)


#--------------------botones inferior----------

miFrame2=Frame(root)
miFrame2.pack()

botonCrear=Button(miFrame2,text="Crear",command=crear)
botonCrear.grid(row=1,column=0,sticky="e",padx=10,pady=10)

botonLeer=Button(miFrame2,text="Leer", command=leer)
botonLeer.grid(row=1,column=1,sticky="e",padx=10,pady=10)

botonActualizar=Button(miFrame2,text="Actualizar",command=actualizar)
botonActualizar.grid(row=1,column=2,sticky="e",padx=10,pady=10)

botonBorrar=Button(miFrame2,text="Eliminar",command=eliminar)
botonBorrar.grid(row=1,column=3,sticky="e",padx=10,pady=10)

root.mainloop()
