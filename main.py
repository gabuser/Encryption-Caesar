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

    def encrypt(self,passinword)-> None:
        self.passiword = passinword
        self.position = 0
        self.stored_key = list()
        encrypted= 0
        
        for a in range(len(self.shift)):

            self.position = (lambda position:(self.passiword[a]+ self.shift[a])%self.mod)(self.position)
            self.stored_key.append(self.position)

        encrypted= bytes(self.stored_key)
        encrypted= encrypted.hex()
        print(encrypted)

    def decrypt(self)->None:
        self.aftercypher  =list()
        self.originalposition = 0
        self.original = 0

        for b in range(len(self.shift)):
            self.originalposition= (lambda convertpositionback: (self.stored_key[b] - self.shift[b]) %self.mod)(self.originalposition)
            self.aftercypher.append(self.originalposition)

        print(bytes(self.aftercypher))

running = Cypher(list(),string.ascii_letters,list(),256)
running.generatekey()
running.encrypt(b'ola mundo ola mundo ola mundo ola mundo ola mundo')
running.decrypt()