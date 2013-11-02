""" spock.ambients.util
"""
from goulash.decorators import arg_types

from spock.ambients.abstract import AbstractAmbient

ambient_args = lambda fxn: arg_types(AbstractAmbient)(fxn)
ambient_args.ArgTypeError = arg_types.ArgTypeError
