

!TRY RUNNING GUI before installing Librarys..!
!Most Kali installations come with the librarys pre installed.!

IF you are missing packages, please follow installation commands:

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


What we learned

•    Creating a GUI is much easier than expected, using tools such as Tkinter - JB
•    Creating a program that navigates directories in a Windows OS is much different than navigating in a Linux environment. -JB
•    The sync process is much easier than expected, it really is just coping over files to different directories. - VH
•    Images in GUI’s is actually kind of difficult, you must use different library’s such as PIL to set images appropriately this can be time costly when doing the          actual implementation of the software – JB
•    This was a good prototype into determining what and how we are going to complete the GUI.
