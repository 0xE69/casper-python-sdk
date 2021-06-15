import typing

from pycspr.codec.byte_array.utils import int_to_le_bytes



# Length when encoded.
ENCODED_LENGTH: int = 1

# Dimension constraints.
MIN = 0
MAX = (2 ** 8) - 1


def encode(value: int) -> typing.List[int]:
    """Maps parsed value to it's CL byte array representation.

    :param value: Value to be mapped.
    :returns: CL byte array representation.
        
    """
    return int_to_le_bytes(value, ENCODED_LENGTH, False)
