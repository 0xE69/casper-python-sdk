import dataclasses

from pycspr.types.cl_types import CL_Type_Result
from pycspr.types.cl_values.base import CL_Value


@dataclasses.dataclass
class CL_Result(CL_Value):
    """Represents a CL type value: function invocation result.
    
    """
    # Associated value.
    value: object

    #region Equality & serialisation

    def __eq__(self, other) -> bool:
        return self.value == other.value

    def as_bytes(self) -> bytes:
        raise NotImplementedError()

    def as_cl_type(self) -> CL_Type_Result:
        return CL_Type_Result()

    def as_parsed(self) -> str:
        raise NotImplementedError()

    @staticmethod
    def from_bytes(as_bytes: bytes) -> "CL_Result":
        raise NotImplementedError()

    #endregion