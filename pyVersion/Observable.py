import Observateur, Equipe

class Observable:
    def __init__(self):
        self.observateurs = []
    
    def ajouter_observateur(self, observateur: Observateur):
        self.observateurs.append(observateur)
    
    def retirer_observateur(self, observateur: Observateur):
        self.observateurs.remove(observateur)
    
    def notifier_observateurs(self, gagnant: Equipe, perdant: Equipe):
        for observateur in self.observateurs:
            observateur.update(gagnant, perdant)