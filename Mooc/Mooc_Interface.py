'''
    Mooc human-computer interaction interface function
'''

import os
import re
if __package__ is None:
    import sys
    sys.path.append('.\\')
    sys.path.append("..\\")
from Mooc.Mooc_Config import *
from Mooc.Mooc_Request import *
from Mooc.Mooc_Download import *
from Mooc.Icourse163.Icourse163_Mooc import *
from Mooc.Icourses.Icourse_Cuoc import *
from Mooc.Icourses.Icourse_Mooc import *

__all__ = [
    "mooc_interface"
]

# Mooc class corresponding to the course name
courses_mooc = {
    "icourse163_mooc": Icourse163_Mooc,
    "icourse_cuoc": Icourse_Cuoc, 
    "icourse_mooc": Icourse_Mooc
}

def mooc_interface():
    try:
        while True:
            os.system("cls")
            print("\t"+"="*91)
            print('\t|\t\t     MOOC downloader (free version v3.4.2)      \tQQ group: {:^27s} |'.format(__QQgroup__))
            print("\t|\t\t    icourse163.org, icourses.cn    \tMail: {:^27s} |".format(__email__))
            print("\t"+"="*91)
            print("\t{:^90}".format("Github: https://github.com/PyJun/Mooc_Downloader"))
            print("\t{:^90}".format("blog: https://blog.csdn.net/qq_16166591/article/details/85249743"))
            print("\t{:^90}".format("Download path: "+PATH))
            urlstr = None
            while not urlstr:
                try:
                    urlstr = input('\nEnter a video course website (Q exit): ')
                except KeyboardInterrupt:
                    print()
            if urlstr == 'q':
                break
            mooc = match_mooc(urlstr)
            if not mooc:
                input("The link link of the video course is illegal, please return to the car ...")
                continue
            if not mooc.set_mode():
                continue
            print("Linking resources......")
            try:
                mooc.prepare(urlstr)
            except RequestFailed:
                print("Network request abnormalities！")
                input("Please press the Enter key to return to the main interface...")
                continue
            while True:
                try:
                    isdownload = mooc.download()
                    if isdownload:
                        print('"{}" Download!'.format(mooc.title))
                        print("Download path: {}".format(mooc.rootDir))
                        os.startfile(mooc.rootDir)
                    else:
                        print('"{}" No class yet！'.format(mooc.title))
                    input("Please press the Enter key to return to the main interface...")
                    break
                except (RequestFailed, DownloadFailed) as err:
                    if isinstance(err, RequestFailed):
                        print("Network request abnormalities！")
                    else:
                        print("File download is abnormal！")
                    if inquire():
                        continue
                    else:
                        break
                except KeyboardInterrupt:
                    print()
                    if inquire():
                        continue
                    else:
                        break
                except:
                    print("The program is abnormally exited, hoping to feedback the author！")
                    return
    except KeyboardInterrupt:
        input("Program exit...")
    finally:
        # if (input("\nBrother, younger sister, take a reward and leave again …(⊙_⊙)… [y/n]: ") != 'n'):
        #     os.startfile(alipay_path)
        os.system("pause")

def inquire():
    redown = None
    while redown not in ('y','n'):
        try: 
            redown = input("Whether to continue[y/n]: ")
        except (KeyboardInterrupt, EOFError):
            print()
    return redown=='y'

def match_mooc(url):
    mooc = None
    for mooc_name in courses_mooc:
        if courses_re.get(mooc_name).match(url):
            mooc = courses_mooc.get(mooc_name)()
            break
    return mooc

def main():
    mooc_interface()

if __name__ == '__main__':
    main()
