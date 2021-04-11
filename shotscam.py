
import requests
import webbrowser
import pyscreenshot
from datetime import datetime
import time
import argparse

print("""   
  _________.__            __   _________                      
 /   _____/|  |__   _____/  |_/   _____/ ____ _____    _____  
 \_____  \ |  |  \ /  _ \   __\_____  \_/ ___\ __  \  /     \ 
 /        \|   Y  (  <_> )  | /        \  \___/ __ \|  Y Y  \ 
/_______  /|___|  /\____/|__|/_______  /\___  >____  /__|_|  /
        \/      \/                   \/     \/     \/      \/
        """)

parser = argparse.ArgumentParser()
parser.add_argument("-V", "--version", help="show program version", action="store_true")
parser.add_argument("--example", "-e", help="show a brief explanation", action="store_true")
parser.add_argument("--extension", "-ext", action="store", dest="ext", help="set the extension", type=str, required=False)
requiredArguments = parser.add_argument_group("Required arguments")
requiredArguments.add_argument("--keyword", "-k", help="set keyword to look for in the URL source code", type=str)
requiredArguments.add_argument("--width", "-w", help="set output width", type=int)
requiredArguments.add_argument("--height", "-hg", help="set output height", type=int)
requiredArguments.add_argument("--sequence", "-s", help="set output sequence", type=int)
requiredArguments.add_argument("--url", "-u", help="set target URL", type=str)

args = parser.parse_args()

if args.version:
    print("v2")
elif args.example:
    print("For URL 'http://example.com/98698' you must input the URL value 'http://example.com/'. The sequence (s) in this case would be 99999.")
elif args.width:
    screen_width = "%i" % args.width
elif args.height:
    screen_height = "%i" % args.height
elif args.sequence:
    sequence = "%i" % args.sequence
elif args.url:
    url = "%s" % args.url
elif args.ext:
    ext = "%s" % args.ext
else:
    print("Invalid argument. Use --help or -h to see the valid options")
    exit(2)

#base_url = 'https://www.vouchersaddict.com/cgi-bin/wingame.pl?source_pk=5617&partner_pk=312&wingame_pk=66&freetest_pk='
current_date = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
screenshot_extension = ".png"


class Colors:
    OK_CYAN = "\033[96m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    Color_Off = "\033[0m"


def url_check():
    if status == 404:
        print(url, "is not up, returned ", status)
    elif status == 200:
        print(url, "is up, returned ", status)
        source_code = requests.get(url).text
        if args.keyword in source_code:
            print(Colors.OK_CYAN + url, "is a match!")
            webbrowser.open(url)
            print("Taking screenshot..." + Colors.Color_Off)
            time.sleep(5)
            screenshot = pyscreenshot.grab(bbox=(0, 35, args.width, args.height))
            screenshot.save(current_date + screenshot_extension)
        else:
            print(Colors.RED + url, "is not a match." + Colors.Color_Off)

    elif status == 301 or 302:
        print(Colors.YELLOW + url, "is a redirecting URL." + Colors.Color_Off)
    else:
        print(url, "returned ", status)


number = 0

while number <= args.sequence:

    if args.ext == "":
        url = args.url+str(number)
        status = requests.get(url).status_code
        number = number+1
        url_check()
    else:
        url = args.url+str(number)+args.ext
        status = requests.get(url).status_code
        number = number+1
        url_check()
