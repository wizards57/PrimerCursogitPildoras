#blanalsdnosndofnspdf
from django.http import HttpResponse
import datetime
from django.template import Template, Context#, loader
from django.template.loader import get_template #esta importación seria para ahorrate la palabra loader linea 30 doc_externo=get_template('primeraplantilla.html')
from django.shortcuts import render
class Persona (object):
    def __init__(self, nombre, apellido):

            self.nombre=nombre
            self.apellido=apellido

def saludo(request): #primera vista 
    p1=Persona("Fernando con class", "Apellido Con class")
    
    #nombre="Fernando"
    #apellido="Mariscal"
    temasdelCurso=["Plantillas", "Modelo", "formularios", "Vistas", "Despliegue"]
    #temasdelCurso=[]
    #----------------------------
    #este se usaba para cargar la plantilla de forma manunal
    # doc_externo=open("C:/Users/UsuarioPro/Documents/django308/Proyecto1/Proyecto1/plantillas/primeraplantilla.html")
    #plt=Template(doc_externo.read())
    #doc_externo.close()
    
    
    #ctx=Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido, "fecha":datetime.datetime.now(), "temas":temasdelCurso})
    #documento=plt.render(ctx)
    #-------------------------------
    #doc_externo=loader.get_template('primeraplantilla.html')
    #doc_externo=get_template('primeraplantilla.html')
    #documento=doc_externo.render({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido, "fecha":datetime.datetime.now(), "temas":temasdelCurso})
    #return HttpResponse(documento)
    #----------------------------------
    return render(request,"primeraplantilla.html",{"nombre_persona":p1.nombre,"apellido_persona":p1.apellido, "fecha":datetime.datetime.now(), "temas":temasdelCurso})

def cursoC(request):
    
    fecha=datetime.datetime.now()
    return render(request, "CursoC.html", {"fecha":fecha})

def cursoCCS(request):
    
    fecha=datetime.datetime.now()
    return render(request, "cursoccs.html", {"fecha":fecha})

def despedida(request):
    return HttpResponse("Hasta la vista BB")

def fecha(request):
    fecha_actual=datetime.datetime.now()
    imprime="""<html>
    <body>
    <h1>
    Laa fecha actual es: %s 
    </html>
    </body>
    </h1>""" % fecha_actual
    return HttpResponse(imprime)

def calculaE(request, anio,edad_actual):
    #edad_actual=edad_actual
    periodo=anio-2020
    edadfutura=edad_actual+periodo
    imprime="""<html>
    <body>
    <h1>
    En el año: %s tendrás %s años 
    </html>
    </body>
    </h1>""" % (anio,edadfutura)
    return HttpResponse(imprime)
