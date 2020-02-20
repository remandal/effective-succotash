import paramiko
import time


def show_version(remote_conn):


print “show_vesrion”
time.sleep(2)
remote_conn.send(“\n”)
remote_conn.send(“\n”)
remote_conn.send(“show version\n”)
time.sleep(2)
#

def my_ssh(ip, o):


try:
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip, port=22, username=user, password=pwd,
            look_for_keys=False, allow_agent=False)
remote_conn = ssh.invoke_shell()  # Invoke the shell for interactive terminal
time.sleep(5)
#output = remote_conn.recv(65535)
#print output
remote_conn.send(“\n”)
remote_conn.send(“\n”)
remote_conn.send(“\n”)
remote_conn.send(“\n”)
print type(ip)
print type(o)
print “printing o”+ o
print “printing ip”+ ip
disable_paging(remote_conn)
output = remote_conn.recv(65535)

if “1” in o:
print “1 in my ssh”
show_version(remote_conn)

remote_conn.send(“exit\n”)
time.sleep(5)
output = remote_conn.recv(65535)
print output
ssh.close()  # Closing the connection

except paramiko.AuthenticationException:
print(“User or password incorrect, Please try again!!!”)


https: // www.ictshore.com/sdn/python-ssh-tutorial/

https: // github.com/paramiko/paramiko/issues/360

https: // knowtoshare.wordpress.com/2016/12/28/python3-and-paramiko-for-ssh-router-and-switch/


https: // medium.com/@keagileageek/paramiko-how-to-ssh-and-file-transfers-with-python-75766179de73

https: // hackersandslackers.com/automate-ssh-scp-python-paramiko/

https: // pynet.twb-tech.com/blog/python/paramiko-ssh-part1.html

https://stackoverflow.com/questions/32284120/config-a-cisco-router-through-paramiko/34110037

https: // www.programcreek.com/python/example/4561/paramiko.SSHClient

https: // community.cisco.com/t5/other-network-architecture/python-to-issue-cli-commands-over-ssh/td-p/3084328





