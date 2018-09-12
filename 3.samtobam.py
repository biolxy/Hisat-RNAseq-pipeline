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
bamlist = os.listdir('../3map/')
for i in bamlist:
    if i.endswith('.sam'):
        # preffix = i.split('.')[0]
        cmd = 'samtools view --threads 32 -b -S ../3map/%s -o %s.bam' % (i, i.split('.')[0])
        print(cmd)
        os.system(cmd)
