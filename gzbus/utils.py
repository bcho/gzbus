# coding: utf-8

'''
    gzbus.utils
    ~~~~~~~~~~~

    Utilites.
'''

import sys


if sys.version_info < (3, 0):
    def u(s):
        if isinstance(s, unicode):
            s = s.encode('u8')
        return s
else:
    def u(s):
        return s


def clean_text(text):
    '''Clean up text.'''
    text = text or ''
    return u(text).strip()
