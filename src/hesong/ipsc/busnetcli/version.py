# -*- coding: utf-8 -*-

"""
version
"""

from __future__ import absolute_import

from pkg_resources import get_distribution, DistributionNotFound

__all__ = ['__version__']

try:
    __version__ = get_distribution('hesong-ipsc-busnetcli').version
except DistributionNotFound:
    from ._scm_version import version as __version__
