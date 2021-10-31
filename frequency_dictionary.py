# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 19:37:00 2020

@author: andrea_sergiacomi
"""

# frequency dictionary
lyrics = "Happy birthday to you Happy birthday to you Happy birthday dear friend Happy birthday to you"
counts = {}

words = lyrics.split(" ")

for w in words:
	w=w.lower()
	if w not in counts:
		counts[w] = 1
	else:
		counts[w] += 1

print(counts)
