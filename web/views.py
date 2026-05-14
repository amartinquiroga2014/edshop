from django.shortcuts import render, get_object_or_404, redirect

from .models import Categoria, Producto
# Create your views here.

def index(request):
     """ VISTAS para el catalogo de productos """
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

""" Vista para el carrito de compras"""
from .carrito import Cart

def carrito(request):     
     return render(request, 'carrito.html')

def agregarCarrito(request, producto_id):
   
    if request.method == 'POST':
         cantidad = int(request.POST['cantidad'])
    else:
       cantidad = 1

    objProducto = Producto.objects.get(pk=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.add(objProducto, cantidad)

    #print(request.session.get("cart"))
    
    if request.method == "GET":
         return redirect('/')
    
    return render(request, 'carrito.html')

def eliminarProductoCarrito(request, producto_id):
     objProducto = Producto.objects.get(pk=producto_id)
     carritoProducto = Cart(request)
     carritoProducto.delete(objProducto)

     return render(request, 'carrito.html')

def limpiarCarrito(request):
     carritoProducto = Cart(request)
     carritoProducto.clear()

     return render(request, 'carrito.html')
