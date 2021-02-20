Requirements:
Python 3.7(not later)
Internet Connectivity
Python Modules for Audio Play, Tkinter, gtts module, aiml module,gTTS pyttsx3 playsound library, requests module, Beautiful Soup, html5lib.



Special Features:
1)GUI Interface
2)Audio Output
3)Live data display of covid cases using Web Scraping of Worldometer
4)Try searching :1)"nearest hospital"(Pattern is * HOSPITAL)
	       2)"who will win techweek"
	       3)"when will college reopen"


Special Considerations:
1) Due to simultaneous making of mp3 audio file for audio output and web scraping in case of covid cases, the response of CoBot is little slow.
2) The default pattern of "*" fails on some occasions. After it fails once, try putting same input again and it will work.
We were unable to find reasons for the same.
3)For output of covid cases user will have to input type of cases and location(India or world). Ex: Number of "Active cases" in "India",
Number of "confirmed cases" in "India". But for every such input, bot will respond same by giving live details. 
4) While the bot is printing output on GUI chat area after audio output it is recomended to not hover cursor over it or better keep it stationary.  