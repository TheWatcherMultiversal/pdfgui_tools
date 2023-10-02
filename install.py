#! /usr/bin/python3
#
#   Installer pdfgui_tools
#
#   PDF GUI Tools | pdfgui_tools installation script
#   GitHub: https://github.com/TheWatcherMultiversal/pdfgui_tools
#
#   License: GPLv3 (GNU/General Public License version 3.0)
#
# ------------------------------------------------------------------ (*)
#   |
#   |
#   °-- Include modules:

import subprocess
import argparse
import sys
try:
    from colorama import Fore
except ImportError:
    print("Install python3-colorama to be able to run the installation script.")

# ----------------------------------------------------------------------------------------------------------------
#   |
#   |
#   °-- Argument:
parser = argparse.ArgumentParser()
parser.add_argument('--all', action='store_true', help='Incorporate poppler-utils into the installation script')
args = parser.parse_args()


# -----------------------------------------------------------------------------------------------------------------
#   |
#   |
#   °-- Defining the variable names:

version         = '1.0.4'
version_poppler = '23.08'

package_pdfgui  = f'pdfgui_tools_stable-release_{version}_all.tar.gz'
package_poppler = f'poppler-utils_{version_poppler}_amd64.tar.gz'

url_package_pdfgui  = f'https://github.com/TheWatcherMultiversal/pdfgui_tools/releases/download/v{version}/{package_pdfgui}'
url_package_poppler = f'https://github.com/TheWatcherMultiversal/pdfgui_tools/releases/download/v{version}/{package_poppler}'


# ------------------------------------------------------------------------------------------------------------------------------


def install_targz(package : str, url : str):
    # ----> Download tar.gz from the specified URL <---- #

    print(Fore.GREEN + f"\r\nInstall {package}\r\n" + Fore.RESET)

    try:
        subprocess.run([f'wget {url}'], check=True, shell=True)

    except subprocess.CalledProcessError:
        print(Fore.RED + 'Error:' + Fore.RESET + ' command wget or source not found.')
        sys.exit(1)

    # ---> Extract the tar.gz file <---- #

    print(Fore.GREEN + 'Extracting content...\r\n' + Fore.RESET)

    try:
        subprocess.run([f'tar -xvzf {package}'], check=True, shell=True)

    except subprocess.CalledProcessError:
        subprocess.run([f'rm {package}'], check=True, shell=True)
        print(Fore.RED + 'Error:' + Fore.RESET + ' the package could not be extracted.')
        sys.exit(2)

    # ----> Remove package if it's previously installed <---- #

    print(Fore.YELLOW + '\r\nThe following command requires superuser privileges:' + Fore.RESET + ' sudo rm -r\r\n')
    print(Fore.GREEN + 'Removing existing files and installing new ones...' + Fore.RESET)

    if package == package_pdfgui:
        subprocess.run(f'sudo rm -r /usr/bin/pdfgui_tools /usr/share/pdfgui_tools/ /usr/share/applications/pdfgui_tools.desktop /usr/share/doc/pdfgui_tools/ /usr/share/man/man1/pdfgui_tools.1.gz', shell=True)

    elif package == package_poppler:
        bin_packages = ['pdfattach', 'pdfdetach', 'pdffonts', 'pdfimages', 'pdfinfo', 'pdfseparate', 'pdfsig', 'pdftocairo', 'pdftohtml', 'pdftoppm', 'pdftops', 'pdftotext', 'pdfunite']

        for i in bin_packages:
            subprocess.run(f'sudo rm -r /usr/bin/{i} /usr/share/man/man1/{i}.1.gz', shell=True)
        
        subprocess.run(f'sudo rm -r /usr/share/doc/poppler-utils', shell=True)

    # ----> Build the package on the system <----

    print(Fore.YELLOW + '\r\nThe following command requires superuser privileges:' + Fore.RESET + ' sudo cp -R -n\r\n')
    print(Fore.GREEN + 'Copying files to their corresponding paths...' + Fore.RESET)

    try:
        subprocess.run([f'sudo cp -R -n {package[:-7]}/usr/ /'], check=True, shell=True)

    except subprocess.CalledProcessError:
        subprocess.run([f'rm -r {package} {package[:-7]}'], check=True, shell=True)
        print(Fore.RED + 'Error:' + Fore.RESET + ' error copying files to the corresponding paths.')
        sys.exit(3)

    # Remove the files generated during the installation
    subprocess.run(f'rm -r {package[:-7]} {package}', shell=True)
    print(Fore.GREEN + '\r\nInstallation complete' + Fore.RESET + ', run ' + Fore.YELLOW + './uninstall.py' + Fore.RESET + f' to remove {package}\r\n')

# ------------------------------------------------------------------------------------------------------------------------------------------------------
#   |
#   |
#   °-- Install pdfgui_tools:
install_targz(package_pdfgui ,url_package_pdfgui)

if args.all:
    install_targz(package_poppler, url_package_poppler)