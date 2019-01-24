class Personne:
    """Classe définissant une personne caractérisée par :
    - son nom ;
    - son prénom ;
    - son âge ;
    - son lieu de résidence"""
    nb_personnes = 0
    
    def __init__(self, nom, prenom):
        """Constructeur de notre classe avec les attributs nom, 
        prenom age et lieu_residence"""
        self.nom = nom
        self.prenom = prenom
        self.age = 33
        self._lieu_residence = "Paris" # Notez le souligné _ devant le nom
        Personne.nb_personnes+=1
        
    def _get_lieu_residence(self):
        print("On accède à l'attribut lieu_residence !")
        return self._lieu_residence
    def _set_lieu_residence(self, nouvelle_residence):
        """Méthode appelée quand on souhaite modifier le lieu de résidence"""
        print("Attention, il semble que {} déménage à {}.".format( \
                self.prenom, nouvelle_residence))
        self._lieu_residence = nouvelle_residence
    # On va dire à Python que notre attribut lieu_residence pointe vers une
    # propriété
    lieu_residence = property(_get_lieu_residence, _set_lieu_residence)

    def __repr__(self):
        """Quand on entre notre objet dans l'interpréteur"""
        return "Personne: nom({0}), prénom({1}), âge({2})".format(
                self.nom, self.prenom, self.age)
        
    def __str__(self):
        """Méthode permettant d'afficher plus joliment notre objet"""
        return "{} {}, âgé de {} ans".format(
                self.prenom, self.nom, self.age)
