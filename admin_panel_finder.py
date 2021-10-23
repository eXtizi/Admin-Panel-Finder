#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from urllib.request import Request
from urllib.request import urlopen
from urllib.request import URLError, HTTPError
b =open('outputworking0.txt','w')

def Space(j):
	i = 0
	while i<=j:
		print (" ")
		i+=1


def findAdmin():
 f = open("admin_login.txt","r");
 link = input("Enter Site Name \n(ex : example.com or www.example.com ): ")
 print ("\n\nAvilable links : \n")
 while True:
        sub_link = f.readline()
        if not sub_link:
                break
        req_link = "http://"+link+"/"+sub_link
        req = Request(req_link)
        try:
         response = urlopen(req)
                
        except HTTPError as e:
         print(req_link+' failed')
                
        except URLError as e:
         print(req_link+' failed')
                
        else:
         print("OK => ",req_link)
         b.write(line)
         b.write('\n')
 b.close()

def Credit():
	Space(9); print ("#####################################")
	Space(9); print ("#   +++ Admin Panel Finder v1 +++   #")
	Space(9); print ("#     Script by Illûmïnåté Ðëmøñ    #")
	Space(9); print ("#    Bangladesh Black Hat Hackers   #")
	Space(9); print ("# Fixed,Modified,Improved By Extizi #")
	Space(9); print ("#####################################")

Credit()
findAdmin()
