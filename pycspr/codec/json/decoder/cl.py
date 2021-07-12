import typing

from pycspr.codec.byte_array import decode as byte_array_decoder
from pycspr.types import CLValue
from pycspr.types import CLType
from pycspr.types import CLTypeKey
from pycspr.types import TYPES_NUMERIC
from pycspr.types import CLType_ByteArray
from pycspr.types import CLType_List
from pycspr.types import CLType_Map
from pycspr.types import CLType_Option
from pycspr.types import CLType_Simple
from pycspr.types import CLType_Tuple1
from pycspr.types import CLType_Tuple2
from pycspr.types import CLType_Tuple3



def decode_cl_type(obj) -> CLType:
    def _decode_byte_array():
        return CLType_ByteArray(size=obj["ByteArray"])

    def _decode_option():
        return CLType_Option(inner_type=decode_cl_type(obj["Option"]))
    
    def _decode_simple():
        return CLType_Simple(typeof=CLTypeKey[obj])

    # Set decoder.
    if isinstance(obj, dict):
        if "ByteArray" in obj:
            decoder = _decode_byte_array
        elif "Option" in obj:
            decoder = _decode_option
        else:
            raise NotImplementError()
    else:
        decoder = _decode_simple
    
    return decoder()


def decode_cl_value(obj: typing.Union[dict, str]) -> CLValue:
    """Decodes a CL value.

    """    
    cl_type = decode_cl_type(obj["cl_type"])
    as_bytes = bytes.fromhex(obj["bytes"])

    if isinstance(cl_type, (CLType_Simple, CLType_ByteArray, CLType_Option)):
        parsed = byte_array_decoder(cl_type, as_bytes)
    else:
        print(cl_type)
        parsed = None

    return CLValue(
        bytes=as_bytes,
        cl_type=cl_type,
        parsed=parsed
        )
