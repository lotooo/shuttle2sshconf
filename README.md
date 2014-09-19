# shuttle2sshconf


## Goal

The goal of this script is to help you convert your shuttle.json file to a traditionnal .ssh/config syntax.
I wrote it to be able to transfer my server list to a linux jumpbox and use the zsh ssh host auto-completion.

## Usage

> $ ./shuttle2sshconfig.py  
> usage: shuttle2sshconf.py [-h] [-c CONF]
> 
> optional arguments:
>   -h, --help            show this help message and exit
>   -c CONF, --conf CONF  Shuttle configuration file

By default it opens ~/.shuttle.json

## Contribute

Please send me your feedback
