#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# author wwqgtxx <wwqgtxx@gmail.com>

import os
import socket
import logging
import traceback


def get_main():
    try:
        from .. import main
    except Exception as e:
        import main

    return main


def get_main_parse():
    return get_main().parse


def call_method_and_save_to_queue(queue, method, args, kwargs):
    queue.put(method(*args, **kwargs))


def get_caller_info():
    try:
        fn, lno, func, sinfo = traceback.extract_stack()[-3]
    except ValueError:  # pragma: no cover
        fn, lno, func = "(unknown file)", 0, "(unknown function)"
    try:
        fn = os.path.basename(fn)
    except:
        pass
    callmethod = "<%s:%d %s> " % (fn, lno, func)
    return callmethod


def is_in(a, b, strict=True):
    result = False
    if isinstance(a, list):
        for item in a:
            if item in b:
                result = True
            elif strict:
                result = False
    else:
        result = (a in b)
    return result


def is_open(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.05)
    try:
        s.connect((ip, int(port)))
        s.shutdown(2)
        logging.info(get_caller_info() + '%d is open' % port)
        return True
    except:
        logging.info(get_caller_info() + '%d is down' % port)
        return False


