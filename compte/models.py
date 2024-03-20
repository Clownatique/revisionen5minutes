from django.db import models
from django.contrib.auth.models import AbstractUser
from quiz.models import FlashCarte, MetaDonneesCarte
from django.core import serializers
import uuid

class Eleve(AbstractUser):
    '''
    Un eleve = un utilisateur.
    TODO:
    Peut être rajouté des infos par rapport au niveau d'étude
    Réfléchir à un système de score
    '''
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    deck = models.ManyToManyField("quiz.MetaDonneesCarte")
    
    def __str__(self):
        return self.username
