=====
Usage
=====

To use poshpy in a project::

    import poshpy
    completed_cmd = poshpy.execute_command("Write-Host 'Hello Wolrd!'")
    if completed_cmd.return_code == 0:
        print(completed_cmd.standard_out)
    else:
        print(completed_cmd.standard_error)
