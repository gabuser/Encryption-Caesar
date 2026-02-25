from typing import Optional
from random import randint
import secrets
from string import ascii_uppercase
import string

class Cypher():
    def __init__(self, shift:list, alphabet:str, key:Optional[list[str]], 
                 mod:int):
        self.shift =shift
        self.alphabet = alphabet
        self.key = key
        self.mod = mod
    
    def generatekey(self)->None:
        self.key = (lambda x: secrets.token_bytes(32))(self.key)

        for bytes_number in range(len(self.key)):
            self.shift.append(self.key[bytes_number])
        print(self.shift)

    def encrypt(self,passinword)-> None:
        self.passiword = passinword
        self.position = 0
        self.stored = list()
        #self.sotred_strings = list()

        for a in range(len(self.shift)):

            self.position = (lambda position:(self.passiword[a]+ self.shift[a])%self.mod)(self.position)
            self.stored.append(self.position)
            
        print(self.key.hex())

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
running = Cypher(list(),string.ascii_letters,list(),256)
running.generatekey()
running.encrypt(b'ola mundo ola mundo ola mundo ola mundo ola mundo')
#running.decrypt()