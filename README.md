# About Scamshot

Shotscam.py is a tool that SOC teams can use to further detect scam campaigns. 
If you came across a URL such as https://example.com/908712, Shotscam.py will iterate over the sequence of values that you indicate as an argument. 
In the case of the URL https://example.com/908712, the ideal sequence would be 1 (already specify in the code of the script) to 999999. 
When passing the arguments a keyword must be specified, and the tool will search for this keyword in the source code of the URL being analyzed. 
If the keyword is found, a match message will appear and a screenshot will be taken (for which width and height values must also be passed to the script).

# Usage

shotscam.py [-h] [-V] [--example] [--keyword KEYWORD] [--width WIDTH]
                   [--height HEIGHT] [--sequence SEQUENCE] [--url URL]

"shotscam.py --help" will show you what the optional and required arguments are.
  
# Usage example
  
python shotscam.py -k JustEat -w 1920 -hg 1080 -s 292 -u "https://www.example.com/anything.ch?source="
  
The order of the values as well as using double quotes is important, otherwise Python will complain.
  
# Limitations
  
Right now the script only works with URLs that have the numeric value over which the tool will iterate at the end of the URL. I am currently working on
making this feature more flexible as well as on including proxy capabilities.
