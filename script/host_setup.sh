#!/usr/bin/env bash
# this script is used to setup host VM to run auto-test.
# designed to run on Ubuntu 18.04

#######################
# install packages
#######################
# install docker
# https://docs.docker.com/engine/installation/linux/ubuntu/
if ! hash docker 2>/dev/null; then
    apt-get update
    apt-get install -y --no-install-recommends \
        apt-transport-https \
        ca-certificates \
        curl \
        gnupg-agent \
        software-properties-common
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    apt-key fingerprint 0EBFCD88
    add-apt-repository \
        "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
        $(lsb_release -cs) \
        stable"
    apt-get update
    apt -y install docker-ce docker-ce-cli containerd.io
fi

# install docker-compose
if ! hash docker-compose 2>/dev/null; then
    curl -L "https://github.com/docker/compose/releases/download/1.11.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    chmod +x /usr/local/bin/docker-compose
    docker-compose --version
fi

# install py3.6 if not exist, ubuntu 18.04 have python3.6 installed by default.
if ! hash python3.6 2>/dev/null; then
    add-apt-repository -y ppa:jonathonf/python-3.6
    apt update
    apt install -y python3.6
fi

echo "host_setup.sh done~"
