#!/usr/bin/env python
import requests
print("Bem vindo a moscow")
ip = input("Insira o IP: ")

url = "http://ip-api.com/json/" + ip

response = requests.get(url)
data = response.json()

print("País: " + data["country"])
print("Cidade: " + data["city"])
print("Região: " + data["regionName"])
print("Latitude: " + str(data["lat"]))
print("Longitude: " + str(data["lon"]))
print("Organização: " + data["org"])
print("Sistema Operacional: " + data["os"])
print("Comandos Android: " + data["androidCommands"])
