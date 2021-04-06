# scamshot

Shotscam.py is a tool that SOC teams can use to further detect scam campaigns. 
If you came across a URL such as https://example.com/908712, Shotscam.py will iterate over the sequence of values that you indicate as an argument. 
In the case of the URL https://example.com/908712, the ideal sequence would be 1 (already specify in the code of the script) to 999999. 
When passing the arguments a keyword must be specified, and the tool will search for this keyword in the source code of the URL being analyzed. 
If the keyword is found, a match message will appear and a screenshot will be taken (for which width and height values must also be passed to the script).
