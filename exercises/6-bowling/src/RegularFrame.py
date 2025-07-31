class RegularFrame:
    lance_1 :int
    lance_2 :int

    def __init__(self, frame: str):
       self.lance_1 = self.convert_frame(frame[0])
       self.lance_2 = self.convert_frame(frame[1])

    def convert_frame(self, frame: str)-> int:
        if frame == '-':
            return 0
        return int (frame)

    def calc_frame(self):
        return self.lance_1 + self.lance_2
        