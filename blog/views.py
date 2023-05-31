from django.shortcuts import render
from .models import Categoria,Post
# Create your views here.


def blog(request):
	post = Post.objects.all()
	categoria = Categoria.objects.all()
	return render(request,"blog/blog.html",{"post":post,"categorias":categoria})



def categoria(request,categoria_id):
	categoria = Categoria.objects.get(id=categoria_id)
	post = Post.objects.filter(categoria=categoria)
	return render(request,'blog/categorias.html',{'categorias':categoria,'post':post})