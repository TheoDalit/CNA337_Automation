import os

class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip):
        # TODO -
        self.server_ip = server_ip

    def ping(self):
        # TODO - Use os module to ping the server
        response = os.system("ping -n 4 " + self.server_ip) #https://stackoverflow.com/questions/2953462/pinging-servers-in-python
        return self.server_ip
