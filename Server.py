import os
import paramiko

class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip):
        # TODO -
        self.server_ip = server_ip

    def ping(self):
        # TODO - Use os module to ping the server
        response = os.system("ping -n 4 " + self.server_ip) #https://stackoverflow.com/questions/2953462/pinging-servers-in-python
        return self.server_ip

ssh = paramiko.SSHClient() # https://mainlydata.kubadev.com/python/using-paramiko-to-control-an-ec2-instance/
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('3.139.89.21', username='ec2-user', password='', key_filename=r'C:\Users\hombo\.ssh\id_rsa') # https://stackoverflow.com/questions/37400974/unicode-error-unicodeescape-codec-cant-decode-bytes-in-position-2-3-trunca
stdin, stdout, stderr = ssh.exec_command('sudo yum update; sudo yum upgrade')
stdin.flush()

data = stdout.read().splitlines()
for line in data:
    print(line)

ssh.close()

