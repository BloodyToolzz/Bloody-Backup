@echo off
pip install -r requirements.txt
echo Requirements installed
ping localhost -n 2 >nul
echo python Bloody Backup.py >> start.bat