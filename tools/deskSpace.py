#deskSpace.py
# alot to do
import os
import webbrowser

def openDir(dir) -> None:
   print(dir)
   os.system(dir)

def OpenSites(site) -> None:
   print("Opening: ", site)
   webbrowser.open_new_tab(site)  # Go to example.com

if __name__ == "__main__":
   openDir("code")
   openDir("C:\\Users\\Tgang\\AppData\\Local\\Obsidian\\Obsidian.exe")
   OpenSites("http://192.168.1.173:7575/board")
   openDir("C:\\Users\\Tgang\\AppData\\Roaming\\Spotify\\Spotify.exe")