# -*- coding: utf-8 -*-

"""
poshpy.models
~~~~~~~~~~~~~~~
This module contains the objects used with PoshPy.
"""


from dataclasses import dataclass


@dataclass
class PowerShellCompleted:
    """Class that is the result of an execution of a PoshPy method.

    Constructor arguments:
    :param return_code: The return code from the PowerShell execution.
    :param standard_out: The stnadard ouptut from the PowerShell execution.
    :param standard_error: The standard error from the PowerShell execution.
    """

    return_code: int
    standard_out: str
    standard_error: str
