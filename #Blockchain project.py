# Blockchain project

# The blockchain uses an encryption system for the hashes, in this case, I'm going to use the same one as bitcoin

from hashlib import sha256

# This is a "theoretical" blockchain so I'm going to create some transactions between users

transactions1 = ["Alex sends 5 coins to Willy",
                 "Willy sends 7 coins to Mario",
                 "Mario sends 4 coins to Luigi"]

transactions2 = ["Clair sends 8 coins to Juan",
                 "Juan sends 9 coins to Emma",
                 "Emma sends 10 coins to Victor"]

# Now it's time to create the blocks of the blockchain, first step, a class

class Block:
    def __init__(self, prev_block, data):
        self.prev_block = prev_block  # At the end we need to relate the previous hash to the new one to build a chain
        self.data = data  # this is the info of the actual transactions
        self.nonce = 0  # This is for the mining of the block

    def hash(self):
        info = "#".join(self.data) + self.prev_block + str(self.nonce)  # Combine the data into a single string
        return sha256(info.encode()).hexdigest()  # Calculate the SHA-256 hash and return the hexadecimal value

# Having blocks, we need the chain so it's time to create a new class

class Chain:
    difficulty = 7

    def __init__(self):
        self.chain = []  # this is where all the blocks of the list will be saved

    def add(self, block):
        self.chain.append(block)

    def mine(self, block):
        while True:
            hash_value = block.hash()
            if hash_value[:self.difficulty] == "0" * self.difficulty: #the variable defficulty determines de amount of "0" that's needed in the beginning of the hash, more 0 more tries
                self.add(block)
                break
            else:
                block.nonce += 1 #Every attempt adds another number to try to calculate the needed hash

block_chain = Chain()

# Now, with a class and the method to build the blocks and the chain, it's time to create the first one

b1 = Block("0" * 64, transactions1)  # I don't have a previous hash so I added one with 64 zeros simulating a hexadecimal code.

block_chain.mine(b1)
print("First block hash:", block_chain.chain[0].hash())

b2 = Block(b1.hash(), transactions2)  # Use the hash of the first block as the previous hash for the second block
block_chain.mine(b2)
print("Second block hash:", block_chain.chain[1].hash())
print("Atempts: ", block_chain.chain[0].nonce)
 