import pytest

from sheenflow._check import ParameterCheckError
from sheenflow._core.definitions.logical_version import LogicalVersion


def test_logical_version_construction():
    ver = LogicalVersion("foo")
    assert ver.value == "foo"

    with pytest.raises(ParameterCheckError):
        LogicalVersion(100)  # type: ignore


def test_logical_version_equality():
    assert LogicalVersion("foo") == LogicalVersion("foo")
