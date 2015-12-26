hipachectl
==========

[![Image Layers](https://badge.imagelayers.io/prologic/hipachectl:latest.svg)](https://imagelayers.io/?images=prologic/hipachectl:latest)

hipachectl is a command-line tool and library to manage [dotCloud](http://dotcloud.com/)'s [hipache](https://github.com/hipache/hipache) load balancer and reverse proxy. hipachectl lets you:

-   list configured virtual hosts
-   add a new virtual host
-   delete a virtual host

hipachectl is MIT licensed.

Installation
------------

Either pull the automatically updated [Docker](http://docker.com/) image:

    $ docker pull prologic/hipachectl

Or install from the development repository:

    $ git clone https://github.com/prologic/hipachectl.git
    $ cd hipachectl
    $ pip install .

Usage
-----

To use hipachectl from [Docker](http://docker.com/):

    $ docker run prologic/hipachectl -u tcp://ip:port <command>

Or:

    $ hipachectl -u tcp://ip:port <command>

Where `ip` and `port` are the IP Address and Port of the [hipache](https://github.com/hipache/hipache) instance or the IP/Port of the Redis instance used. e.g: `tcp://redis:6379`

Or if you have a named [hipache](https://github.com/hipache/hipache) instance you can use `--link`:

    $ docker run --link hipache prologic/hipachectl

For help use the `--help` option.
