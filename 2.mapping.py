#!/usr/bin/env python
# -*- coding: utf-8 -*-
u"""
File Name   : aa.py .

Author      : biolxy
E-mail      : biolxy@aliyun.com
Created Time: 2018-09-12 14:02:55
version     : 1.0
Function    : The author is too lazy to write nothing
"""
# hisat2 -p 8 --dta -x ../hisat2_index/NCBIM37 -1 ../clean_data/P0-2_1.paired.fq.gz -2 ../clean_data/P0-2_1.paired.fq.gz -S P0-2.sam

import os
data = os.listdir('../2cleandata/')
paired = []
for i in data:
    if i.endswith('.fastq_trimmed_filtered'):
        paired.append(i)

# check
# print(len(paired))
if len(paired) % 2 != 0:
    print('num Not Paired!!!')
    exit()

paired.sort()
for i in range(0, len(paired), 2):
    file1 = paired[i]
    file2 = paired[i+1]
    # print(file1, file2)
    if file1.split('_')[0] != file2.split('_')[0]:
        print('prefix Not paired!!!')
        exit()
    cmd = 'hisat2 -p 32  -x /data1/plant_genome/Teatree/Teatree_tran  -1 ../2cleandata/%s -2 ../2cleandata/%s -S %s.sam' % (file1, file2, file1.split('.')[0])
    print(cmd)
    os.system(cmd)
