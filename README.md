# LocalFileInclusion
 i built this tool while i was testing a site 
as DOING IT ONCE COOL, DOING IT TWICE SHAME ON ME.
# Screen Shots
<img src="https://i.ibb.co/0m2Pbpw/lfi.png" alt="LFI" border="0">

<img src="https://i.ibb.co/cQxZDrN/show.png" alt="LFI" border="0">

### HOW TO USE 
~~~~
Set a URL > https://www.site.com/page.php
~~~~
~~~~
Set the Resource > page.php?=./path/stuff
~~~~
~~~~
Set the AUTO mode [0] for False, [1] True > 0
~~~~

### DETAILS
~~~~
• Example of what the tool is able to handle : https://www.site.com/page.php?=stuff
                                           :https://www.site.com/page?=./path/stuff
~~~~

~~~~
• [Resource]The part 'page.php?=stuff' is an exaple of Resource or the Resource Path
~~~~

~~~~
• [url]The part 'https://www.site.com/page.php' is an example of an URL
~~~~

~~~~
• [Auto]By defulte it's False which means that the tool gonna run a simple test on the site
  If you gonna turn it on you should consider that the txt file LFI.txt is require for 
  trying to find any possible leak of information from the server
~~~~
