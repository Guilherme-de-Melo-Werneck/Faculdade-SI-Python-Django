from django.shortcuts import render
from .models import Pessoas


def index(request):
    pessoas = Pessoas.objects.all()
    template_name = "index.html"
    context = {
                'pessoas':pessoas
    }
    return render(request, template_name, context)


def list_pessoas(request):
    pessoas = Pessoas.objects.all()
    template_name = "list_pessoas.html"
    context = {
                'pessoas':pessoas
    }
    return render(request, template_name, context)


# from django.http import HttpResponse
# def index(request):
#     seu_nome = 'Guilherme'
#     idade = 20
#     html = f'''
#     <html>
#     <head>
#         <title> Aula3 </title>
#     </head>
#     <body>
#         <font face = "Trebuchet MS" color = "red">
#         <h1> Meu nome é {seu_nome} </h1>
#         <h2> Minha idade é {idade} anos </h2>
        
#     </body>
#     </html>
# '''
    
#     return HttpResponse(html)
