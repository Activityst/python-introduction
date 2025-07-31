class SpareFrame:
    nex_lance :int

    def __init__(self, frame: str):
        self.lance_1 = self.convert_spare_frame(frame[0])
        self.lance_2 = self.convert_spare_frame(frame[1])
        self.lance_3 = self.convert_spare_frame(frame[2])

    def convert_spare_frame(self, frame: str) -> int:
        if frame == 'X':
            return 10
        elif frame == '-':
            return 0
        return int(frame)

    def calc_frame(self):
        return self.lance_1 + self.lance_2 + self.lance_3