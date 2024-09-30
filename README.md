### This program is a command line chat application that leverages TCP Sockets and threading to deal with multiple users' interactions.
---
## Difficulties faced:
- figuring out how to test the application by running the program from ther server and client side in multiple terminals
- how to get the specific client socket for private messaging from only the username. I solved this by creating another dictionary that connected the username to the socket, so when the user gives the username for the direct message, I am able to use the dictionary to access the appropriate client socket
---
## To use:
- in the terminal, navigate to the folder HW1
- start the server by running "python server.py"
- After starting the server, clients are now ready to join
- Open another terminal for each client and navigate to the same folder
- join the server by running "python client.py"
- The client will then be prompted to input a username
- from here they can type any message to broadcast to all other users, they can type "/private <username> <message>" to send a private message, or they can type "/quit" to quit the application
