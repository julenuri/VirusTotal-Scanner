# VirusTotal-Scanner
Script to scan executable files using VirusTotal API, available from the windows context menu.

![Screenshoot](http://i.imgur.com/J2uklEA.png)

# How to install?

- Create account on [VirusTotal,com](https://virustotal.com/)
- Write Your API key in app.py (line 6)
- Install requirements
- Run: ```pyinstaller app.py --noconsole --onefile```
- Move app.exe file from ```dist``` directory to any place You want
- Run app.exe as an administrator (only one time, it needs to install registry key)

# How to use it?

Right click on any exe file (max 128 MB), click on  "VirusTotalScanner" and wait for report :-)

# Limits
[VirusTotal.com API Documentation](https://www.virustotal.com/pl/documentation/public-api/)
