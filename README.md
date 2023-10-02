<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=3c0c0c&height=130&section=header&text=PDF-GUI-Tools&fontSize=39&fontColor=fff&animation=twinkling&fontAlignY=35"/> 

<div align="center"> 
<p>Technologies used:</p>
<a href="#!" target="_blank"><img src="https://img.shields.io/badge/-Linux-1e1f20?style=for-the-badge&logo=linux&logoColor=yellow"></a>
<a href="#!" target="_blank"><img src="https://img.shields.io/badge/-Qt-052F15?style=for-the-badge&logo=qt&logoColor=green"></a>
<a href="#!" target="_blank"><img src="https://img.shields.io/badge/-Python-141b4a?style=for-the-badge&logo=python&logoColor=green"></a>
<a href="#!" target="_blank"><img src="https://img.shields.io/badge/-Bash-082405?style=for-the-badge&logo=gnu bash&logoColor=white"></a>
<a href="#!" target="_blank"><img src="https://img.shields.io/badge/-Css-024550?style=for-the-badge&logo=css3&logoColor=cyan"></a>
<a href="#!" target="_blank"><img src="https://img.shields.io/badge/-Git-161618?style=for-the-badge&logo=git&logoColor=orange"></a>
</div>


<div align="center">
<h1>pdfgui_tools
</div>
<div align="center">
<img src="./icons/pdfguitools.svg" width="100">
</div>

**pdfgui_tools** is a user interface tool developed in Qt and Python that integrates with **poppler-utils** for PDF document management. This simple and user-friendly tool allows you to merge PDF files, convert PDF to HTML, as well as convert PDF to text. Additionally, in the near future, more functions with additional features will be added.

## Install via deb package
To install pdfgui_tools, you will first need to download the **Debian package**, which can be found at the following link: 

<a href="https://github.com/TheWatcherMultiversal/pdfgui_tools/releases/download/v1.0.4/pdfgui_tools_stable-release_1.0.4_all.deb" target="_blank">📦 Download deb package</a>

Once we have our **Debian package** installed, simply execute the following command, and it will be downloaded to our system:

    sudo dpkg -i pdfgui_tools_stable-release_1.0.4_all.deb
    
- Note: If we find any missing dependencies, it's just a matter of installing them with the `sudo apt install -f` command

Now we just need to check if the program was installed correctly, for this we execute the following:

    pdfgui_tools

## Install using a script
If you do not have a Debian-based distribution or if you have a different package manager, you can use the installation script `./install.py`.

To do this, first make sure that the `./install.py` script and the `./uninstall.py` script have the necessary permissions to run on the system:

    chmod 755 ./install.py ./uninstall.py

Now we can install pdfgui_tools by running the installation script:

    ./install.py

- Note: You can uninstall pdfgui_tools from the system using the `./uninstall.py` script.

### poppler-utils

In a special case where your distribution doesn't include the **poppler-utils** package in its repositories, use the `--all` parameter of the installation script to include **poppler-utils** in the installation:

    ./install.py --all
    
- Note: If you need to uninstall everything, run `./uninstall.py` again with the `--all` parameter.

Now we just need to check if the program was installed correctly, for this we execute the following:

    pdfgui_tools

In case you encounter any errors while running the script, please read the error messages provided by the script. Additionally, you will need to install the necessary dependencies to run pdfgui_tools correctly.

## Start using pdfgui_tools
To start using pdfgui_tools, run the  `pdfgui_tools` command, and a window like the following should appear:

![1](./Screenshots/Screenshot_1.png?raw=true)

As you can see, it's a very simple window that displays the functions the application can perform.

If we select an option, we will see a window like the following:

![1](./Screenshots/Screenshot_2.png?raw=true)

A window appears displaying the application's function. Each window is similar, and you can explore each function as needed. Additionally, if you require assistance, you can access a help window using the `F1` key.

## Dependencies
Before being able to use pdfgui_tools, you need to have the following **dependencies** installed on your system for the program to function properly:

- **poppler-utils**
- **python3-pyqt5**
- **qtbase5-dev**

## Report bugs or give suggestions
To notify errors in the program or give suggestions for it, write your request in the following email: <universepenguin@protonmail.com>
