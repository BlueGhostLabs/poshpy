#!/usr/bin/env python
"""Tests for `poshpy` package."""
# pylint: disable=redefined-outer-name

import poshpy


def test_execute_command(fake_process):
    command = "Write-Host 'Hello Wolrd!'"
    fake_process.register_subprocess(["powershell", "-Command", command],
                                     stdout=[b"Write-Host 'Hello Wolrd!'"],
                                     returncode=0)

    completed = poshpy.execute_command(command)

    assert completed.return_code == 0
    assert completed.standard_out == b"Write-Host 'Hello Wolrd!'\n"
    assert not completed.standard_error


def test_execute_command_with_error(fake_process):
    command = "Write-Hst 'Hello Wolrd!'"
    fake_process.register_subprocess(["powershell", "-Command", command],
                                     stderr=[b"Improperly formed command."],
                                     returncode=1)

    completed = poshpy.execute_command(command)

    assert completed.return_code == 1
    assert not completed.standard_out
    assert completed.standard_error == b"Improperly formed command.\n"


def test_execute_file(fake_process):
    file = "/Hello-World.ps1"
    fake_process.register_subprocess(["powershell", "-File", file],
                                     stdout=[b"File Hello-World executed."],
                                     returncode=0)

    completed = poshpy.execute_file(file)

    assert completed.return_code == 0
    assert completed.standard_out == b"File Hello-World executed.\n"
    assert not completed.standard_error


def test_execute_file_with_error(fake_process):
    file = "/Hello-World.ps1"
    fake_process.register_subprocess(["powershell", "-File", file],
                                     stderr=[b"File not found."],
                                     returncode=1)

    completed = poshpy.execute_file(file)

    assert completed.return_code == 1
    assert not completed.standard_out
    assert completed.standard_error == b"File not found.\n"
