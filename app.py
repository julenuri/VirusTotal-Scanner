import requests
import sys
import webbrowser
import winreg as wr

API_KEY = '#'


def install():
    scanner_reg = wr.CreateKey(
        wr.HKEY_CLASSES_ROOT,
        'exefile\\shell\\VirusTotalScanner'
    )
    wr.SetValue(scanner_reg, 'command', wr.REG_SZ, sys.argv[0] + ' %1')
    wr.CloseKey(scanner_reg)


def scan_file(exe_file):
    response = requests.post(
        'https://www.virustotal.com/vtapi/v2/file/scan',
        files={
            'file': (exe_file.split('\\')[-1], open(exe_file, 'rb'))
        },
        params={
            'apikey': API_KEY
        })
    json_response = response.json()
    webbrowser.open(json_response['permalink'])


if __name__ == "__main__":
    if len(sys.argv) == 1:
        install()
    else:
        scan_file(sys.argv[1])
