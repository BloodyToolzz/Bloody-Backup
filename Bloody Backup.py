import requests, random, time, sys, os, pystyle
from colorama import Fore
import os
import colorama
from re import findall
from json import loads, dumps
from base64 import b64decode
from subprocess import Popen, PIPE
from urllib.request import Request, urlopen
from threading import Thread
from time import sleep
from pystyle import *
import subprocess
import requests
import sys
import time
from sys import argv
# import brain

os.system('title [Bloody Backup] - Loading')
os.system('cls')
Write.Print('Info: It is recommended that you use a VPN to prevent ratelimits.\n', Colors.purple_to_blue, interval=0.008)
time.sleep(2)
os.system('cls')

os.system('title [Bloody Backup] - by Bloody')


banner = ("""
                  
██████╗ ██╗      ██████╗  ██████╗ ██████╗ ██╗   ██╗    ██████╗  █████╗  ██████╗██╗  ██╗██╗   ██╗██████╗ 
██╔══██╗██║     ██╔═══██╗██╔═══██╗██╔══██╗╚██╗ ██╔╝    ██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██║   ██║██╔══██╗
██████╔╝██║     ██║   ██║██║   ██║██║  ██║ ╚████╔╝     ██████╔╝███████║██║     █████╔╝ ██║   ██║██████╔╝
██╔══██╗██║     ██║   ██║██║   ██║██║  ██║  ╚██╔╝      ██╔══██╗██╔══██║██║     ██╔═██╗ ██║   ██║██╔═══╝ 
██████╔╝███████╗╚██████╔╝╚██████╔╝██████╔╝   ██║       ██████╔╝██║  ██║╚██████╗██║  ██╗╚██████╔╝██║     
╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝    ╚═╝       ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     
                                                                                                          
                  Made By Bloody,
                  [Youtube] https://youtube.com/c/ScriptHubRoblox
                  [Discord] https://discord.gg/sJTjPzaPT5

                                                            """)
Anime.Fade(Center.Center(banner), Colors.purple_to_blue, Colorate.Vertical, interval=0.025, enter=True)
print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter(banner)))


token = Write.Input("Please Enter Your Account Token:\n", Colors.purple_to_blue, interval=0.008)
time.sleep(2)
os.system('cls')

def save_friends():
    saved_friends = 0

    friends = requests.get('https://discord.com/api/v6/users/@me/relationships', headers = headers)
    for friend in friends.json():
        if friend['type'] == 1:
            username = 'Username: %s#%s | User ID: %s\n' % (friend['user']['username'], friend['user']['discriminator'], friend['id'])
            Write.Print('[?] ' + username, Colors.purple_to_blue, interval=0.008)
            with open('Bloody Friends.txt', 'a', encoding = 'UTF-8') as f:
                f.write(username)
            saved_friends += 1

    with open('Bloody Friends.txt', 'r', encoding = 'UTF-8') as f:
        fixed = f.read()[:-1]
    with open('Bloody Friends.txt', 'w', encoding = 'UTF-8') as f:
        f.write(fixed)

    Write.Print('[?] Successfully saved all %s bloody friends.\n' % (saved_friends), Colors.purple_to_blue, interval=0.008)
    time.sleep(3)
    os.system('cls')

def save_servers():
    saved_servers = 0
    attempts = 0
    server_info_all = ''

    servers = requests.get('https://discordapp.com/api/v6/users/@me/guilds', headers = headers)
    for server in servers.json():
        server_info_all += '%s|||%s\n' % (server['id'], server['name'])

    payload = {
        'max_age': '0',
        'max_uses': '0',
        'temporary': False
    }

    for server_info in server_info_all.splitlines():
        server_id = server_info.split('|||')[0]
        server_name = server_info.split('|||')[1]

        channels = requests.get('https://discord.com/api/v6/guilds/%s/channels' % (server_id), headers = headers)
        for channel in channels.json():
            if channel['type'] == 0:
                channel_id = channel['id']
                invite = requests.post('https://discord.com/api/v6/channels/%s/invites' % (channel_id), json = payload, headers = headers)
                
                if invite.status_code == 403:
                    attempts += 1
                    Write.Print('Discord Server: %s | Channel ID: %s | Retrying . . .\n' % (server_name, channel_id), Colors.purple_to_blue, interval=0.008)
                    if attempts == 5:
                        Write.Print('%s has a Vanity URL.\n' % (server_name), Colors.purple_to_blue, interval=0.008)
                        with open('Bloody Servers.txt', 'a', encoding = 'UTF-8') as f:
                            f.write('Discord Server: %s | Vanity URL\n' % (server_name))
                        saved_servers += 1
                        attempts = 0
                        break
                    else:
                        pass
                    time.sleep(4)
                
                elif invite.status_code == 429:
                    Write.Print('[!] Rate limited.\n', Colors.purple_to_blue, interval=0.008)
                    time.sleep(15)
                
                else:
                    invite_url = 'https://discord.gg/%s' % (str(invite.json()['code']))
                    Write.Print('[?] Discord Server: %s | Invite Link: %s\n' % (server_name, invite_url), Colors.purple_to_blue, interval=0.008)
                    with open('Bloody Servers.txt', 'a', encoding = 'UTF-8') as f:
                        f.write('Discord Server: %s | Channel ID: %s | Invite Link: %s\n' % (server_name, channel_id, invite_url))
                    saved_servers += 1
                    time.sleep(4)
                    break

    Write.Print('\n[?] Successfully saved all %s bloody servers.\n' % (saved_servers), Colors.purple_to_blue, interval=0.008)
    time.sleep(3)
    os.system('cls')
    

def add_friends():
    added_friends = 0

    if os.path.exists('Bloody Friends.txt'):
        with open('Bloody Friends.txt', 'r', encoding = 'UTF-8') as f:
            for line in f.readlines():
                while True:
                    try:
                        line = line.replace('\n', '')
                        user_id = line.split('User ID: ')[1]
                        user_name = line.split(' |')[0]
                    except IndexError:
                        Write.Print('[!] Invalid syntax at line: %s\n' % (line), Colors.purple_to_blue, interval=0.008)
                        break
                    
                    add = requests.put('https://discord.com/api/v6/users/@me/relationships/%s' % (user_id), json = {}, headers = headers)
                    if add.status_code == 429:
                        Write.Print('[!] Rate limited.\n', Colors.purple_to_blue, interval=0.008)
                        time.sleep(50)
                    elif add.status_code == 204:
                        Write.Print('[?] Sent Friend Request to: %s\n' % (user_name), Colors.purple_to_blue, interval=0.008)
                        added_friends += 1
                        break
                    elif add.status_code == 400:
                        Write.Print('[!] User has disabled Friend Requests: %s\n' % (user_name), Colors.purple_to_blue, interval=0.008)
                        break
                    elif add.status_code == 403:
                        Write.Print('[!] Verify your Discord account.\n', Colors.purple_to_blue, interval=0.008)
                        break
                    else:
                        Write.Print('[!] Error: %s\n' % (add.text), Colors.purple_to_blue, interval=0.008)
                        break

                delay = random.randint(30, 35)
                time.sleep(delay)
        
        Write.Print('\n[?] Successfully added %s bloody friends.\n' % (added_friends), Colors.purple_to_blue, interval=0.008)
        time.sleep(3)
        os.system('cls')
        
        
    
    else:
        Write.Print('[!] You have not saved any friends.\n', Colors.purple_to_blue, interval=0.008)
        os.system('pause >nul')

def join_servers():
    joined_servers = 0

    if os.path.exists('Bloody Servers.txt'):
        with open('Bloody Servers.txt', 'r', encoding = 'UTF-8') as f:
            for line in f.readlines():
                while True:
                    try:
                        line = line.replace('\n', '')
                        if 'Vanity URL' in line:
                            Write.Print('[?] Server has a Vanity URL.\n', Colors.purple_to_blue, interval=0.008)
                            break
                        else:
                            invite_code = line.split('https://discord.gg/')[1]
                            server_name = line.split('Discord Server: ')[1].split(' | Channel ID')[0]
                    except IndexError:
                        Write.Print('[!] Invalid syntax at line: %s\n' % (line), Colors.purple_to_blue, interval=0.008)
                        break
                    
                    join = requests.post('https://discord.com/api/v6/invites/%s' % (invite_code), headers = headers)
                    if join.status_code == 429:
                        Write.Print('[!] Rate limited.\n', Colors.purple_to_blue, interval=0.008)
                        time.sleep(50)
                    elif join.status_code == 200:
                        Write.Print('[?] Successfully Joined: %s\n' % (server_name), Colors.purple_to_blue, interval=0.008)
                        joined_servers += 1
                        break
                    elif join.status_code == 403:
                        Write.Print('[!] Verify your Discord account.\n', Colors.purple_to_blue, interval=0.008)
                        break
                    else:
                        Write.Print('[!] Error: %s\n' % (join.text), Colors.purple_to_blue, interval=0.008)
                        break

                delay = random.randint(40, 45)
                time.sleep(delay)

        Write.Print('\n[?] Successfully joined %s bloody servers.\n' % (joined_servers), Colors.purple_to_blue, interval=0.008)
        time.sleep(3)
        os.system('cls')

    else:
        Write.Print('[!] You have not saved any servers.\n', Colors.purple_to_blue, interval=0.008)
        os.system('pause >nul')

while True:
    os.system('title [Bloody Backup by Bloody] - Main Menu')
    headers = { 'authorization': token }
    connect = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers = headers)

    if connect.status_code == 200:
        option = str(Write.Input('[1] Save Friends\n[2] Save Servers\n\n[3] Add Friends\n[4] Join Servers\n\n[>] Select an option:\n', Colors.purple_to_blue, interval=0.008))
        os.system('cls')
        print()
        if option == '1' or option == 'Save Friends':
            os.system('title [Bloody Backup] - Save Friends')
            save_friends()
        elif option == '2' or option == 'Save Servers':
            os.system('title [Bloody Backup] - Save Servers')
            save_servers()
        elif option == '3' or option == 'Add Friends':
            os.system('title [Bloody Backup] - Add Friends')
            add_friends()
        elif option == '4' or option == 'Join Servers':
            os.system('title [Bloody Backup] - Join Servers')
            join_servers()
        else:
            Write.Print('[!] Invalid option.\n\n', Colors.purple_to_blue, interval=0.008)
            time.sleep(2)
            os.system('cls')

    else:
        Write.Print('[!] Invalid Discord token. Please restart the program.\n', Colors.purple_to_blue, interval=0.008)
        Write.Print('Press any key to continue . . .', Colors.purple_to_blue, interval=0.008)
        os.system('pause >nul')
        break
