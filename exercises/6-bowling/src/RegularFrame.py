class RegularFrame:
    lance_1 :int
    lance_2 :int

    def __init__(self, frame: str):
       self.lance_1=4


    def convert_char(self, value):
        if value == 0:
            return '-'
        return str(value)