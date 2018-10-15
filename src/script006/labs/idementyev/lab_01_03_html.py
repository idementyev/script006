#!/usr/bin/env python3

"""
Function that builds html tags. Apply html escaping for html special chars.
Receive 2 parameters – tag type and tag content. Return generated html as text.
"""

__version__ = '0.0.1'
__author__ = 'Ilya R. Dementyev'
__date__ = '2018-10-15'


def html_decorator(tag: str, text: str) -> str:
    """
    Returns decorated HTML string with special chars escaping
    :param tag: the tag to wrap into
    :param text: text to wrap around
    :return: decorated string
    """

    text = text\
        .replace("&", "&amp;")\
        .replace("<", "&lt;")\
        .replace(">", "&gt;")\
        .replace('"', '&quot;')
    if type(tag) is not str or tag[0].isdigit() or " " in tag:
        print("Invalid XML tag, skipping")
        return text
    return "<{tstart}>{text}</{tend}>".format(tstart=tag, text=text, tend=tag)
