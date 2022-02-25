
import psycopg2
import statistics

op=0;

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
        print("Que desea realizar")
        print("1.Ingresar notas")
        print("2. Ver historial")
        print("3.Salir")
        op=int(input("Opción:"))

    except ValueError or TypeError:
        print("Ingrese un valor valido")

    except NameError:
        print("Ingrese un valor valido")

    def datos(a,b,c,d,e):
        lista=[a,b,c,d,e]
        prom=(a+b+c+d+e)//5
        print("La media es",prom,"\n")
        med=statistics.median(lista)
        print("La mediana es:",med,"\n")
        mod=statistics.mode(lista)
        print("La moda es:",mod,"\n")
        dev=statistics.stdev(lista)
        print("La desviación estandard es:",round(dev,4),"\n")
        varianz=statistics.variance(lista)
        print("La varianza es:",varianz,"\n")
        Cursor=conexion.cursor()
        Cursor.execute("INSERT INTO programa2(numero1,numero2,numero3,numero4,numero5,media,mediana,moda,desviacion,varianza) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",(a,b,c,d,e,prom,med,mod,dev,varianz))
        conexion.commit()
        Cursor.close()

    logico=False




    if op==1:
        try:
            nota1=float(input("Ingrese la primera nota:"))
            nota2=float(input("Ingrese la segunda nota:"))
            nota3=float(input("Ingrese la tercera nota:"))
            nota4=float(input("Ingrese la cuarta nota:"))
            nota5=float(input("Ingrese la quinta nota:"))
            datos(nota1,nota2,nota3,nota4,nota5)
        

        except ValueError or TypeError:
            print("Ingrese un caracter valido:")

        except NameError:
            print("Ingrese un caracter valido")

    if op==2:
        Cursor=conexion.cursor()
        SQL='SELECT*FROM programa2;'
        Cursor.execute(SQL)
        valores=Cursor.fetchall()
        print(valores)
        Cursor.close()

    if(op==3):
        quit()