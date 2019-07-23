from django.shortcuts import render

# Create your views here.

def pagina_inicial(request):
    context = {"nome": "Camila",
     "gatos": ["bilbo", "tigrinho", "felix", "zeus", "darko"]
     }
    return  render(request, 'index.html', context)
