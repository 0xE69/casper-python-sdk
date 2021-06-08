from pycspr.serialization.utils import CLTypeKey
from pycspr.serialization.utils import int_from_le_bytes
from pycspr.serialization.utils import int_to_le_bytes



# Formal type within CL type system.
TYPEOF = CLTypeKey.U8

# Length when encoded.
_ENCODED_LENGTH: int = 1

# Dimension constraint.
_MIN_SIZE = 0
_MAX_SIZE = (2 ** 8) - 1


# Decodes input data.
decode = lambda v: int_from_le_bytes(v, False)


# Encodes a domain type instance.
to_bytes = lambda v: int_to_le_bytes(v, _ENCODED_LENGTH, False)


# Returns length in bytes of encoded data.
get_encoded_length = lambda _: _ENCODED_LENGTH


# A predicate returning a flag indicating whether encoded data can be decoded.
is_decodeable = lambda encoded: isinstance(encoded, list) and len(encoded) == _ENCODED_LENGTH


# A predicate returning a flag indicating whether domain type instance can be encoded.
is_encodeable = lambda v: isinstance(v, int) and _MIN_SIZE <= v <= _MAX_SIZE
