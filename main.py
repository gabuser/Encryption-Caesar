from typing import Optional
from random import randint
from random import choice
from string import ascii_uppercase
import string

class Cypher():
    def __init__(self, shift:int, alphabet:str):
        self.shift =shift
        self.alphabet = alphabet
    
    def generatekey(self)->None:
        pass

    def encrypt(self,passinword)-> None:
        self.passiword = passinword
        self.position = 0
        self.stored = list()
        self.sotred_strings = list()

        for a in range(len(self.passiword)):
            self.passiword = (lambda passinword: ord(passinword[a]) -ord(passinword[a]))(passinword)
            self.position = (lambda position:(self.passiword+ 25)%26)(self.position)
            self.newpos = (lambda postition: chr(self.position+ ord(passinword[a])))(self.position)
            
            self.stored.append(self.newpos)
            self.sotred_strings.append(passinword[a])
        
    def decrypt(self)->None:
        self.aftercypher = 0
        self.originalposition = 0
        self.original = 0

        for b in range(len(self.stored)):
            self.aftercypher = (lambda normalize: (ord(self.stored[b]) - ord(self.sotred_strings[b])))(self.aftercypher)
            self.originalposition= (lambda convertpositionback: (self.aftercypher - self.shift) %26)(self.originalposition)
            self.original = (lambda strings: (self.originalposition + ord(self.sotred_strings[b])))(self.original)
            print(chr(self.original))
        
        print(self.stored)
running = Cypher(25,string.ascii_letters )
running.encrypt('ola mundo ola mundo ola mundo ola mundo ola mundo')
running.decrypt()