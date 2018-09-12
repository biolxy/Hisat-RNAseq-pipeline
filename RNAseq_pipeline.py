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
from util.base import color_term
# from util.base import StreamToLogger
# from util.base import execute_cmd
import os
# import re
import time
import sys
import argparse

__VERSION__ = 'v1.0.0'
# logging.basicConfig(level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',filename="out.log",filemode='a')
# for i in range(1, 10):
#     print(color_term("I love you {}".format(i)))

# # execute_cmd("for i in `ls *`;do echo $i;done")
# execute_cmd("mkdir {}".format('aa'))


def main():
    u"""主要的函数流程."""
    # 步骤0，脚本开始，判断指定文件夹中是否存在文件 R1.fastq 或 R1.fastq.gz, 若不存在则中止程序
    print(color_term("-------------------------------------------------------------------", 'green'))
    print(color_term("the input dir is:\t{}".format(input_dir), 'green'))
    print(color_term("the output dir is:\t{}".format(output_dir), 'green'))
    print(color_term("-------------------------------------------------------------------", 'green'))
    start_time = time.time()
    fastq_fq1_list = []
    samplenum = 1
    for i in os.listdir(input_dir):
        # print i
        if i.endswith('R1.fastq') or i.endswith('R1.fastq.gz'):
            fq1 = os.path.join(input_dir, i)
            fq2 = os.path.join(input_dir, i.replace("R1.fastq", "R2.fastq"))
            if os.access(fq2, os.F_OK):
                fastq_fq1_list.append(fq1)
                fastq_fq1_list.append(fq2)
                print("samplenum: {}\tR1: {}\tR2: {}".format(samplenum, fq1, fq2))
                samplenum += 1
            else:
                print(color_term("don't exist the R2.fastq file of {}".format(fq1), 'yellow'))
    # if fastq_fq1_list:
    #     for i, item in enumerate(fastq_fq1_list, 1):
    #         samplenum = i
    #         fq1 = item

    if not fastq_fq1_list:
        print(color_term("can't find file with the suffix .R1.fastq.gz or .R1.fastq !!!", 'red'))
        sys.exit()
    print(color_term("main function execute time: {}s".format(round(time.time() - start_time, 2))))

    # 步骤1，trim掉read 左端13碱基序列，去除低质量序列， 对数据做质控

    #

if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(
            prog="Standard".format(__VERSION__),
            description="This is a RNAseq_pipeline."
            )
        # formatter_class=argparse.RawTextHelpFormatter,
        # https://docs.python.org/3/library/argparse.html
        # https://docs.python.org/2/howto/argparse.html
        # https://codeday.me/bug/20171209/105070.html
        group = parser.add_mutually_exclusive_group()
        group.add_argument(
            '-i',
            '--inputdir',
            type=str,
            help="Input dir for fastq file. To identify the input file, the suffix must is .R1.fastq.gz and .R1.fastq.gz or .R1.fastq and .R1.fastq, and you should make sure you have read and write access to these files",
            metavar='')
        # 指定参数的形式，一般写两个，一个短参数，一个长参数
        group.add_argument(
            '-o',
            '--outputdir',
            type=str,
            help="Specify output directory",
            metavar='')
        args = parser.parse_args()
        input_dir = os.path.abspath(args.inputdir)
        output_dir = os.path.abspath(args.outputdir)
        main()
    except KeyboardInterrupt:
        pass
    except IOError as e:
        raise
