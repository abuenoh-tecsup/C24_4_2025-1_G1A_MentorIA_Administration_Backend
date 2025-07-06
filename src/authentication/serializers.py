# authentication/serializers.py

from rest_framework import serializers
from .models import User, Professor, Student
from google.oauth2 import id_token
from google.auth.transport import requests
from django.conf import settings

class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    google_id = serializers.CharField(required=False, allow_null=True, allow_blank=True)

    class Meta:
        model = User
        fields = [
            'url', 'id', 'username', 'email', 'phone', 'first_name', 
            'last_name', 'date_joined', 'last_login', 'profile_picture_url', 
            'google_id', 'role', 'password'
        ]
        extra_kwargs = {
            'url': {'view_name': 'user-detail'},
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        google_id = validated_data.pop('google_id', None)
        
        user = User(**validated_data)
        user.google_id = google_id
        
        # Si es admin y se proporciona password, lo establecemos
        if user.role == 'admin' and password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        
        user.save()
        return user

    def update(self, instance, validated_data):
        # Remover password del validated_data si existe
        password = validated_data.pop('password', None)
        google_id = validated_data.pop('google_id', None)
        
        # Actualizar campos básicos
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        # Solo actualizar google_id si se proporciona y no es una cadena vacía
        if google_id is not None and google_id != '':
            instance.google_id = google_id
        elif google_id == '': # Permite borrar el google_id si se envía vacío
            instance.google_id = None
        
        # No actualizamos password aquí por seguridad, debería manejarse aparte
        instance.save()
        return instance


class ProfessorSerializer(serializers.HyperlinkedModelSerializer):
    user_details = UserSerializer(source='user', read_only=True)
    
    # Campos del usuario que vendrán desde el frontend
    username = serializers.CharField(write_only=True)
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    phone = serializers.CharField(write_only=True, required=False, allow_blank=True)
    profile_picture_url = serializers.URLField(write_only=True, required=False, allow_blank=True)

    class Meta:
        model = Professor
        fields = [
            'url', 'id', 'user_details', 'employee_code', 'hire_date', 
            'department', 'academic_title', 'office_location', 'status',
            # Campos del usuario
            'username', 'first_name', 'last_name', 'email', 'phone', 'profile_picture_url'
        ]
        extra_kwargs = {
            'url': {'view_name': 'professor-detail'}
        }

    def create(self, validated_data):
        # Extraer datos del usuario
        user_data = {
            'username': validated_data.pop('username'),
            'first_name': validated_data.pop('first_name'),
            'last_name': validated_data.pop('last_name'),
            'email': validated_data.pop('email'),
            'phone': validated_data.pop('phone', ''),
            'profile_picture_url': validated_data.pop('profile_picture_url', ''),
            'role': 'professor'
        }
        
        # Crear usuario
        user = User(**user_data)
        user.set_unusable_password()
        user.save()
        
        # Crear profesor
        professor = Professor.objects.create(user=user, **validated_data)
        return professor

    def update(self, instance, validated_data):
        # Extraer datos del usuario
        user_data = {}
        user_fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'profile_picture_url']
        
        for field in user_fields:
            if field in validated_data:
                user_data[field] = validated_data.pop(field)
        
        # Actualizar usuario si hay datos
        if user_data:
            # No permitir cambiar username en actualización
            user_data.pop('username', None) # Asegurarse de que no se actualice el username
            
            for attr, value in user_data.items():
                setattr(instance.user, attr, value)
            instance.user.save()
        
        # Actualizar profesor
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        return instance


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    user_details = UserSerializer(source='user', read_only=True)
    
    # Campos del usuario que vendrán desde el frontend
    username = serializers.CharField(write_only=True)
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    phone = serializers.CharField(write_only=True, required=False, allow_blank=True)
    profile_picture_url = serializers.URLField(write_only=True, required=False, allow_blank=True)

    class Meta:
        model = Student
        fields = [
            'url', 'id', 'user_details', 'career', 'student_code', 'enrollment_date',
            'current_semester', 'average_grade', 'status',
            # Campos del usuario
            'username', 'first_name', 'last_name', 'email', 'phone', 'profile_picture_url'
        ]
        extra_kwargs = {
            'url': {'view_name': 'student-detail'}
        }

    def create(self, validated_data):
        # Extraer datos del usuario
        user_data = {
            'username': validated_data.pop('username'),
            'first_name': validated_data.pop('first_name'),
            'last_name': validated_data.pop('last_name'),
            'email': validated_data.pop('email'),
            'phone': validated_data.pop('phone', ''),
            'profile_picture_url': validated_data.pop('profile_picture_url', ''),
            'role': 'student'
        }
        
        # Crear usuario
        user = User(**user_data)
        user.set_unusable_password()
        user.save()
        
        # Crear estudiante
        student = Student.objects.create(user=user, **validated_data)
        return student

    def update(self, instance, validated_data):
        # Extraer datos del usuario
        user_data = {}
        user_fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'profile_picture_url']
        
        for field in user_fields:
            if field in validated_data:
                user_data[field] = validated_data.pop(field)
        
        # Actualizar usuario si hay datos
        if user_data:
            # No permitir cambiar username en actualización
            user_data.pop('username', None) # Asegurarse de que no se actualice el username
            
            for attr, value in user_data.items():
                setattr(instance.user, attr, value)
            instance.user.save()
        
        # Actualizar estudiante
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        return instance


class LoginSerializer(serializers.Serializer):
    credential = serializers.CharField() 

    def validate(self, data):
        token = data.get('credential')
        if not token:
            raise serializers.ValidationError('Google credential token is required.')

        try:
            idinfo = id_token.verify_oauth2_token(
                token, 
                requests.Request(), 
                settings.GOOGLE_CLIENT_ID
            )
            
            google_user_id = idinfo['sub']
            google_email = idinfo.get('email')

            # --- 👇 AQUÍ ESTÁ LA LÍNEA DE DEPURACIÓN 👇 ---
            print(f"--------------------------------------------------")
            print(f"DEBUG: Google User ID obtenido del token: {google_user_id}")
            print(f"DEBUG: Google Email obtenido del token: {google_email}")
            print(f"--------------------------------------------------")
            # --- 👆 FIN DE LA LÍNEA DE DEPURACIÓN 👆 ---

        except ValueError as e:
            raise serializers.ValidationError(f'Invalid Google token: {e}')

        try:
            # 1. Intentar encontrar por google_id (si ya se había vinculado)
            user = User.objects.get(google_id=google_user_id)
            if user.email != google_email: # Solo actualiza si ha cambiado
                user.email = google_email
            user.save() # Guarda solo si hubo cambios, para evitar escrituras innecesarias

        except User.DoesNotExist:
            # 2. Si no se encuentra por google_id, intentar encontrar por email
            try:
                user = User.objects.get(email=google_email)
                if not user.google_id:
                    user.google_id = google_user_id
                    user.save()
                elif user.google_id != google_user_id:
                    raise serializers.ValidationError(
                        'Esta cuenta de correo ya está registrada con una cuenta de Google diferente.'
                    )

            except User.DoesNotExist:
                # 3. Si no se encuentra ni por google_id ni por email, entonces el usuario no existe en el sistema.
                raise serializers.ValidationError(f'Usuario con correo {google_email} no encontrado en el sistema.')

        # Verificar si la cuenta está activa
        if not user.is_active:
            raise serializers.ValidationError('Cuenta de usuario inactiva.')

        # Aquí puedes agregar lógica específica según el rol si necesitas redirigir
        if user.role != 'admin':
            raise serializers.ValidationError('Acceso denegado. Solo administradores pueden iniciar sesión aquí.')

        # Si todo es válido, adjuntar el usuario a los datos validados
        data['user'] = user
        return data