
import hashlib as hasher
import datetime as date

'''
__target__ = 区块链初探 
'''

#定义区块链是什么样子,比如每个链的索引位置,时间数据,以及哈希值
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()
        # 初始化参数
    def hash_block(self):
        sha = hasher.sha256()#使用sha256进行加密
        sha.update(
            bytes(
                str(self.index) + str(self.timestamp) + str(self.data) + str(
                    self.previous_hash), 'utf-8'))#更新数据,返回给我们一个16进制的加密结果
        return sha.hexdigest()
#创建一个起源块
def create_genesis_block():
    # 起源块后续的块链都会以一种方式创建
    return Block(0, date.datetime.now(), "Genesis Block", "0")
#起源块后续的块链都会以一种方式创建
def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "你好,我是块链 " + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)
def main():
    # 起源块后续的块链都会以一种方式创建
    blockchain = [create_genesis_block()]
    previous_block = blockchain[0]
    # 手动构造块链,索引为0的任意先前块链,起源块之后的追加块链
    num_of_blocks_to_add = 100
    # 添加到链上
    for i in range(0, num_of_blocks_to_add):
        block_to_add = next_block(previous_block)
        blockchain.append(block_to_add)
        previous_block = block_to_add
        print("Block #{} has been added to the"
              "blockchain!".format(block_to_add.index))
        print("Hash: {}\n".format(block_to_add.hash))
if __name__ == "__main__":
    main()