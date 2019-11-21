#!/usr/bin/env python3.6

from subprocess import run, PIPE
import os
from pathlib import Path
import tempfile

CONF_DIR_P = Path(os.environ['CONF_DIR'])


def run_by_argfile(arg_scripts):
    if isinstance(arg_scripts, (list, tuple)):
        argfiles = arg_scripts
    else:
        argfiles = [arg_scripts]
    args = ''
    for argfile in argfiles:
        ret = run(['sh', argfile], stdout=PIPE)
        args += ret.stdout.decode()
    # run robot command
    with tempfile.NamedTemporaryFile(mode='w+') as fp:
        fp.write(args)
        fp.seek(0)
        print(fp.name)
        run(['robot', '--argumentfile', fp.name])


if __name__ == "__main__":

    print("start robot framework for autotest...")
    arg_main = CONF_DIR_P / 'arg_main.sh'
    run_by_argfile(arg_main)
