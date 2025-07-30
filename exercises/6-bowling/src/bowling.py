#write code here
class Bowling:
    def zero(self, score):
        nb_quille =(score == 0)
        return nb_quille



    def Point(self, score):
        nb_quille = (score != 0 and score < 10)
        return nb_quille

    #def Spare(self, score):
