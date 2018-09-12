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
bamlist = os.listdir('./')
for i in bamlist:
    if i.endswith('.bam'):
        # preffix = i.split('.')[0]
        # cmd1= 'samtools view -b -S ../mapped/%s > %s.bam'%(i,i.split('.')[0])
        # print(cmd1)
        # os.system(cmd1)
        cmd2 = 'samtools sort --threads 32 -m 10G  %s -o  %s.sort.bam ' % (i, i.split('.')[0])
        print(cmd2)
        os.system(cmd2)
