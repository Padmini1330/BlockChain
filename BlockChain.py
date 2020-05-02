import hashlib


class BlockChain:

    block_chain = None

    def __init__(self, data):
        self.block = None
        self.block_hash = None

        # CHECKING IF THE CHAIN IS EMPTY OR NOT
        if BlockChain.block_chain is None:

            # IF THIS IS THE FIRST BLOCK THEN SET THE "previous_hash" TO "STRING OF ZEROS"
            previous_hash = "00000000000000000000000000000000"

            # GET THE "Block" OBJECT
            self.block = self.Block(data, previous_hash)
            # GET THE HASH OF THE "Block" OBJECT
            self.block_hash = self.block.get_block_hash()

            # CREATE THE CHAIN AND APPEND THE OBJECT
            BlockChain.block_chain = []
            BlockChain.block_chain.append(self)
        else:

            # IF THIS IS NOT THE FIRST BLOCK THEN GET THE PREVIOUS-HASH AND SET IT TO "previous_hash"
            previous_hash = BlockChain.get_hash_of_last_block()

            # GET THE "Block" OBJECT
            self.block = self.Block(data, previous_hash)
            # GET THE HASH OF THE "Block" OBJECT
            self.block_hash = self.block.get_block_hash()

            # APPEND THE OBJECT TO THE CHAIN
            BlockChain.block_chain.append(self)

    # THIS METHOD IS USED TO GET HASH OF THE LAST BLOCK OBJECT
    @staticmethod
    def get_hash_of_last_block():
        last_block = BlockChain.block_chain[-1]
        return last_block.block_hash

    # THIS METHOD IS USED TO GET DETAILS OF ALL THE BLOCKS IN THE CHAIN
    @staticmethod
    def get_all_blocks():
        blocks = []
        for blk in BlockChain.block_chain:
            block = blk.get_block()
            blocks.append(block)

        return blocks

    # THIS METHOD IS USED TO GET DETAILS OF A BLOCK
    def get_block(self):
        block = {
            "data": self.block.data,
            "previous hash": self.block.previous_hash,
            "nonce": self.block.nonce,
            "hash": self.block_hash
        }
        return block

    # THIS CLASS "Block" COMPOSES THE DATA PART OF A BLOCK IN THE CHAIN
    class Block:

        def __init__(self, data, previous_hash):
            self.data = data
            self.previous_hash = previous_hash
            self.nonce = 0

        # THIS METHOD IS USED TO GET THE HASH OF THE "Block" OBJECT
        def get_block_hash(self):

            # GET BLOCK DATA AND CREATE A HASH OF THAT BLOCK-DATA (block_data)
            immutable_data = self.data + self.previous_hash
            block_data = immutable_data + str(self.nonce)
            block_hash = hashlib.md5(block_data.encode()).hexdigest()

            # CHECK FOR ONE ZERO AT THE BEGINNING OF THE HASH
            # IF ZERO IS NOT PRESENT THEN INCREMENT THE "nounce" AND RECOMPUTE THE HASH
            # UNTIL A ZERO IS PRESENT AT THE BEGINNING OF THE HASH
            while block_hash[0] != '0':
                self.nonce = self.nonce + 1
                block_data = immutable_data + str(self.nonce)
                block_hash = hashlib.md5(block_data.encode()).hexdigest()

            # RETURN THE HASH
            return block_hash
