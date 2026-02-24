from typing import Optional
from random import randint
import secrets
from string import ascii_uppercase
import string

class Cypher():
    def __init__(self, shift:int, alphabet:str, key:Optional[int], 
                 mod:int):
        self.shift =shift
        self.alphabet = alphabet
        self.key = key
        self.mod = mod
    
    def generatekey(self)->None:
        self.key = (lambda x: secrets.token_hex(32))(self.key)
        print(self.key)

    def encrypt(self,passinword)-> None:
        self.passiword = passinword
        self.position = 0
        self.stored = list()
        self.sotred_strings = list()

        for a in range(len(self.passiword)):
            
            self.passiword = (lambda passinword: ord(passinword[a]) -ord(passinword[a]))(passinword)
            self.position = (lambda position:(self.passiword+ self.shift)%self.mod)(self.position)
            self.newpos = (lambda postition: chr(self.position+ ord(passinword[a])))(self.position)
            
            self.stored.append(self.newpos)
            self.sotred_strings.append(passinword[a])
        
    def decrypt(self)->None:
        self.aftercypher = 0
        self.originalposition = 0
        self.original = 0

        for b in range(len(self.stored)):
            self.aftercypher = (lambda normalize: (ord(self.stored[b]) - ord(self.sotred_strings[b])))(self.aftercypher)
            self.originalposition= (lambda convertpositionback: (self.aftercypher - self.shift) %self.mod)(self.originalposition)
            self.original = (lambda strings: (self.originalposition + ord(self.sotred_strings[b])))(self.original)
            print(chr(self.original))
        
        print(self.stored)
running = Cypher(3,string.ascii_letters,0,26)
running.generatekey()
#running.encrypt(b'ola mundo ola mundo ola mundo ola mundo ola mundo')
#running.decrypt()