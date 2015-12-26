hipachectl
==========

[![Image Layers](https://badge.imagelayers.io/prologic/hipachectl:latest.svg)](https://imagelayers.io/?images=prologic/hipachectl:latest)

hipachectl is a command-line tool to manage [dotCloud](http://dotcloud.com/)'s [hipache](https://github.com/hipache/hipache) load balancer and reverse proxy. hipachectl lets you:

-   list configured virtual hosts
-   add a new virtual host
-   delete a virtual host

hipachectl is MIT licensed.

Installation
------------

Either pull the prebuilt [Docker](http://docker.com/) image:

    $ docker pull prologic/hipachectl

Or install from the development repository:

    $ git clone https://github.com/prologic/hipachectl.git
    $ cd hipachectl
    $ pip install -r requirements.txt

Usage
-----

To use hipachectl from [Docker](http://docker.com/):

    $ docker run prologic/hipachectl -H <hipache_ip> <command>

Or:

    $ hipachectl -H <docker_ip> <command>

For help user the `--help` option.
