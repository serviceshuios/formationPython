class Error(Exception):
    """Classe de base pour les exceptions dans ce module."""
    pass

class InputError(Error):
    """Exceptions levées pour les erreurs de saisie.

    Attributes:
        expression -- variable de récupération de la donnée saisie
        message -- message d'erreur
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message