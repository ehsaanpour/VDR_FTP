# VDR_FTP
This project provides a simple graphical user interface (GUI) application for transferring files from a VDR (Video Disk Recorder) using FTP. The application is built with Python and the PySimpleGUI library.

**Features:**

*   Connect to a VDR via FTP.
*   List files available on the VDR.
*   Download individual files or all files from the VDR.
*   Simple and intuitive user interface.

**Requirements:**

*   Python 3.x
*   PySimpleGUI library (`pip install PySimpleGUI`)
*   A VDR with FTP enabled.

**Usage:**

1.  Run the `test.py` script.
2.  Enter the VDR's IP address, username, and password.
3.  Click "Login" to connect to the VDR.
4.  Once connected, the list of files on the VDR will be displayed.
5.  Select a file from the list and click "Download File" to download a single file, or click "Download All" to download all files.
6.  Choose the destination folder for the downloaded files.

**Files:**

*   `main.py`: Contains the main application logic for the VDR file transfer (This file seems to be an older version or a different attempt, as `test.py` contains the functional GUI). 
*   `test.py`: Contains the functional PySimpleGUI application for connecting to the VDR, listing files, and downloading files.
*   `Laptop.png`, `VDR.png`, `arrow.png`: Image files used in the GUI.
*   `README.md`: This readme file.
*   `.idx/dev.nix`, `.vscode/settings.json`: Configuration files.

**Attribution:**

All rights reserved for Ehsanpour.com and Hakamian.
