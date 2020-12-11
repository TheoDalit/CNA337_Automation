# This is the template code for the CNA337 Final Project
# Theodore Dalit, tfdalit@student.rtc.edu
# CNA 337 Fall 2020

from Server import Server
def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.2 by Theo")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    # TODO - Create a Server object
    ec2 = Server('3.139.89.21')
    # TODO - Call Ping method and print the results
    # print(ec2.ping())

