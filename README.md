<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=3c0c0c&height=130&section=header&text=PDF-GUI-Tools&fontSize=39&fontColor=fff&animation=twinkling&fontAlignY=35"/> 


[![GitHub release](https://img.shields.io/github/release/TheWatcherMultiversal/pdfgui_tools.svg)](https://github.com/TheWatcherMultiversal/pdfgui_tools/releases)
[![GitHub last commit](https://img.shields.io/github/last-commit/TheWatcherMultiversal/pdfgui_tools)](https://github.com/TheWatcherMultiversal/pdfgui_tools/)
[![GitHub license](https://img.shields.io/badge/license-GPLv3.0-brown)](https://github.com/TheWatcherMultiversal/pdfgui_tools/blob/main/LICENSE)
[![Poppler version](https://img.shields.io/badge/poppler--utils-23.08-orange)](https://poppler.freedesktop.org/)
[![PySide6 version](https://img.shields.io/badge/PySide6-6.6.0-green)](https://pypi.org/project/PySide6/)
[![PyPDF2 version](https://img.shields.io/badge/PyPDF2-1.26.0-red)](https://pypi.org/project/PyPDF2/)
[![PyMuPDF version](https://img.shields.io/badge/PyMuPDF-1.23.5-0b8c2c)](https://pypi.org/project/PyMuPDF/)

---

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

![1](./Screenshots/Screenshot_1.png?raw=true)

# Sections
### Install pdfgui_tools:
- [Debian-based distributions](#install-via-deb-package)
- [Arch-based distributions (AUR) - Unofficial](#install-from-aur-yay)
- [Install using a script](#install-using-a-script)

### Using pdfgui_tools:
- [Start using pdfgui_tools](#start-using-pdfgui_tools)

### Important:
- [Dependencies](#dependencies)
- [Report bugs or give suggestions](#report-bugs-or-give-suggestions)

## Install via deb package
To install pdfgui_tools, you will first need to download the **Debian package**, which can be found at the following link: 

<a href="https://github.com/TheWatcherMultiversal/pdfgui_tools/releases/download/v2.0.0/pdfgui_tools_stable-release_2.0.0_amd64.deb" target="_blank">📦 Download deb package</a>

> Note: This will download the default version with the `amd64` **architecture**. If you want to install the version with `all` architectures, it is recommended to read the [Dependencies](#dependencies) section.

Once we have our **Debian package** installed, simply execute the following command, and it will be downloaded to our system:

    sudo dpkg -i pdfgui_tools_stable-release_2.0.0_amd64.deb
    
> Note: If we find any missing dependencies, it's just a matter of installing them with the `sudo apt install -f` command

Now we just need to check if the program was installed correctly, for this we execute the following:

    pdfgui_tools

## Install from AUR (yay) - Unofficial
In case you are using an **Arch-based** distribution, you can download pdfgui_tools from **AUR** using `yay`:

    yay -S pdfgui_tools-bin

<p>You can find the package at this <a href="https://aur.archlinux.org/packages/pdfgui_tools-bin">link</a>, thanks to <a href="https://github.com/begin-theadventure">begin-theadventure</a>.</p>

## Install using a script
If you don't have a **Debian-based** distribution or don't want to install from the **AUR**, you can install **pdfgui_tools** using the installation script `./install.py`. Before starting, first install **python3-colorama** to avoid import conflicts

To do this, first make sure that the `./install.py` script have the necessary permissions to run on the system:

    chmod 755 ./install.py

Now we can install pdfgui_tools by running the installation script:

    ./install.py

If you want to install the version for **all architectures**, use the `--arch-all` option.

> Note: This will install the default version with the `x86_64` **architecture**. If you need to install the `all` **architecture** version, which contains the unpacked Python packages, you will need to install the dependencies. Refer to the [Dependencies](#dependencies) section for more information.

To **uninstall pdfgui_tools**, simply use the argument `-u` or `--uninstall` to perform this action.

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

![1](./Screenshots/Screenshot_2.png?raw=true)

If you need help or assistance navigating PDF GUI Tools, use the  `F1` key to display the help window.

## Dependencies
Before being able to use pdfgui_tools, you need to have the following **dependencies** installed on your system for the program to function properly:

#### Dependencies

<ul>
<li><a href="https://poppler.freedesktop.org/" target="_blank"><b>poppler-utils</b></a></li>
<li><a href="" target="_blank"><b>xdg-utils</b></a></li>
</ul>

#### Optional dependencies

<ul>
<li><a href="" target="_blank"><b>breeze-icon-theme (default)</b></a></li>
</ul>

> Note: A default **icon theme** that works with **Qt** is required to properly display the **pdfgui_tools interface**. In some distributions like **KDE**, this dependency is not necessary.

#### Python dependencies

<ul>
<li><a href="https://pypi.org/project/PyPDF2/" target="_blank"><b>PyPDF2 (1.26.0)</b></a></li>
<li><a href="https://pypi.org/project/PyMuPDF/" target="_blank"><b>PyMuPDF (1.23.5)</b></a></li>
<li><a href="https://pypi.org/project/PySide6/" target="_blank"><b>PySide6 (6.6.1)</b></a></li>
</ul>

> Note: Starting from version `2.0.0` of **pdfgui_tools**, for versions with the `amd64` or `x86_64` **architecture**, it is not necessary to install **Python-related dependencies** separately. pdfgui_tools is bundled with pyinstaller along with **all the necessary dependencies** to run. It will only require those dependencies that are not part of Python.

## Report bugs or give suggestions
To notify errors in the program or give suggestions for it, write your request in the following email: <universepenguin@protonmail.com>
