import json
import os
import pathlib
import typing

import pytest


_PATH_TO_ASSETS = pathlib.Path(os.path.dirname(__file__)).parent / "assets"
_PATH_TO_VECTORS = _PATH_TO_ASSETS / "vectors"


@pytest.fixture(scope="session")
def cl_types() -> list:
    class _Accessor():
        def __init__(self):
            self.fixture = _read_vector("cl_types_simple.json") + _read_vector("cl_types_complex.json")

        def get_vectors(self, typeof: str) -> list:
            typeof = typeof if isinstance(typeof, str) else typeof.name
            return [i for i in self.fixture if i["typeof"] == typeof.upper()]

        def get_vector(self, typeof: str) -> dict:
            return self.get_vectors(typeof)[0]

        def get_value(self, typeof: str) -> object:
            return self.get_vector(typeof)["value"]

        def get_value_as_bytes(self, typeof: str) -> bytes:
            return bytes.fromhex(self.get_value(typeof))
    
    return _Accessor()


@pytest.fixture(scope="session")
def crypto_1() -> list:
    data = _read_vector("crypto_hashes.json")
    for i in data:
        for j in i["hashes"]:
            j["digest"] = bytes.fromhex(j["digest"])

    return data


@pytest.fixture(scope="session")
def crypto_2() -> list:
    data = _read_vector("crypto_key_pairs.json")
    for i in data:
        i["pvk"] = bytes.fromhex(i["pvk"])
        i["pbk"] = bytes.fromhex(i["pbk"])
        i["accountKey"] = bytes.fromhex(i["accountKey"])
        i["accountHash"] = bytes.fromhex(i["accountHash"])

    return data


@pytest.fixture(scope="session")
def crypto_3() -> list:
    data = _read_vector("crypto_signatures.json")
    for i in data:
        i["signingKey"]["pvk"] = bytes.fromhex(i["signingKey"]["pvk"])
        i["sig"] = bytes.fromhex(i["sig"])

    return data


@pytest.fixture(scope="session")
def deploy_1() -> list:
    data = _read_vector("deploys_1.json")
    for i in data:
        i["bytes"]["payment"] = bytes.fromhex(i["bytes"]["payment"])
        i["bytes"]["session"] = bytes.fromhex(i["bytes"]["session"])
        i["hashes"]["body"] = bytes.fromhex(i["hashes"]["body"])
        i["hashes"]["deploy"] = bytes.fromhex(i["hashes"]["deploy"])
        i["session"]["target"] = bytes.fromhex(i["session"]["target"])

    return data

def _read_vector(fname: str, parser: typing.Callable = json.load):
    with open(_PATH_TO_VECTORS / fname) as fhandle:
        return fhandle.read() if parser is None else parser(fhandle)