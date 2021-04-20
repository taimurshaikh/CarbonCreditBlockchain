""" Blockchain modules adapted from https://www.youtube.com/watch?v=b81Ib_oYbFk https://github.com/howCodeORG/Simple-Python-Blockchain """
import datetime
import hashlib

class Block:

    def __init__(self, transactionLst):
        self.data = transactionLst
        self.blockNo = 0
        self.next = None
        self.hashedVal = None
        self.nonce = 0
        self.previous_hash = 0x0

    def hash(self):
        h = hashlib.sha256()
        h.update(
        str(self.nonce).encode('utf-8') +
        str(self.previous_hash).encode('utf-8') +
        str(self.timestamp).encode('utf-8') +
        str(self.blockNo).encode('utf-8')
        )
        return h.hexdigest()

    def __str__(self):
        return "Block Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.blockNo) + "\nBlock Data: " + str(self.data) + "\nHashes: " + str(self.nonce) + "\n--------------"

class BlockChain:

    def __init__(self):
        self.diff = 10
        self.maxNonce = 2**32
        self.target = 2 ** (256-self.diff)
        self.head = Block("Genesis")
        self.block = self.head

    def add(self, block):

        block.previous_hash = self.block.hash()
        block.blockNo = self.block.blockNo + 1

        self.block.next = block
        self.block = self.block.next

    def mine(self, block):
        for n in range(self.maxNonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1

class Transaction:

    def __init__(self, sender, buyer, amount):
        self.sender = sender
        self.buyer = buyer
        self.amount = amount
        self.tokensBought = amount * TOKEN_PRICE
        self.timestamp = datetime.datetime.now()

    def __str__(self):
        return f"{self.buyer.name} bought {self.tokensBought} tokens from {self.sender.name} for {self.amount} at {self.timestamp}"
