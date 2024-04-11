### 				MOOC video download based on Python crawler [The open source code has stopped being maintained, and the software is still being maintained and updated]

##### 1. Project Description:

- The project environment is Windows10, Python3
- Use Python3.6 urllib3 module crawler, involving modules including standard libraries, third-party libraries and other open source components, which have been packaged into exe files
- Supports Mooc videos, subtitles, courseware downloads, courses are downloaded to the hard drive in the form of a directory tree, and supports Potplayer playback
- Supports China University, NetEase Cloud Classroom, Youdao Premium Class, Youdao Leading the World, Tencent Classroom, China Public Online School, New Oriental, Xiaoetong, Xuelang, Douyin Classroom, Bilibili Classroom, Gaotu Classroom, Tutu Classroom, Qianliao, Interest Island, Love Course, Xuetang Online, MOOC, Chaoxing Learning Network (Xueyin Online), Wisdom Tree, Smart Vocational Education, video course download of the top 20 MOOC online courses, the core download is called Aria2c
- Users can directly download [Xuewuzhi Downloader](https://github.com/PyJun/Mooc_Downloader/releases) under Release and install it for use.
- For information on the use of the downloader and related issues, click to view [Mooc Downloader Help Document](https://github.com/PyJun/Mooc_Downloader/wiki)

##### 2. Demo:

![demo1.png](http://xuewuzhi.cn/images/demo1.png)

![demo2.png](http://xuewuzhi.cn/images/demo2.png)

##### 4.project files

- Mooc_Main.py, 	the main program of the entire project, actually calls Mooc_Interface
- Mooc_Interface.py 	human-computer interaction interface module
- Mooc_Config.py 	Mooc configuration file
- Mooc_Base.py 		Mooc abstract base class
- Mooc_Potplayer.py 	is used to generate dpl files specifically for Potplayer playback
- Mooc_Request.py 	is a Mooc request library wrapped in urllib
- Mooc_Download.py 	calls the command interface for Aira2c download
- Icourses module 	package with love courses
   - Icourse_Base.py 	is the base class of icourse downloader, inherited from Mooc_Base
   - Icourse_Config.py 	configuration file
   - Icourse_Cuoc.py 	is a subcategory for downloading Icourse video open courses, http://www.icourses.cn/cuoc/
   - Icourse_Mooc.py 	is a subcategory for downloading Icourse resource sharing courses, http://www.icourses.cn/mooc/
- Icourse163 		module package about Chinese university MOOCs
   - Icourse163_Base.py The base class of Chinese University MOOC downloader, inherited from Mooc_Base
   - Icourse163_Config.py configuration file
   - Icourse163_Mooc.py A subclass of Chinese University MOOC downloader, inherited from Icourse163_Base.py

##### 5.Run the project

Please make sure you are in the root directory of the project, and then enter the following command in the terminal (python3 environment, no dependent third-party modules)

```powershell
python -m Mooc
```

##### 6.packaging instructions

1. First make sure that **pyinstaller** has been installed. If it is not installed, use pip to install it, open the terminal and enter:

   ```powershell
   pip install pyinstaller
   ```

2. Then enter the terminal in the root directory of the project:

    ```powershell
    pyinstallerMooc.spec
    ```

3. Finally, a **dist** folder will appear in the project root directory, and a **Mooc-3.4.0.exe** program will appear in the folder.

![package.png](http://xuewuzhi.cn/images/package.png)


##### 7. Precautions
The project code has not been updated for a long time. There is an exe file I packaged under Releases, which can be downloaded and used directly~
[This project is an early open source code, and the latest version of the code is not open source]
1. The new version of the code involves website crawling, parsing, and decryption. It is easy to lose harmony after being open sourced.
2. The new version involves too many module dependencies (including but not limited to nodejs, electron, ariac2, annie, ffmpeg, wkhtmltopdf and some self-compiled python dependent libraries), making it difficult to separate an independently usable open source version
3. There is really no energy to maintain two open source and closed source versions of the code at the same time.
4. This project is not a complete open source project. The software provided is virus-free and can be used for free (it also includes paid functions)
