'''
    Mooc Configuration file of the general project
'''

import sys
import os
import re


# Constant, fixed parameter
__QQgroup__ = "196020837"
__email__  = "py.jun@qq.com"
if hasattr(sys, 'frozen'):
    PATH = os.path.dirname(sys.executable)
else:
    PATH = os.path.dirname(os.path.abspath(__file__))  # Program current path
winre = re.compile(r'[?*|<>:"/\\\s]')  # windoes File illegal character matching
WIN_LENGTH = 64
TIMEOUT = 60   # Request timeout time
PLAYLIST = 'playlist.dpl'
PALYBACK = 'DPL_PYJUN'
BATNAME = 'Fix the playlist.bat'
BATSTRING = '''\
@echo off
copy {0} {1}
echo Successful repair“{1}”
echo Please use the Potplayer player to open "{1}" to watch the video (not installed Potplayer to download and install it by yourself)
pause
'''.format(PALYBACK, PLAYLIST)
LENGTH = 80

# Variables, modified parameters
download_speed = "0"
if getattr(sys, 'frozen', False): #Whether to pack
    aria2_path = os.path.join(sys._MEIPASS, "aria2c.exe")
    alipay_path = os.path.join(sys._MEIPASS, "Alipay.jpg")
else:
    aria2_path = os.path.join(PATH, "aria2c.exe")
    alipay_path = os.path.join(PATH, "Alipay.jpg")
aira2_cmd = '%s --header "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36 -- fUcIvJ01pZVQhNq23lXm9gjazkeonsCx" --check-certificate=false -x 16 -s 64 -j 64 -k 2M --disk-cache 128M --max-overall-download-limit %s "{url:}" -d "{dirname:}" -o "{filename:}"'%(aria2_path, download_speed)

# Demand matching of course links
courses_re = {
    "icourse163_mooc": re.compile(r'\s*https?://www.icourse163.org/((learn)|(course))/(.*?)(#/.*)?$'),
    "icourse_cuoc": re.compile(r'\s*https?://www.icourses.cn/web/sword/portal/videoDetail\?courseId=([\w-]*)'), 
    "icourse_mooc": re.compile(r'\s*((https?://www.icourses.cn/sCourse/course_(\d+).html)|'
                        r'(https?://www.icourses.cn/web/sword/portal/shareDetails\?cId=(\d+)))')
}

__all__ = [
    "__QQgroup__", "__email__", "PATH", "winre", "TIMEOUT", "PLAYLIST", "PALYBACK", 
    "BATNAME", "BATSTRING", "LENGTH", "WIN_LENGTH", 

    "download_speed", "aria2_path", "aira2_cmd", "courses_re", "alipay_path"
]
