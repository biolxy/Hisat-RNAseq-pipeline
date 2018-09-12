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

import os
data = os.listdir("../0rawdata/")
paired = []
for i in data:
    if i.endswith('.fastq'):
        paired.append(i)
if len(paired) % 2 != 0:
    print('num Not Paired!!!')
    exit()
paired.sort()
for i in range(0, len(paired), 2):
        file1 = paired[i]
        file2 = paired[i+1]
        print(file1, file2)
        print("TrimmingReads")
        os.system("perl /home/lixiangyong/soft/NGSQCToolkit/Trimming/TrimmingReads.pl -i ../0rawdata/{fq1} -irev ../0rawdata/{fq2} -l 13 -n 50 -o {outputdir}".format(fq1=file1, fq2=file2, outputdir="../1rawdata/"))
