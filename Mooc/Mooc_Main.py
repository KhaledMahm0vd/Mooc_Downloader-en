'''
Mooc downloader main program

     Author: PyJun
     Email: py.jun@qq.com
'''

if __package__ is None:
    import sys
    sys.path.append('.\\')
    sys.path.append('..\\')
from Mooc.Mooc_Interface import *

def main():
    try:
        mooc_interface()
    except:
        pass

if __name__ == '__main__':
    main()
