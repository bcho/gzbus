# coding: utf-8

'''
    gzbus.utils
    ~~~~~~~~~~~

    Utilites.
'''


def clean_text(text):
    '''Clean up text.'''
    text = text or ''
    return text.strip()
