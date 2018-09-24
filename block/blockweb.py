#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     blockweb
    Author:        wyb
    Date:          2018/9/23 0023
    Description:   
"""
import hashlib
import json
from textwrap import dedent
from time import time
from uuid import uuid4

from flask import Flask

class Blockchain(object):
    ...

# Instantiate our Node（实例化我们的节点）
app = Flask(__name__)

# Generate a globally unique address for this node（为这个节点生成一个全球唯一的地址）
node_identifier = str(uuid4()).replace('-', '')

# Instantiate the Blockchain（实例化 Blockchain类）
blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    return "We'll mine a new Block"

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    return "We'll add a new transaction"

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)