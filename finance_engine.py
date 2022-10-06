#  Finance Engine V000

import numpy as np
import json

def dump_j_to_json(j, file_name, jobj_name='no_name_given'):
    with open(file_name, 'w') as f_temp:
        json.dump(j, f_temp, indent=2)
    if jobj_name != 'no_name_given':
        print('JSON OPERATION: ' + '"' + jobj_name + '"' + ' dumped to: ' + file_name)


def load_json_to_j(file_name, jobj_name='no_name_given'):
    with open(file_name) as f_temp:
        j = json.load(f_temp)
    if jobj_name != 'no_name_given':
        print('JSON OPERATION: ' + file_name + ' loaded into ' + '"' + jobj_name + '"')
    return j

j_test = load_json_to_j("transactions.json")
n_txns = len(j_test)
print(j_test)

txn_test = {'DATE': '2022-09-01 00:00:00', 'TITLE': 'DYMON -WLK, Ottawa On', 'AMOUNT': 298.32, 'UNIT': 'CAD', 'ACCOUNT': 'SCO2029', 'NOTE': ''}
j_test[str(n_txns)] = txn_test
print(j_test)

def append_txn_to_j_txnreg(j_txnreg, j_txn):
    n_txnreg_txns = len(j_txnreg)  # number of tnxs in txnreg
    j_txnreg[str(n_txnreg_txns)] = j_txn
    return j_txnreg

def gen_j_txn(timestamp, title, amount, unit, account, note):
    j_txn = {'DATE': timestamp, 'TITLE': title, 'AMOUNT': amount, 'UNIT': unit, 'ACCOUNT': account, 'NOTE': note}
    return j_txn

dump_j_to_json(j_test, "transactions_test1.json")