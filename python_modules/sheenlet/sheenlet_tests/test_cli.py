import subprocess

from click.testing import CliRunner
from sheenlet.cli import dagit


def test_invoke_ui():
    runner = CliRunner()
    result = runner.invoke(dagit, ["--version"])
    assert "sheenlet, version" in result.output


def test_invoke_cli_wrapper_with_nonexistant_option():
    process = subprocess.Popen(["sheenlet", "--fubar"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    _, stderr = process.communicate()
    assert process.returncode != 0
    assert b"error: no such option: --fubar\n" in stderr.lower()


def test_invoke_cli_wrapper_with_invalid_option():
    process = subprocess.Popen(["sheenlet", "-d", "."], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    _, stderr = process.communicate()
    assert process.returncode != 0
    assert (
        b"Error: Invalid set of CLI arguments for loading repository/pipeline. See --help for details.\n"
        in stderr
    )
