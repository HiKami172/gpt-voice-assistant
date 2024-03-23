import dataclasses

from service_managers.service_manager import ServiceManager
import subprocess
import os
from json import dumps

from typing import Dict


@dataclasses.dataclass
class Program:
    name: str
    executable_path: str
    start_parameters: Dict

    def start(self, parameters):
        pass


class ProgramsManager(ServiceManager):
    def __init__(self, programs):
        self.programs = programs

    def run_program(self, name):
        """
        Runs the specified program on user's computer.

        :param string name: Program's name in english
        :return: Result of the program execution attempt
        """
        program = self.programs[name]
        executable = program["executable"]
        params = program["parameters"]
        args = []
        args.append(executable)
        args.extend([f"--{k}={v}" for k, v in params.items()])
        args_str = ' '.join(args)
        completed_process = subprocess.run(args_str)
        result = {
            "args": completed_process.args,
            "return_code": completed_process.returncode,
        }
        return dumps(result)
