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
import sys
try:
    from colorama import Fore
except ImportError:
    print("Install python3-colorama to be able to run the installation script.")

# ------------------------------------------------------------------ (*)
#   |
#   |
#   °-- Defining the variable names:

version     = '1.0.4'
package     = f'pdfgui_tools_stable-release_{version}_all.tar.gz'
url_package = f'https://github.com/TheWatcherMultiversal/pdfgui_tools/releases/download/v{version}/{package}'

# ------------------------------------------------------------------ (*)
#   |
#   |
#   °-- Download pdfgui_tools from the specified URL:

print(Fore.GREEN + f"\r\nInstall pdfgui_tools_stable-release_{version}_tar.gz\r\n" + Fore.RESET)

try:
    subprocess.run([f'wget {url_package}'], check=True, shell=True)
except subprocess.CalledProcessError:
    print(Fore.RED + 'Error:' + Fore.RESET + ' command wget or source not found.')
    sys.exit(1)

# ------------------------------------------------------------------ (*)
#   |
#   |
#   °-- Extract the tar.gz file:

print(Fore.GREEN + 'Extracting content...\r\n' + Fore.RESET)

try:
    subprocess.run([f'tar -xvzf {package}'], check=True, shell=True)
except subprocess.CalledProcessError:
    subprocess.run([f'rm {package}'], check=True, shell=True)
    print(Fore.RED + 'Error:' + Fore.RESET + ' the package could not be extracted.')
    sys.exit(2)

# ------------------------------------------------------------------ (*)
#   |
#   |
#   °-- Remove pdfgui_tools if it's previously installed:

print(Fore.YELLOW + '\r\nThe following command requires superuser privileges:' + Fore.RESET + ' sudo rm -r\r\n')
print(Fore.GREEN + 'Removing existing files and installing new ones...' + Fore.RESET)

subprocess.run(f'sudo rm -r /usr/bin/pdfgui_tools /usr/share/pdfgui_tools/ /usr/share/applications/pdfgui_tools.desktop /usr/share/doc/pdfgui_tools/ /usr/share/man/man1/pdfgui_tools.1.gz', shell=True)

# ------------------------------------------------------------------ (*)
#   |
#   |
#   °-- Build the package on the system:

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
print(Fore.GREEN + '\r\nInstallation complete' + Fore.RESET + ', run ' + Fore.YELLOW + './uninstall.py' + Fore.RESET + ' to remove pdfgui_tools\r\n')
