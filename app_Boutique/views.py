from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria

# Página de inicio
def inicio_boutique(request):
    total_categorias = Categoria.objects.count()
    categorias = Categoria.objects.all().order_by('-fechacreacion')[:5]
    return render(request, 'inicio.html', {'total_categorias': total_categorias, 'categorias': categorias})

# Agregar categoría
def agregar_categoria(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        tipo = request.POST.get('tipo')
        slug = request.POST.get('slug')
        activo = True if request.POST.get('activo') == 'on' else False

        Categoria.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            tipo=tipo,
            slug=slug,
            activo=activo
        )
        return redirect('ver_categorias')
    return render(request, 'categoria/agregar_categoria.html')

# Ver todas
def ver_categorias(request):
    categorias = Categoria.objects.all().order_by('nombre')
    return render(request, 'categoria/ver_categorias.html', {'categorias': categorias})

# Actualizar
def actualizar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    return render(request, 'categoria/actualizar_categoria.html', {'categoria': categoria})

def realizar_actualizacion_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    if request.method == 'POST':
        categoria.nombre = request.POST.get('nombre')
        categoria.descripcion = request.POST.get('descripcion')
        categoria.tipo = request.POST.get('tipo')
        categoria.slug = request.POST.get('slug')
        categoria.activo = True if request.POST.get('activo') == 'on' else False
        categoria.save()
        return redirect('ver_categorias')
    return redirect('ver_categorias')

# Borrar
def borrar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('ver_categorias')
    return render(request, 'categoria/borrar_categoria.html', {'categoria': categoria})
