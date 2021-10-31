# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 17:22:30 2020

@author: andrea_sergiacomi
"""

def panino(tipo_di_panino):
	print("--------------------")
	print(tipo_di_panino())
	print("--------------------\n")

def cheeseburger():
	my_cb = "cheddar\nlattuga\ncipolla\nbacon\nketchup\nhamburger di scottona"
	return my_cb

def sandwitch_tonno():
	my_st = "lattuga\nmayonese\ntonno"
	return my_st

print("Cheeseburger")
panino(cheeseburger)

print("Sandwitch al tonno")
panino(sandwitch_tonno)
