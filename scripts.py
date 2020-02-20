#!/usr/bin/env python

import sys
import paramiko
import os
import getpass
import time
import datetime
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


try:
    import env_user
except (SyntaxError, ModuleNotFoundError):
    print("Invalid input in env_file. Please complete the required fields in the proper format.")
    sys.exit(1)


__author__ = "remandal"
__version__ = "0.1"
__copyright__ = "Copyright (c) 2020."
__license__ = "GNU Public License, Version 3"


#if len(sys.argv) < 4:
#    print("args missing")
#    sys.exit(1)


hostname = "10.127.196.249"
password = "Apple!23"
command = "show clock"

username = "admin"
port = 22



def main():

    try:
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.WarningPolicy)

        client.connect(hostname=hostname, port=port, username=username, password=password)

        stdin, stdout, stderr = client.exec_command(command)
        print stdout.read(),

    finally:
        client.close()

    #try:
    #    t = paramiko.Transport((hostname, port))
    #    t.connect(username=username, password=password)
    #    sftp = paramiko.SFTPClient.from_transport(t)
    #    sftp.get(source, dest)

    #finally:
    #    t.close()
    # ssh_demo.py

    Email_password = getpass.getpass(
        prompt="Please enter the sender email password: ")
    while True:
        print("%s: Starting the ise monitoring script using probe to %s." % (
            str(datetime.datetime.now()), probe_address))

        failure_count = 0
        while failure_count < 3:
            try:
                probe = paramiko.SSHClient()
                probe.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                probe.connect(probe_address, port=22,
                              username=probe_username, password=probe_password)
                time.sleep(30)
                probe.close()
                print("%s: Monitoring probe is reachable. No actions needed." %
                      str(datetime.datetime.now()))
                failure_count = 0
            except socket.error:
                print("%s: Monitor probe is unreachable. Please verify IP connectivity to the probe"
                      " and rerun the script." str(datetime.datetime.now()))
                sys.exit(1)
            except paramiko.ssh_exception.AuthenticationException:
                failure_count += 1
                print("%s: Authentication failed %s time(s)." % (str(datetime.datetime.now())),
                      str(failure_count))
                time.sleep(60)
            except paramiko.ssh_exception.NoValidConnectionsError:
                print("%s: Monitor probe is unreachable. Please verify IP connectivity to the probe"
                      " and then rerun the script." % str(datetime.datetime.now()))
                sys.exit(1)
            except paramiko.ssh_exception.SSHException:
                print("%s: Invalid credentials for the probe. Please set proper username/password "
                      "and rerun the script." % str(datetime.datetime.now()))
                sys.exit(1)
        print("%s: Authentication to probe unavailable. We will proceed "
              "with the ise restart to recover." % str(datetime.datetime.now()))
        restart_ise(ise_address, ise_username, ise_password, 22)
        send_email(sender_email, Email_password, recipient_email,
                   smtp_server, smtp_server_port)
        time.sleep(600)
