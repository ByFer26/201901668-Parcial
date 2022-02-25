
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
        print("1. Calcular el iva")
        print("2.Ver historial")
        print("3.Salir")
        op=int(input("Ingrese una opcion:"))

    except ValueError or NameError:
        print("Ingrese un numero")

    except TypeError:
        print("Ingrese un numero")

    try: 
        if op==1:
            precio=float(input("Ingrese el precio:"))
            iva=precio*0.12
            precioN=precio-iva
            print("El precio original es ",precio," el precio sin iva es ",precioN," el iva es",iva)
            Cursor=conexion.cursor()
            Cursor.execute("INSERT INTO programa3(precio,iva,precion) VALUES(%s,%s,%s);",(precio,round(iva,4),precioN))
            conexion.commit()
            Cursor.close()

        if op==2:
            Cursor=conexion.cursor()
            SQL='SELECT*FROM programa3;'
            Cursor.execute(SQL)
            valores=Cursor.fetchall()
            print(valores)
            Cursor.close()

        if op==3:
            quit()
        
    except ValueError or NameError:
        print("Ingrese algo valido")

    except TypeError:
        print("Ingrese algo valido")