#! /usr/bin/python3
#
#   Uninstall pdfgui_tools
#
#   PDF GUI Tools | pdfgui_tools uninstall script
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
try:
    from colorama import Fore
except ImportError:
    print("Install python3-colorama to be able to run the uninstall script.")

# ----------------------------------------------------------------------------------------------------------------
#   |
#   |
#   °-- Argument:
parser = argparse.ArgumentParser()
parser.add_argument('--all', action='store_true', help='Incorporate poppler-utils into the uninstall script')
args = parser.parse_args()


# ------------------------------------------------------------------ (*)
#   |
#   |
#   °-- Remove pdfgui_tools if it's previously installed:

print(Fore.YELLOW + '\r\nThe following command requires superuser privileges:' + Fore.RESET + ' sudo rm -r\r\n')
print(Fore.GREEN + 'Removing pdfgui_tools from the system...' + Fore.RESET)

subprocess.run(f'sudo rm -r /usr/bin/pdfgui_tools /usr/share/pdfgui_tools/ /usr/share/applications/pdfgui_tools.desktop /usr/share/doc/pdfgui_tools/ /usr/share/man/man1/pdfgui_tools.1.gz', shell=True)

print(Fore.GREEN + '\r\npdfgui_tools was successfully removed' +  Fore.RESET)

# ------------------------------------------------------------------ (*)
#   |
#   |
#   °-- Remove poppler-utils if it's previously installed:

if args.all:
    
    bin_packages = ['pdfattach', 'pdfdetach', 'pdffonts', 'pdfimages', 'pdfinfo', 'pdfseparate', 'pdfsig', 'pdftocairo', 'pdftohtml', 'pdftoppm', 'pdftops', 'pdftotext', 'pdfunite']

    for i in bin_packages:
        subprocess.run(f'sudo rm -r /usr/bin/{i} /usr/share/man/man1/{i}.1.gz', shell=True)
            
    subprocess.run(f'sudo rm -r /usr/share/doc/poppler-utils', shell=True)

    print(Fore.GREEN + '\r\npoppler-utils was successfully removed' +  Fore.RESET)