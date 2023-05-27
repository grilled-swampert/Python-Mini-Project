from os import walk
import pygame

def import_folder(path):
    for information in walk(path):
        print(information)
    
import_folder('C:/Users/user/Desktop/TejasPython/run')