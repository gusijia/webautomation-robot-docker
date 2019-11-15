from subprocess import run, DEVNULL

class SanityCheck(object):

    def ping_machine_should_succeed(self, machine):
        ret = run(['ping', '-c', '3', machine], stdout=DEVNULL)
        if ret.returncode:
            raise AssertionError(f'ping to {machine} failed')
        else:
            print(f'ping to {machine} is successful')

    def ping_machines_should_succeed(self, containers):
        for container in containers:
            self.ping_machine_should_succeed(container)
