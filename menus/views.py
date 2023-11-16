from django.shortcuts import render

def menu_view(request,menu_name=None):
    # context['current_path']=current_path
    return render(request, 'menus/index.html',{'menu_name':menu_name})