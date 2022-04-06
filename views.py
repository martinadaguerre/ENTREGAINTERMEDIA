from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context
from django.template import loader 

from appcoder.forms import CursoFormulario
from appcoder.forms import ProfesorFormulario

def inicio (request):
    plantilla= loader.get_template("inicio")
    archivo= open(r'C:\Users\marti\OneDrive\Escritorio\app_coder\proyectocoder\appcoder\templates')
    plantilla = Template(archivo.read())
    archivo.close()
    context = Context()
    documento = plantilla.render(context)
    return HttpResponse(documento)
def estudiantes(request):

      return render(request, "AppCoder/estudiantes.html")
def entregables(request):

      return render(request, "AppCoder/entregables.html")

def curso(request):

      curso =  curso(nombre="Desarrollo web", camada="19881")
      curso.save()
      documentoDeTexto = f"--->curso: {curso.nombre}   Camada: {curso.camada}"

def cursos(request):

      if request.method == 'POST':

            miFormulario = CursoFormulario(request.POST) 

            print(miFormulario)

            if miFormulario.is_valid:  

                  informacion = miFormulario.cleaned_data

                  curso = curso (nombre=informacion['curso'], camada=informacion['camada']) 

                  curso.save()

                  return render(request, "AppCoder/inicio.html") 

      else: 

            miFormulario= CursoFormulario() 

      return render(request, "AppCoder/cursos.html", {"miFormulario":miFormulario})
def profesores(request):

      if request.method == 'POST':

            miFormulario = ProfesorFormulario(request.POST) 

            print(miFormulario)

            if miFormulario.is_valid:   

                  informacion = miFormulario.cleaned_data
                  
                  profesor = profesor (nombre=informacion['nombre'], apellido=informacion['apellido'],
                   email=informacion['email'], profesion=informacion['profesion']) 

                  profesor.save()

                  return render(request, "AppCoder/inicio.html") 

      else: 

            miFormulario= ProfesorFormulario() 

      return render(request, "AppCoder/profesores.html", {"miFormulario":miFormulario})

 

def buscar(request):

      if  request.GET["camada"]:

	     
            camada = request.GET['camada'] 
            cursos = curso.objects.filter(camada__icontains=camada)

            return render(request, "AppCoder/inicio.html", {"cursos":cursos, "camada":camada})

      else: 

	      respuesta = "No enviaste datos"
