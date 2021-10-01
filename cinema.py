#!/usr/bin/python
# -*- coding: utf-8 -*-

class Realisateur:
    def __init__(self, nom, prenom):
        self._ident = 1
        nom = nom.title()
        self._nom = nom
        prenom = prenom.title()
        self._prenom = prenom
        self._films = []   
            
    def get_ident(self):
        """
        getter de l'identifient
        """
        return self._ident 
  
    def get_nom(self):
        """
        getter du nom
        """
        return self._nom
    
    def get_prenom(self):
        '''
        getter du prenom
        '''
        return self._prenom
    
    def presentation(self):
        '''
        affiche le nom et les films realise
        '''
        print(self._prenom +' '+ self._nom)
        for film in self._films:
            print('- ',film.get_titre(), film.get_annee())
    
    def addFilm(self, un_film):
        """
        ajout d'un film à la liste des films realises
        """
        if not(un_film in self._films):
            if un_film.get_realisateur() == None:
                self._films.append(un_film)
                un_film.set_realisateur(self)
            else:
                return 'Le film à déja été réinitialisé'
        else:
            return 'Le film à déja été réalisé'
        
liste_films = {}        
class Film:
    def __init__(self, titre, annee):
        self._ident = 11
        self._titre = titre
        self._annee = annee
        self._realisateur = None      
            
    def __repr__(self):
        return self.get_titre()
    
    def get_ident(self):
        """
        getter de l'identifient
        """
        return self._ident
    
    def get_titre(self):
        """
        getter du titre
        """
        return self._titre
    
    def get_annee(self):
        #getter de l' annee de realisation
        return self._annee
    
    def get_realisateur(self):
        """
        getter du realisateur
        """
        return self._realisateur
    
    def presentation(self):
        #retourne le titre, l'annee et le realisateur du filme
        if self._realisateur == None:
            return ' '.join([self._titre, '(', self._annee, ')'])
        else:              
            return (' '.join([self._titre, '(', self._annee, ')', self._realisateur.get_nom(), self._realisateur.get_prenom()]))
    
    def set_realisateur(self, un_realisateur):
        #setteur du realisateur
        self._realisateur = un_realisateur
    
    