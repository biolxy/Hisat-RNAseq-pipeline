#!/usr/bin/env python
# -*- coding: utf-8 -*-
u"""
File Name   : base.py .

Author      : biolxy
E-mail      : biolxy@aliyun.com
Created Time: 2018-07-24 13:34:17
version     : 1.0
Function    : 用来提供一些基础功能，例如linux客户端彩色输出，记录日志，安全shell命令等
"""
import shlex
import logging
import subprocess


def color_term(string, color='blue', bold=True):
    u"""Linux客户端彩色输出，适配py2，py3."""
    colors = {
        'grey': '\033[0;30m',
        'red': '\033[0;31m',
        'green': '\033[0;32m',
        'yellow': '\033[0;33m',
        'blue': '\033[0;34m',
        'megenta': '\033[0;35m',
        'cyan': '\033[0;36m',
        'white': '\033[0;37m',
        'bold': '\033[1m',
        'end': '\033[0m'
    }
    color_format = colors[color].replace('[0', '[1') if bold else colors[color]
    return color_format + str(string) + colors['end']
    # print(color_term("{}".format(var), 'red'))


class StreamToLogger(object):
    u"""
    Fake file-like stream object that redirects writes to a logger instance.

    记录log日志，适配py3
    Refer: [Redirect stdout and stderr to a logger in Python]
           (https://www.electricmonk.nl/log/2011/08/14/redirect-stdout-and-stderr-to-a-logger-in-python/)
           [How to redirect stdout and stderr to logger in Python]
           (https://stackoverflow.com/questions/19425736/how-to-redirect-stdout-and-stderr-to-logger-in-python)
    """

    def __init__(self, logger, log_level=logging.INFO):
        self.logger = logger
        self.log_level = log_level
        self.linebuf = ''

    def write(self, buf):
        for line in buf.rstrip().splitlines():
            self.logger.log(self.log_level, line.rstrip())
    # logging.basicConfig(level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',filename="out.log",filemode='a')
    # SetupLogger('log', os.path.join(dir_output, 'handleAutobox.log'), log_mode=args.log_mode,
    #             format_sh='%(message)s', format_fh='[%(levelname)s] %(message)s')
    # logger = logging.getLogger('log')


def execute_cmd(cmd):
    u"""Change sys.system(),提供安全的shell输入端口，为以后web键入命令提供基础,适配py2, py3.

    execute_cmd 中可以直接嵌套 linux命令，同样可以嵌套类似 python script.py inputfile 等命令
    通常用法为 execute_cmd("mkdir {}".format())
    该函数调用 color_term 函数
    """
    # print("Command will be execute in a subshell:\n\t{}".format(cmd))
    try:
        p = subprocess.Popen(
            shlex.split(cmd),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
            )
        for line in iter(p.stdout.readline, b''):
            print(line.rstrip().decode())
        error = p.stderr.read().decode()
        print error
    except Exception as e:
        print("\n{}\n".format(cmd))
        raise e
