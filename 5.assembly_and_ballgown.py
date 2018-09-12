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
# /media/ibm_disk/work/duzc/duzc/software/stringtie-1.3.1c.Linux_x86_64/stringtie -e -B -p 8 -G ../assemble_screen/sample.gtf.merged -o /P0-2/P0-2.gtf ./mapping_screen/P0-2.sort.bam
import os
bamlist = os.listdir('../4samtobam/')
for i in bamlist:
    if i.endswith('.sort.bam'):
        preffix = i.split('.')[0]
        cmd = 'stringtie -e -B -A ./FPKM_result/%s_gene.fpkm -p 32 -G /data1/plant_genome/Teatree/Teatree.gtf -o ./sample/%s/%s.gtf ../4samtobam/%s' % (preffix, preffix, preffix, i)
        print(cmd)
        os.system(cmd)
