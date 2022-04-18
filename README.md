
## Usage

Note: TRY RUNNING GUI before installing Librarys! -JB
Note: Most Kali installations come with the librarys pre installed! -JB
Note: If you are missing packages, please follow installation commands: -JB

```sh
python3 -m keyring --disable
```
```sh
pip install pillow
```
```sh
python3 -m pip install image
```
```sh
sudo apt-get install python3-tk
```
```sh
sudo apt-get install python3-pil python3-pil.imagetk
```

To run GUI

```sh
cd SyncDemo
```
```sh
python3 gui.py
```

## Functionality Implemented SYNC
We implemented a graphical User interface that has 2 users (Analyst 1, Analyst 2) where Analyst 1 holds file information and a picture of a fully implemented vehicle with nodes. Analyst 2 on the other hand has nothing (abscent file and empty vehicle). You can verify this buy pressing buttons Analyst_1 File and Analyst_2 file. Once you press the sync button the files essentially get copied over to Analyst 2 and his vehicle gets filled up with nodes. Closing the program will reset Analyst_2 files for demonstration purposes. -JB

## Status
Current version is V1.0 - JB

## What we learned
Creating a GUI is much easier than expected, using tools such as Tkinter - JB

Creating a program that navigates directories in a Windows OS is much different than navigating in a Linux environment. -JB

The sync process is much easier than expected, it really is just coping over files to different directories. - VH

Images in GUI’s is actually kind of difficult, you must use different library’s such as PIL to set images appropriately this can be time costly when doing the actual implementation of the software – JB

This was a good prototype into determining what and how we are going to complete the GUI. -VH
