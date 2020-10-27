# -*- coding: utf-8 -*-

"""
poshpy.api
~~~~~~~~~~~~
This module implements the Poshpy API.
:copyright: (c) 2020 by Jamie Phillips.
:license: Apache2, see LICENSE for more details.
"""

import subprocess
import base64

from poshpy.models import PowerShellCompleted


def execute_command(command):
    """
    Executes PowerShell with the -Command argument, passing in the command provided.

    :param command: PowerShell command to execute.
    :return: :class:`PowerShellCompleted <PowerShellCompleted>` data class.
    :rtype: PowerShell
    Usage::
      >>> import poshpy
      >>> completed = poshpy.execute_command("Write-Host 'Hello Wolrd!'")
      >>> completed
      <PowerShellCompleted(return_code=0, standard_out=b'Hello Wolrd!\n', standard_error=b'')>
    """
    completed = subprocess.run(["powershell", "-Command", command], capture_output=True)
    return PowerShellCompleted(completed.returncode, completed.stdout, completed.stderr)


def execute_encoded_command(command):
    """
    Executes PowerShell with the -EncodedCommand argument and encodes the command.

    :param command: PowerShell command to be encoded and executed.
    :return: :class:`PowerShellCompleted <PowerShellCompleted>` data class.
    :rtype: PowerShell
    Usage::
      >>> import poshpy
      >>> completed = poshpy.execute_encoded_command("Write-Host 'Hello Wolrd!'")
    """
    cmd = base64.b64encode(command.encode('utf-16le'))
    completed = subprocess.run(["powershell", "-EncodedCommand", cmd], capture_output=True)
    return PowerShellCompleted(completed.returncode, completed.stdout, completed.stderr)


def execute_file(file_path):
    """
    Executes PowerShell with the -File argument and passes the file path.

    :param file_path: PowerShell file to execute.
    :return: :class:`PowerShellCompleted <PowerShellCompleted>` data class.
    :rtype: PowerShell
    Usage::
      >>> import poshpy
      >>> from os import path
      >>> full_path = path.abspath("HelloWorld.ps1")
      >>> completed = poshpy.execute_file(full_path)
    """
    completed = subprocess.run(["powershell", "-File", file_path], capture_output=True)
    return PowerShellCompleted(completed.returncode, completed.stdout, completed.stderr)

