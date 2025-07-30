from .RegularFrame import RegularFrame
class Bowling:
    frames: list[RegularFrame]

    def __init__(self, frames_as_string: str):
        frames_as_string_list = frames_as_string.split()
        self.regular_frames = frames_as_string_list[0]





   # def calc (s: str):

