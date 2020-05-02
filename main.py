from BlockChain import BlockChain

if __name__ == "__main__":
    b1 = BlockChain("BlockChain")
    b2 = BlockChain("Bitcoin")
    print(b1.get_block())
    print(b2.get_block())
    print(BlockChain.get_all_blocks())
