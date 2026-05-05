from django.shortcuts import render, get_object_or_404

from .models import Categoria, Producto
# Create your views here.

def index(request):
     """ VISTAS para el catalogo de prodcutos """
     listaProductos = Producto.objects.all()
     listaCategorias = Categoria.objects.all()
     
     context = {
          'productos': listaProductos,
          'categorias': listaCategorias
     }
     return render(request, 'index.html', context)

def productosPorCategoria(request, categoria_id):
     """ Vista para filtrar productos por categoria"""

     objCategoria = Categoria.objects.get(pk=categoria_id)
     listaProductos = objCategoria.producto_set.all()
     listaCategorias = Categoria.objects.all()

     context = {
          'productos': listaProductos,
          'categorias': listaCategorias
     }
     return render(request, 'index.html', context)

def productosPorNombre(request):
     """ Vista para filtrar productos por nombre """
     nombre = request.POST['nombre']

     listaProductos = Producto.objects.filter(nombre__contains=nombre)
     listaCategorias = Categoria.objects.all()

     context = {
          'productos': listaProductos,
          'categorias': listaCategorias
     }
     return render(request, 'index.html', context)

def productoDetalle(request,producto_id):
     """ Vista para el detalle de producto"""
     
     objProducto = get_object_or_404(Producto, pk=producto_id)

     context = {
          'producto': objProducto
     }
     return render(request, 'producto.html', context)