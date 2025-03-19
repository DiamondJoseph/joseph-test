import subprocess
import sys

from test_joseph import __version__


def test_cli_version():
    cmd = [sys.executable, "-m", "test_joseph", "--version"]
    assert subprocess.check_output(cmd).decode().strip() == __version__
