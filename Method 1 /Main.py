import PySimpleGUI as sg
import paramiko

command = "df"
host = "YOUR PI'S IP ADDRES HERE" 
username = "YOUR PI'S USERNAME HERE" 
password = "YOUR PASSWORD TO YOUR PI HERE"

client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, password=password)

_stdin, _stdout,_stderr = client.exec_command("rm -fR THE NAME OF YOUR REPOSITORY HERE")
print(_stdout.read().decode())

_stdin, _stdout,_stderr = client.exec_command("rm -fR /home/YOUR USERNAME HERE/.config/autostart/autovlc.desktop")
print(_stdout.read().decode())

_stdin, _stdout,_stderr = client.exec_command("git clone https://github.com/GITHUB NAME HERE/THE NAME OF YOUR REPOSITORY HERE.git")
print(_stdout.read().decode())

_stdin, _stdout,_stderr = client.exec_command("mv /home/YOUR USERNAME HERE/THE NAME OF YOUR REPOSITORY HERE/autovlc.desktop /home/YOUR USERNAME HERE/.config/autostart")
print(_stdout.read().decode())

_stdin, _stdout,_stderr = client.exec_command("sudo reboot")
print(_stdout.read().decode())


    

