# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 12:21:08 2018

@author: abrahao de weber
"""

def encrypt(a,e,n):
    m = []
    for i in a:
        m.append((ord(i)**e) % n)
    return m

def decrypt(d,n,m):
    t = []
    for i in m:
        t.append(chr(i**d % n))
    return t

