import os
import csv

def menu():
    os.system("cls")
    print("******** Le buscamos todo   ********\n"+
          "===========================\n"+
          "[1]-> Ingreso investigación \n"+
          "[2]-> Eliminar investigación \n"+
          "[3]-> Mostrar una investigación específica \n"+
          "[4]-> Salir \n")
    while(True):
        try:
            op=int(input("Ingrese su opción "))
            if(op>=1 and op<=4):
                break
        except ValueError:
            print("Debe ser un núemro entero ")
    return op
def validaNombre():
    tt=""
    while(len(tt.strip())<3):
        tt=input("Ingrese nombre ").capitalize()
    return tt
def validaRut():
    rr=""
    while(len(rr.strip())<8):
        rr=input("Ingrese rut ")
    return rr
def validaTipo():
    tt=""
    while(tt!="Estudios geneticos" and tt!="Calidad de vida" and tt!="Estudios epidemiológicos"):
        tt=input("Ingrese tipo de investigación Estudios geneticos/Calidad de vida/Estudios epidemiológicos ").capitalize()
    return tt
def validaTot():
    while(True):
        try:
            vv=int(input("Cuantos investigadores son?  "))
            if(vv>0):
                break
        except ValueError:
            print("Debe ser entero")
    return vv
def validaTiempo():
    while(True):
        try:
            vv=int(input("Cuanto tiempo tardará, mínimo 90 dias "))
            if(vv>90):
                break
        except ValueError:
            print("Debe ser entero")
    return vv
def ingresarInvestigacion():
    rut=validaRut()
    nomb=validaNombre()
    tipo=validaTipo()
    totalI=validaTot()
    tiempo=validaTiempo()
    if(tipo=="Calidad de vida"):
        vv=19000
    elif(tipo=="Estudios epidemiológicos"):
        vv=30000
    else:
        vv=25000
    inversion=int((tiempo/30)*4)*vv*totalI
    with open('investigacion.csv', mode='a+', newline='') as file:
        writer = csv.writer(file)           
        writer.writerow([rut,nomb,tipo,totalI,tiempo,inversion])
    print("Esta investigación costará un total de :$",inversion)
    print("Archivo creado")
    os.system("pause")
def eliminar():
    rut=validaRut()
    animalitos=[]
    with open("investigacion.csv","r") as f:
        info=csv.reader(f)
        animalitos=list(info)
    os.system("erase investigacion.csv")
    with open("investigacion.csv","w",newline="") as f:
        x=csv.writer(f)
        for ali in animalitos:
            if(ali[0] != rut):
                x.writerow(ali)
    print("Investigacion del rut, elimindas del archivo!!!")
    os.system("pause")
def mostrarUna():
    rut=validaRut()
    animalitos=[]
    with open("investigacion.csv","r") as f:
        info=csv.reader(f)
        animalitos=list(info)
        for ali in animalitos:
            if(ali[0] == rut):
                print("DATOS DE LA INVESTIGACION")
                print("Rut: ",ali[0])
                print("Nombre: ",ali[1])
                print("Tipo: ",ali[2])
                print("Total investigadores: ",ali[3])
                print("Tiempo de investigacion: ",ali[4])
                print("Costo total: $",ali[5])
    os.system("pause")

        


