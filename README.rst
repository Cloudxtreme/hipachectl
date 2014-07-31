.. docker:: http://docker.com/
.. dotCloud:: http://dotcloud.com/
.. hipache:: https://github.com/hipache/hipache


hipachectl
==========

hipachectl is a command-line tool to manage `dotCloud`_'s `hipache`_
load balancer and reverse proxy. hipachectl lets you:

- list configured virtual hosts
- add a new virtual host
- delete a virtual host


Installation
------------

Either pull the prebuilt `Docker`_ image::
    
    $ docker pull prologic/hipachectl

Or install from the development repository::
    
    $ hg clone https://bitbucket.org/prologic/hipachectl
    $ cd hipachectl
    $ pip install -r requirements.txt


Usage
-----

To use hipachectl from `docker`_::
    
    $ docker run prologic/hipachectl -H <hipache_ip> <command>

Or::
    
    $ ./hipachectl.py -H <docker_ip> <command>

For help user the ``--help`` option.
