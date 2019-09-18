from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    Cafeteria = "Cafeteria"
    Libreria = "Libreria"
    Administrador = 'Administrador'
    belongs_to = (
        (Cafeteria, 'Cafeteria'),
        (Libreria, 'Libreria'),
        (Administrador, 'Administrador')

    )
    user = models.OneToOneField(User)
    completed_data = models.SmallIntegerField(default=0)
    sucursal = models.SmallIntegerField(default = 0)
    belongs_to = models.CharField(choices = belongs_to, max_length=100)
    picture = models.ImageField(upload_to='imagenes_perfil', blank=True)

