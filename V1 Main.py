import PySimpleGUI as sg
import paramiko

command = "df"
host = "192.168.153.235" 
username = "bennettb" 
password = "12345678"

client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, password=password)

_stdin, _stdout,_stderr = client.exec_command("rm -fR Raiderweekly")
print(_stdout.read().decode())

_stdin, _stdout,_stderr = client.exec_command("rm -fR /home/bennettb/.config/autostart/autovlc.desktop")
print(_stdout.read().decode())

_stdin, _stdout,_stderr = client.exec_command("git clone https://github.com/Bebe1s/Raiderweekly.git")
print(_stdout.read().decode())

_stdin, _stdout,_stderr = client.exec_command("mv /home/bennettb/Raiderweekly/autovlc.desktop /home/bennettb/.config/autostart")
print(_stdout.read().decode())

_stdin, _stdout,_stderr = client.exec_command("sudo reboot")
print(_stdout.read().decode())


    

