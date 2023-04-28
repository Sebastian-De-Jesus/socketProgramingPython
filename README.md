# Python Socket Program:
Author: Sebastian Reyes
CLASS 471-(03) SPRING 2023

## Simple client-server, that allows the user to use the following commands.
**get**, **put**, **ls**, and lastly **quit**

### HOW TO USE
Download files on to desired computer,
Begin by starting *server.py* and indicating desired *port* number
EX. python3 server.py 5555

Next, start the *client.py* and indicated *ecs.fullerton.edu* and *port*
EX. python3 client.py ecs.fullerton.edu 5555

### BE ADVISED
Both client and server must use the same ports, server.py/client.py are both configured to 
use local host for their ip **127.0.0.1** becasue we are unable to bind to *fullerton.edu*

### ADDITIONALLY ITEMS to MENTION:
Server will remain on untill program is extied, while client can disconnect at anytime with the
*quit* command. This program does not do any type of checking to see if the CWD has the file you 
are asking to "get".

