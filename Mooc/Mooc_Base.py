'''
    Mooc Displication: used to derive all MOOC subclasses
'''

import os
from abc import ABC, abstractmethod
from Mooc.Mooc_Config import *
from Mooc.Mooc_Download import *
from Mooc.Mooc_Request import *

__all__ = [
    "Mooc_Base"
]

class Mooc_Base(ABC):
    def __init__(self):
        self.__mode = None
        self.__cid = None
        self.__title = None
        self.__infos = None
        self.__rootDir = None

    @property
    def mode(self):
        '''Download mode: Used for selective download'''
        return self.__mode

    @mode.setter
    def mode(self, mode):
        self.__mode = mode

    @property
    def cid(self):
        '''Curriculum ID'''
        return self.__cid
    
    @cid.setter
    def cid(self, cid):
        self.__cid = cid

    @property
    def title(self):
        '''Title of Course'''
        return self.__title
    
    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def infos(self):
        '''Analysis of course information'''
        return self.__infos

    @property
    def rootDir(self):
        return self.__rootDir

    @rootDir.setter
    def rootDir(self, rootDir):
        self.__rootDir = rootDir
    
    @infos.setter
    def infos(self, infos):
        self.__infos = infos

    @abstractmethod
    def _get_cid(self):
        pass
    
    @abstractmethod
    def _get_title(self):
        pass

    @abstractmethod
    def _get_infos(self):
        pass

    @abstractmethod
    def _download(self):
        pass

    @abstractmethod
    def set_mode(self):
        pass

    @abstractmethod
    def prepare(self, url):
        pass

    @abstractmethod
    def download(self):
        pass

    @classmethod
    def download_video(cls, video_url, video_name, video_dir):
        '''Download mp4 video file'''
        succeed = True
        if not cls.judge_file_existed(video_dir, video_name, '.mp4'):
            try:
                header =  request_head(video_url)
                size = float(header['Content-Length']) / (1024*1024)
                print("  |-{}  [mp4] size: {:.2f}M".format(cls.align(video_name,LENGTH), size))
                aria2_download_file(video_url, video_name+'.mp4', video_dir)
            except DownloadFailed:
                print("  |-{}  [mp4] Resources cannot be downloaded！".format(cls.align(video_name,LENGTH)))
                succeed = False
        else:
            print("  |-{}  [mp4] Has successfully downloaded！".format(cls.align(video_name,LENGTH)))
        return succeed

    @classmethod
    def download_pdf(cls, pdf_url, pdf_name, pdf_dir):
        '''download PDF '''
        succeed = True
        if not cls.judge_file_existed(pdf_dir, pdf_name, '.pdf'):
            try:
                aria2_download_file(pdf_url, pdf_name+'.pdf', pdf_dir)
                print("  |-{}  (pdf) Has successfully downloaded！".format(cls.align(pdf_name,LENGTH)))
            except DownloadFailed:
                print("  |-{}  (pdf) Resources cannot be downloaded！".format(cls.align(pdf_name,LENGTH)))
                succeed = False
        else:
            print("  |-{}  (pdf) Has successfully downloaded！".format(cls.align(pdf_name,LENGTH)))
        return succeed

    @classmethod
    def download_sub(cls, sub_url, sub_name, sub_dir):
        '''Download subtitles'''
        succeed = True
        if not cls.judge_file_existed(sub_dir, sub_name, '.srt'):
            try:
                aria2_download_file(sub_url, sub_name+'.srt', sub_dir)
            except DownloadFailed:
                succeed = False
        return succeed

    @staticmethod
    def judge_file_existed(dirname, filename, fmt):
        '''
        judge_file_existed(dirname, filename, fmt) 
        Determine whether there is a file that has been successfully downloaded in the DIRNAME directory to FMT and file name is FILENAME
        '''
        filepath = os.path.join(dirname, filename)
        exist1 = os.path.exists(filepath+fmt)
        exist2 = os.path.exists(filepath+fmt+'.aria2')
        return exist1 and not exist2

    @staticmethod
    def align(string, width):  #  Align the Chinese character string, cut off excess output at the same time
        '''
        align(string, width) According to the width width in the middle of the alignment character, it is mainly used for the middle of Chinese characters
        '''
        res = ""
        size = 0
        for ch in string:
            if (size+3 > width):
                break
            size += 1 if ord(ch) <= 127 else 2
            res += ch
        res += (width-size)*' '
        return res
