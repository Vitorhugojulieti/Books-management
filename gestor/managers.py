# Em gestor/managers.py
from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, cpf=None, telefone=None, admin=False, bloqueado=False, **extra_fields):
        if not username:
            raise ValueError('O nome de usuário deve ser definido.')
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            cpf=cpf,
            telefone=telefone,
            admin=admin,
            bloqueado=bloqueado,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, cpf=None, telefone=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('admin', True)
        extra_fields.setdefault('bloqueado', False)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, cpf, telefone, **extra_fields)