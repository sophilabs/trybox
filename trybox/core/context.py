import subprocess

class Context(object):

    def __init__(self, venv, repository):
        self._venv = venv
        self._repository = repository

    def run_command(self, command):
        full_command = ['bash', '-c', "source {0}/bin/activate && cd {1} && {2}".format(
            self._venv,
            self._repository,
            command
        )]
        p = subprocess.Popen(full_command,
            stdin = subprocess.PIPE,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE)
        output, error = p.communicate()
        return {'output': output, 'error': error }

    def create_file(self, filename):
        pass

    def create_directory(self, directory):
        pass

    def save_file(self, filename, content):
        pass