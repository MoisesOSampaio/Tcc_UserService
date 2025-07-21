from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.
'''
username (nome de usuário único)

password (senha criptografada)

email (endereço de e-mail)

first_name (primeiro nome)

last_name (sobrenome)

is_active (se a conta está ativa)

is_staff (se o usuário pode acessar o painel de administração)

is_superuser (se o usuário tem todas as permissões)

date_joined (data de criação da conta)

last_login (data do último login)
'''


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    cargo = models.CharField(max_length=100, null=False)
    lideranca = models.BooleanField()

    class Meta:
       
        db_table = 'users' 

    def __str__(self):
        return self.username
