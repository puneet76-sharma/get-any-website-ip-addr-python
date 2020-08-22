import socket as s

host= input("enter the host(website): ")


print(f'IP of {host} is {s.gethostbyname(host)}')

input()