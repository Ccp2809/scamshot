
import requests
import webbrowser
import pyscreenshot
from datetime import datetime
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-V", "--version", help="show program version", action="store_true")
parser.add_argument("--example", "-e", help="show a brief explanation", action="store_true")
requiredArguments = parser.add_argument_group("Required arguments")
requiredArguments.add_argument("--keyword", "-k", help="set keyword to look for in the URL source code", type=str)
requiredArguments.add_argument("--width", "-w", help="set output width", type=int)
requiredArguments.add_argument("--height", "-hg", help="set output height", type=int)
requiredArguments.add_argument("--sequence", "-s", help="set output sequence", type=int)
requiredArguments.add_argument("--url", "-u", help="set target URL", type=str)

args = parser.parse_args()  # Reads arguments from the command line

if args.version:
    print("v1")
elif args.example:
    print("For URL 'http://example.com/98698' you must input the URL value 'http://example.com/' enclosed within double quotes. The sequence (s) in this case would be 99999.")
elif args.width:
    screen_width = "%i" % args.width
elif args.height:
    screen_height = "%i" % args.height
elif args.sequence:
    sequence = "%i" % args.sequence
elif args.url:
    url = "%s" % args.url
else:
    print("Invalid argument. Use --help or -h to see the valid options")
    exit(2)

current_date = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
screenshot_extension = ".png"

for number in range(290, args.sequence+1):
    url = args.url+str(number)
    status = requests.get(url).status_code

    if status == 404:
        print(url, "is not up, returned ", status)
    elif status == 200:
        print(url, "is up, returned ", status)
        source_code = requests.get(url).text
        if args.keyword in source_code:
            print(url, "is a match!")
            webbrowser.open(url)
            print("Taking screenshot...")
            time.sleep(5)
            screenshot = pyscreenshot.grab(bbox=(0, 35, args.width, args.height))
            screenshot.save(current_date + screenshot_extension)
        else:
            print(url, "is not a match.")

    elif status == 301 or 302:
        print(url, "is a redirecting URL, returned ", status)
    else:
        print(url, "returned ", status)
