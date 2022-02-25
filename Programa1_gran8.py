import psycopg2

conexion=psycopg2.connect(
        host="localhost",
        port="5432",
        user="postgres",
        password="netacad20",
        dbname="Parcial"
    )

logico=False
while(not logico):

    try:

        print("Que desea realizar ")
        print("1.Jugar gran 8")
        print("2.Ver el historial")
        print("3.Salir")
        op=int(input("Opcion: "))

        def resultado(a,b):
            if(a+b==8 or a==8 or b==8):
                print("Gano el juego")
                res=str("Gano el juego")
                Cursor=conexion.cursor()
                Cursor.execute("INSERT INTO programa1(cara1,cara2,resultado) VALUES(%s,%s,%s);",(a,b,res))
                conexion.commit()
                Cursor.close()

            if(a+b==7 or a==7 or b==7) :
                print("Perdio el juego")
                res=str("Perdio el juego")
                Cursor=conexion.cursor()
                Cursor.execute("INSERT INTO programa1(cara1,cara2,resultado) VALUES(%s,%s,%s);",(a,b,res))
                conexion.commit()
                Cursor.close()

            else:
                print("Puede seguir jugando")
                res=str("Puede seguir")
                Cursor=conexion.cursor()
                Cursor.execute("INSERT INTO programa1(cara1,cara2,resultado) VALUES(%s,%s,%s);",(a,b,res))
                conexion.commit()
                Cursor.close()

    except ValueError or NameError:
        print("Ingrese un numero")      

    except TypeError:
        print("Ingrese un numero")      


    try:
        if op==1:
            cara1=int(input("Cara 1 del dado:"))
            cara2=int(input("Cara 2 del dado:"))
            resultado(cara1,cara2)

        if op==2:
            Cursor=conexion.cursor()
            SQL='SELECT*FROM programa1;'
            Cursor.execute(SQL)
            valores=Cursor.fetchall()
            print(valores)
            Cursor.close() 

        if op==3:
            quit()

    except NameError or ValueError:
        print("Ingrese algo valido")

    except TypeError:
        print("Ingrese algo valido")

