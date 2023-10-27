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

**pdfgui_tools** is a user interface tool developed in Qt and Python that integrates with **poppler-utils** and **PyPDF2** for PDF document management. It's a **simple** and **user-friendly** tool that includes various utilities such as merging PDFs, splitting PDFs, converting them to multimedia files like PNG or SVG, encrypting or decrypting, among other utilities included in pdfgui_tools.

<div align="center">
<p>pdfgui_tools
</div>

![1](./Screenshots/Screenshot_2.png?raw=true)

# Sections
### Install pdfgui_tools:
- [Debian-based distributions](#install-via-deb-package)
- [Arch-based distributions (AUR)](#install-from-aur-yay)
- [Install using a script](#install-using-a-script)

### Using pdfgui_tools:
- [Start using pdfgui_tools](#start-using-pdfgui_tools)

### Important:
- [Dependencies](#dependencies)
- [Report bugs or give suggestions](#report-bugs-or-give-suggestions)

## Install via deb package
To install pdfgui_tools, you will first need to download the **Debian package**, which can be found at the following link: 

<a href="https://github.com/TheWatcherMultiversal/pdfgui_tools/releases/download/v1.1.0/pdfgui_tools_stable-release_1.1.0_all.deb" target="_blank">📦 Download deb package</a>

Once we have our **Debian package** installed, simply execute the following command, and it will be downloaded to our system:

    sudo dpkg -i pdfgui_tools_stable-release_1.1.0_all.deb
    
- Note: If we find any missing dependencies, it's just a matter of installing them with the `sudo apt install -f` command

Now we just need to check if the program was installed correctly, for this we execute the following:

    pdfgui_tools

## Install from AUR (yay)
In case you are using an **Arch-based** distribution, you can download pdfgui_tools from **AUR** using `yay`:

    yay -S pdfgui_tools-bin

- <p>You can find the package at this <a href="https://aur.archlinux.org/packages/pdfgui_tools-bin">link</a>, thanks to <a href="https://github.com/begin-theadventure">begin-theadventure</a>.</p>

## Install using a script
If you do not have a Debian-based distribution or if you have a different package manager, you can use the installation script `./install.py`.

To do this, first make sure that the `./install.py` script have the necessary permissions to run on the system:

    chmod 755 ./install.py

Now we can install pdfgui_tools by running the installation script:

    ./install.py

- Note: To uninstall pdfgui_tools, you can use `./install.py --uninstall`  to remove pdfgui_tools from the system.

### poppler-utils

In a special case where your distribution doesn't include the **poppler-utils** package in its repositories, use the `--all` parameter of the installation script to include **poppler-utils** in the installation:

    ./install.py --all

- <p>The <b>poppler-utils</b> package included in the installation script is designed for the <b>amd64</b> architecture. If you need this package for a different architecture, we recommend checking the official <a href="https://poppler.freedesktop.org/" >poppler-utils</a> page and obtaining the source code.</p>
- If you need to uninstall everything, run `./install.py` again with the `--remove-all` parameter.

Now we just need to check if the program was installed correctly, for this we execute the following:

    pdfgui_tools

In case you encounter any errors while running the script, please read the error messages provided by the script. Additionally, you will need to install the necessary dependencies to run pdfgui_tools correctly.



## Start using pdfgui_tools
To start using pdfgui_tools, run the  `pdfgui_tools` command, and a window like the following should appear:

![1](./Screenshots/Screenshot_1.png?raw=true)

If you require assistance with the use of pdfgui_tools, you can check my blog or access help directly from the app by pressing the `F1` key.

## Dependencies
Before being able to use pdfgui_tools, you need to have the following **dependencies** installed on your system for the program to function properly:

- **poppler-utils**
- **python3-pypdf2**
- **python3-pyqt5**
- **qtbase5-dev**

## Report bugs or give suggestions
To notify errors in the program or give suggestions for it, write your request in the following email: <universepenguin@protonmail.com>
