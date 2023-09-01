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
try:
    from colorama import Fore
except ImportError:
    print("Install python3-colorama to be able to run the installation script.")

# ------------------------------------------------------------------ (*)
#   |
#   |
#   °-- Remove pdfgui_tools if it's previously installed:

print(Fore.YELLOW + '\r\nThe following command requires superuser privileges:' + Fore.RESET + ' sudo rm -r\r\n')
print(Fore.GREEN + 'Removing pdfgui_tools from the system' + Fore.RESET)

subprocess.run(f'sudo rm -r /usr/bin/pdfgui_tools /usr/share/pdfgui_tools/ /usr/share/applications/pdfgui_tools.desktop /usr/share/doc/pdfgui_tools/ /usr/share/man/man1/pdfgui_tools.1.gz', shell=True)

print(Fore.GREEN + 'pdfgui_tools was successfully removed' +  Fore.RESET)