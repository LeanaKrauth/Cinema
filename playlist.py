#!/usr/bin/python
# -*- coding: utf-8 -*-

from sl29.structures import Queue
from cinema import Realisateur, Film

realisateurs = [{'id':1,'nom':'Lautner', 'prenom':'Georges', 'films':[1,2]},
                {'id':2,'nom':'Gillian', 'prenom':'Terry', 'films':[3,4,5]},
               ]

films = [
    {'id':1,'titre':"Les tontons fligueurs", 'annee':1963},
    {'id':2,'titre':"Des pissenlits par la racine", 'annee':1964},
    {'id':3,'titre':"L'armée des 12 singes", 'annee':1996},
    {'id':4,'titre':"MONTY PYTHON, Le sens de la vie", 'annee':2002},
    {'id':5,'titre':"Las Vegas parano", 'annee':1998},  
]

class Playlist:
    def __init__(self):
        self._realisateurs = []
        self._films = []
        
    def creer_films(self, dico_films):
        for film in dico_films:
            nouveau_film = Film(film['id'], film['titre'], film['annee'])
            self._films.append(nouveau_film)
    
    def afficher_films(self):
        print(self._films)
        
    def creer_realisateur(self, dico_realisateurs):
        for realisateurs in dico_realisateurs:
            nouveau_realisateur = Realisateur(realisateurs['id'], realisateurs['nom'], realisateurs['prenom'])



