# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 22:44:02 2018

@author: Administrator
"""

from __future__ import division, print_function, absolute_import
import wfdb
"""
#test
#读取在线波形数据(以100为例)
pbsig, pbfields = wfdb.rdsamp('101', pb_dir = 'mitdb')
#读取本地波形数据(以101为例)
sig, fields = wfdb.rdsamp('101/101')

annotation = wfdb.rdann('101/101', 'atr')
#annotation.aux_note[0] = '(N'
a = annotation.ann_len
a1 = annotation.sample#表示注释位置
a2 = annotation.symbol#表示标注的符号
a3 = annotation.subtype#
a4 = annotation.chan
a5 = annotation.num
"""
#在线全部读取
patient_name_list = [100,104,108,113,117,122,201,207,212,217,222,231,
                     101,105,109,114,118,123,202,208,213,219,223,232,
                     102,106,111,115,119,124,203,209,214,220,228,233,
                     103,107,112,116,121,200,205,210,215,221,230,234]
patient_information_list = []
for i in patient_name_list:
    print(i)
    pbsig, pbfields = wfdb.rdsamp(str(i), pb_dir = 'mitdb')
    if "MLII" in pbfields["sig_name"]:
        print("have MLII")
        temp_index = pbfields["sig_name"].index("MLII")
        temp_sig = pbsig[:,temp_index]
        pbannotation = wfdb.rdann(str(i), 'atr', pb_dir='mitdb', return_label_elements=['label_store', 'symbol'])
        temp_sample = pbannotation.sample
        temp_symbol = pbannotation.symbol
        temp_ann_len = pbannotation.ann_len
        patient_information_list.append([i, temp_sig, temp_sample, temp_symbol, temp_ann_len])
    else:
        print("not have MLII")
del i, pbsig, pbfields, temp_index, temp_sig, pbannotation, temp_sample, temp_symbol, temp_ann_len

#save_information
f = open('save_information.txt', "a+")
for i in patient_information_list:
    f.write(str(i[0]) + ";")
    for j in i[1]:
        f.write(str(j) + ",")
    f.write(";")
    for j in i[2]:
        f.write(str(j) + ",")
    f.write(";")
    for j in i[3]:
        f.write(str(j) + ",")
    f.write(";")
    f.write(str(i[4]) + ";" + "\n")
    print(i[0])
del i
f.close()


#因为切割方法因人而异，所以只做到了读取在线数据，按照格式进行保存