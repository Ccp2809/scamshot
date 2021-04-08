# About Scamshot

Shotscam.py is a tool that SOC teams can use to further detect scam campaigns. 
If you came across a URL such as https://example.com/908712, Shotscam.py will iterate over the sequence of values that you indicate as an argument. 
In the case of the URL https://example.com/908712, the ideal sequence would be 1 (already specify in the code of the script) to 999999. 
When passing the arguments a keyword must be specified, and the tool will search for this keyword in the source code of the URL being analyzed. 
If the keyword is found, a match message will appear and a screenshot will be taken (for which width and height values must also be passed to the script).

# Usage

In the second version of shotscam.py you can iterate values not only at the end of the URL, but anywhere you want. The optional argument "-ext" for "extension" has been added.
        
usage: shotscam.py [-h] [-V] [--example] [--extension EXT] [--keyword KEYWORD]
                   [--width WIDTH] [--height HEIGHT] [--sequence SEQUENCE]
                   [--url URL]

optional arguments:
  -h, --help            show this help message and exit
  -V, --version         show program version
  --example, -e         show a brief explanation
  --extension EXT, -ext EXT
                        set the extension

Required arguments:
  --keyword KEYWORD, -k KEYWORD
                        set keyword to look for in the URL source code
  --width WIDTH, -w WIDTH
                        set output width
  --height HEIGHT, -hg HEIGHT
                        set output height
  --sequence SEQUENCE, -s SEQUENCE
                        set output sequence
  --url URL, -u URL     set target URL

  
# Usage example

If you want to iterate the values at the end of the URL, the following command should be taken as an example:

python shotscam.py -k JustEat -w 1920 -hg 1080 -s 292 -u "https://www.example.com/anything.ch?source=" -ext ""

If, on the other hand, you want to iterate in a URL parameter/path that is somewhere in the middle of the URL, the following kind of command should be used:

python shotscam.py -k JustEat -w 1920 -hg 1080 -s 292 -u "https://www.example.com/anything.ch?source=" -ext "/rest/of/the/url"
  
The order of the values as well as using double quotes is important, otherwise Python will complain.
  
# Future implementations
  
The intention is to add proxy and user-agent features as soon as possible.
