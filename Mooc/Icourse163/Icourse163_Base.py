'''
    Icourse163 Abstract base
'''

import os
if __package__ is None:
    import sys
    sys.path.append('../')
from Mooc.Mooc_Base import *
from Mooc.Mooc_Download import *
from Mooc.Mooc_Request import *
from Mooc.Mooc_Potplayer import *

__all__ = [
    "Icourse163_Base"
]

class Icourse163_Base(Mooc_Base):
    potplayer = Mooc_Potplayer()

    def __init__(self):
        super().__init__()
        self.infos = {}  # Course video and file link request information, including ID, etc.
        self.__term_id = None # Download the title of the course ID
    
    @property
    def term_id(self):
        return self.__term_id

    @term_id.setter
    def term_id(self, term_id):
        self.__term_id = term_id

    def set_mode(self):
        while True:
            try:
                instr = input("Please enter a 0-4 number selective download content (1: ultra-high-definition, 2: HD, 3: bidding, only download courseware) [0 exit]:: ")
                if not instr:
                    continue
                try:
                    innum = int(instr)
                    if innum == 0:
                        return False
                    elif  1 <= innum <= 4:
                        self.mode = innum
                        return True
                    else:
                        print("Please enter an integer between 0-4!")
                        continue
                except ValueError:
                    print("Please enter an integer between 0-4!")
            except KeyboardInterrupt:
                pass

    @classmethod
    @potplayer
    def download_video(cls, video_url, video_name, video_dir):
        return super().download_video(video_url, video_name, video_dir)
