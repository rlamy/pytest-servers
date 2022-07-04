import os
from pathlib import Path

from pytest_servers.utils import is_pytest_session


def test_is_pytest_session():
    assert is_pytest_session()


def test_s3_fake_creds_file(
    s3_fake_creds_file,  # pylint: disable=unused-argument
):
    assert os.getenv("AWS_PROFILE") is None
    assert os.getenv("AWS_ACCESS_KEY_ID") == "pytest-servers"
    assert os.getenv("AWS_SECRET_ACCESS_KEY") == "pytest-servers"
    assert os.getenv("AWS_SECURITY_TOKEN") == "pytest-servers"
    assert os.getenv("AWS_SESSION_TOKEN") == "pytest-servers"
    assert (Path("~").expanduser() / ".aws").exists()
