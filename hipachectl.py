#!/usr/bin/env python


"""A command-line tool to manage hipache configurations"""


from __future__ import print_function

from argparse import ArgumentParser


from redis import StrictRedis


def add_virtualhost(r, args):
    ip = args.ip
    port = "" if args.port in (80, 443) else ":{0:d}".format(args.port)
    scheme = "https" if args.port == 443 else "http"
    url = "{0:s}://{1:s}{2:s}".format(scheme, ip, port)

    r.rpush("frontend:{0:s}".format(args.vhost), args.id)
    r.rpush("frontend:{0:s}".format(args.vhost), url)


def delete_virtualhost(r, args):
    r.delete("frontend:{0:s}".format(args.vhost), args.id)


def list_virtualhosts(r, args):
    for i, k in enumerate(r.keys()):
        vhost = k.split(":")[1]
        id, url = r.lrange(k, 0, -1)
        print("{0:d}. {1:s} {2:s} {3:s}".format(i, vhost, id, url))


def parse_args():
    parser = ArgumentParser(description=__doc__)

    parser.add_argument(
        "-H", dest="host", metavar="HOST", type=str,
        help="hipache Host"
    )

    subparsers = parser.add_subparsers(
        title="Commands",
        description="Available Commands",
        help="Description"
    )

    # add
    add_parser = subparsers.add_parser(
        "add",
        help="Add VirtualHost"
    )
    add_parser.set_defaults(func=add_virtualhost)

    add_parser.add_argument(
        "-i", "--ip", dest="ip", default=None, metavar="IP", type=str,
        help="IP Address"
    )

    add_parser.add_argument(
        "-p", "--port", dest="port", default=80, metavar="PORT", type=int,
        help="HTTP Listening Port"
    )

    add_parser.add_argument(
        "id", metavar="ID", type=str,
        help="Container Name or CID"
    )

    add_parser.add_argument(
        "vhost", metavar="VHOST", type=str,
        help="Application VirtualHost"
    )

    # delete
    delete_parser = subparsers.add_parser(
        "delete",
        help="Delete VirtualHost"
    )
    delete_parser.set_defaults(func=delete_virtualhost)

    delete_parser.add_argument(
        "id", metavar="ID", type=str,
        help="Container Name or CID"
    )

    delete_parser.add_argument(
        "vhost", metavar="VHOST", type=str,
        help="Application VirtualHost"
    )

    # list
    list_parser = subparsers.add_parser(
        "list",
        help="List VirtualHosts"
    )
    list_parser.set_defaults(func=list_virtualhosts)

    return parser.parse_args()


def main():
    args = parse_args()

    r = StrictRedis(args.host)

    args.func(r, args)


if __name__ == "__main__":
    main()
