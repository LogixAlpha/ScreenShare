#!bin/bash

echo "Giving sudo priviliege to scrcpy.py"

cd ~/Downloads

unzip ScreenShare-main.zip && cd ScreenShare-main/

sudo pip install -r requirements.txt

sudo python scrcpy.py

echo "Done"
