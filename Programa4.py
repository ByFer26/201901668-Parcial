from typing import Type
import psycopg2

conexion=psycopg2.connect(
        host="localhost",
        port="5432",
        user="postgres",
        password="netacad20",
        dbname="Parcial"
    )
op=0;

logico=False
while(not logico):
    try: 
        print("Que desea realizar")
        print("1. Averiguar el tipo de numero")
        print("2.Ver el historial")
        print("3.Salir")
        op=int(input("Opcion:"))
    
    except ValueError or NameError:
        print("Ingrese un numero")

    except TypeError:
        print("Ingrese un numero")

    try:
        if op==1:
            numero=int(input("Ingrese un numero:"))
            divisores=0
            for i in range(1,numero+1):
                if(numero%i==0):
                    divisores=divisores+1
            print(divisores)
            if(divisores==2):
                print("Es un numero primo")
                tipo=str("Primo")
                Cursor=conexion.cursor()
                Cursor.execute("INSERT INTO programa4(numero,tipo) VALUES(%s,%s);",(numero,tipo))
                conexion.commit()
                Cursor.close()
            else:
                print("No es un numero primo")
                tipo=str("No es primo")
                Cursor=conexion.cursor()
                Cursor.execute("INSERT INTO programa4(numero,tipo) VALUES(%s,%s);",(numero,tipo))
                conexion.commit()
                Cursor.close()
        
        if op==2:
            Cursor=conexion.cursor()
            SQL='SELECT*FROM programa3;'
            Cursor.execute(SQL)
            valores=Cursor.fetchall()
            print(valores)
            Cursor.close()            
                
                
                    
            
        
        if(op==3):
            quit()

    except ValueError or NameError:
        print("Ingrese algo valido")

    except TypeError:
        print("Ingrese algo valido")
    
     

