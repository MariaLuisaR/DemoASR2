from django.shortcuts import render
from .models import Usuario

def upload_file(request):
    # Fetch the user details for ID 1020
    user_name = None
    user_estado = None
    error_message = None
    try:
        user = Usuario.objects.get(id=1020)
        user.estado = "Aprobado"
        user.save()
        user_name = user.nombre
        user_estado = user.estado
    except Usuario.DoesNotExist:
        error_message = 'Usuario con ID 1020 no encontrado.'
    
    usuarios = Usuario.objects.all()

    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        if user_id:
            user = Usuario.objects.filter(id=user_id).first()
            if user:
                user_name = user.nombre
                user_estado = user.estado
            else:
                error_message = 'Usuario no encontrado.'
        else:
            error_message = 'ID de usuario no proporcionado.'

    return render(request, 'upload_file.html', {'user_name': user_name, 'user_estado': user_estado, 'error_message': error_message, 'usuarios': usuarios})
