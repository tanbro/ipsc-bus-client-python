# -*- coding: utf-8 -*-

"""
Some helper functions
"""

from __future__ import absolute_import

import logging

__all__ = ['b2s_recode', 's2b_recode', 'to_bytes', 'to_str', 'to_unicode', 'LoggerMixin']

if bytes != str:  # Python 3
    #: Define text string data type, same as that in Python 2.x.
    unicode = str  # pylint: disable=invalid-name


def b2s_recode(bs, source_encoding=None, target_encoding=None):  # pylint: disable=invalid-name
    """将 :class:`bytes` 字符串重编码为 :class:`str` 字符串

    :param bytes bs: 待转换字节字符串
    :param str source_encoding: bytes 的编码格式。
        默认 `utf-8`。
    :param str target_encoding: 转换结果字符串的编码格式。
        仅 Python2 环境下有效。
    :return: 转换结果字符串
    :rtype: str
    """
    if bs is None:
        return bs
    if bytes == str:  # Python 2
        return bs.decode(source_encoding).encode(target_encoding)
    # Python 3
    return bs.decode(source_encoding)


def s2b_recode(s, source_encoding=None, target_encoding=None):  # pylint: disable=invalid-name
    """将 :class:`str` 字符串重编码为 :class:`bytes` 字符串

    :param str s: 待转换字节字符串
    :param str source_encoding: bytes 的编码格式。
        仅 Python2 环境下有效。
    :param str target_encoding: 转换结果字符串的编码格式。
    :return: 转换结果字符串
    :rtype: bytes
    """
    if s is None:
        return s
    if bytes == str:  # Python 2
        return s.decode(source_encoding).encode(target_encoding)
    # Python 3
    return s.encode(target_encoding)


def to_bytes(s, encoding='utf-8'):  # pylint: disable=invalid-name
    """Convert to `bytes` string.

    :param s: String to convert.
    :param str encoding: Encoding codec.
    :return: `bytes` string, it's `bytes` or `str` in Python 2.x, `bytes` in Python 3.x.
    :rtype: bytes

    * In Python 2, convert `s` to `bytes` if it's `unicode`.
    * In Python 2, return original `s` if it's not `unicode`.
    * In Python 2, it equals to :func:`to_str`.
    * In Python 3, convert `s` to `bytes` if it's `unicode` or `str`.
    * In Python 3, return original `s` if it's neither `unicode` nor `str`.
    """
    if s is None:
        return s
    if isinstance(s, bytes):
        return s
    if isinstance(s, unicode):
        return s.encode(encoding)
    raise TypeError('Type of argument "s" is neither "str" nor "bytes".')


def to_str(s, encoding='utf-8'):  # pylint: disable=invalid-name
    """Convert to `str` string.

    :param s: String to convert.
    :param str encoding: Decoding codec.
    :return: `str` string, it's `bytes` in Python 2.x, `unicode` or `str` in Python 3.x.
    :rtype: str

    * In Python 2, convert `s` to `str` if it's `unicode`.
    * In Python 2, return original `s` if it's not `unicode`.
    * In Python 2, it equals to :func:`to_bytes`.
    * In Python 3, convert `s` to `str` if it's `bytes`.
    * In Python 3, return original `s` if it's not `bytes`.
    * In Python 3, it equals to :func:`to_unicode`.
    """
    if bytes == str:  # Python 2
        return to_bytes(s, encoding)
    # Python 3
    return to_unicode(s, encoding)


def to_unicode(s, encoding='utf-8'):  # pylint: disable=invalid-name
    """Convert to `unicode` string.

    :param s: String to convert.
    :param str encoding: Encoding codec.
    :return: `unicode` string, it's `unicode` in Python 2.x, `str` or `unicode` in Python 3.x.
    :rtype: unicode

    * In Python 2, convert `s` to `unicode` if it's `str` or `bytes`.
    * In Python 2, return original `s` if it's neither `str` or `bytes`.
    * In Python 3, convert `s` to `str` or `unicode` if it's `bytes`.
    * In Python 3, return original `s` if it's not `bytes`.
    * In Python 3, it equals to :func:`to_str`.
    """
    if s is None:
        return s
    if isinstance(s, bytes):
        return s.decode(encoding)
    if isinstance(s, unicode):
        return s
    raise TypeError('Type of argument "s" is neither "str" nor "bytes".')


class LoggerMixin:
    """Mixin Class provide a :attr:`logger` property
    """

    @classmethod
    def get_logger(cls):
        """`logger` instance.

        :rtype: logging.Logger

        logger name format is `ModuleName.ClassName`
        """
        try:
            name = '{0.__module__:s}.{0.__qualname__:s}'.format(cls)
        except AttributeError:
            name = '{0.__module__:s}.{0.__name__:s}'.format(cls)
        return logging.getLogger(name)

    @property
    def logger(self):
        """`logger` instance.

        :rtype: logging.Logger

        logger name format is `ModuleName.ClassName`
        """
        return self.get_logger()
