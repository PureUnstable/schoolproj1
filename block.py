class block(object):
    
    def __init__(self):
        self.next_block_hash = '0000000000000000000000000000000000000000000000000000000000000000'
        self.block_height: 0
        self.block_hash = '0000000000000000000000000000000000000000000000000000000000000000'
        self.timestamp = ''
        self.num_bits: 0x0
        self.prev_block_hash: '0000000000000000000000000000000000000000000000000000000000000000'
        self.transactions = list()
        self.block_header = ''

class transaction(object):
    
    def __init__(self):
        self.trans_in = True
        self.value = 0.0
        self.recv_addr = '0000000000000000000000000000000000'
        self.send_addr = '0000000000000000000000000000000000'
