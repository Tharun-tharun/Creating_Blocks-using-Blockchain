# consists blocks
# blocks consist transactions
# blocks are contains hash functions
        # unique digital fingerprint - transaction + previous blocks hash

from Block import Block

blockchain = []

genesis_block = Block("Chancellor on the brink...", ["satoshi sent 1 BTC to Ivan",
                                                     "Maria sent 5 BTC to jenny",
                                                     "Satoshi sent 100 BTC to Hal"])

second_block = Block(genesis_block.block_hash, ["Satoshi sent 10 BTC to Adam"])
third_block = Block(second_block.block_hash, ["A to C sent 5 BTC", "Lee sent 10 BTC to Vanson"])


print("Block hash: Genesis Block")
print(genesis_block.block_hash)

print("Block hash: Second Block")
print(second_block.block_hash)

print("Block hash: Third Block")
print(third_block.block_hash)






































































