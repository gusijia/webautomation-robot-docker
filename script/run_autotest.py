#!/usr/bin/env python3.6

from subprocess import run
import os
from pathlib import Path
import configparser

CUR_DIR = Path(os.path.realpath(__file__)).parent
PROJ_HOME = CUR_DIR.parent
PROPTY_PATH = PROJ_HOME / 'conf' / 'main.properties'
CONFIG = configparser.ConfigParser()
CONFIG.read(str(PROPTY_PATH))
CONF = dict(CONFIG['MAIN'])

CONF['docker_dir'] = PROJ_HOME / 'docker'
CONF['compose_yml'] = CONF['docker_dir'] / 'docker-compose.yml'
CONF['volume_dir'] = PROJ_HOME / 'volume'


def export_vars():
    """
    export env vars for running docker-compose.
    :return:
    """
    for var in CONF:
        os.putenv(var, CONF[var])


if __name__ == "__main__":
    export_vars()
    print('\n\nstart building docker compose ...')
    run(['docker-compose', '--project-name', CONF['proj_name'], '--file',
         CONF['compose_yml'], 'build'])
    print('\n\nstart running docker compose ...')
    run(['docker-compose', '--project-name', CONF['proj_name'], '--file',
         CONF['compose_yml'], 'up', '-d'])
    print('\n\nstart robot automation testing ...')
    cmd = ("docker exec -i robot sh -c 'python "
           "\"${ROBOT_HOME}/script/run_robot.py\"'")
    run(cmd, shell=True)
