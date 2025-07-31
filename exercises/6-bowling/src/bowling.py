from .RegularFrame import RegularFrame
class Bowling:
    frames: list[RegularFrame]

    def __init__(self, frames_as_string: str):
        frames_as_string_list = frames_as_string.split()
        temp_list=[]
        for frame_1 in frames_as_string_list :
            temp_list.append(RegularFrame(frame_1))
        self.frames= temp_list

    def calc(self) -> int:
        total_score = 0
        for frame in self.frames:
            total_score += frame.calc_frame()
        return total_score


