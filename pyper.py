#!/usr/bin/env python3

import socket

from argparse import ArgumentParser
from impacket import smb, smbconnection
from mysmb import MYSMB

DEFAULT_PIPES = [ "browser", "spoolss", "netlogon", "lsarpc", "samr" ]

def main(args):
    pipes = DEFAULT_PIPES
    username = ""
    password = ""

    if args.username:
        username = args.username

    if args.password:
        password = args.password

    if args.wordlist:
        with open(args.wordlist, "r") as f:
            for name in f:
                pipes.add(name.rstrip())

    print("[*] finding named pipes for: {}".format(args.target))

    conn = MYSMB(args.target)
    conn.get_socket().setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    conn.login(username, password, maxBufferSize=4356)
	
    tid = conn.tree_connect_andx("\\\\"+conn.get_remote_host()+"\\"+"IPC$")
    for pipe in pipes:
        try:
            fid = conn.nt_create_andx(tid, pipe)
            conn.close(tid, fid)
            print("\x1b[0;32;40m[+] {}\x1b[0m".format(pipe))
        except smb.SessionError as e:
            print("\x1b[0;31;40m[-] {}\x1b[0m".format(pipe))
            continue

    conn.disconnect_tree(tid)

if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument("target", help="IP address of target")

    parser.add_argument("-w", "--wordlist", help="wordlist file to use for pipe names")
    parser.add_argument("-u", "--username", help="username to use for authentication, defaults to NULL")
    parser.add_argument("-p", "--password", help="password to use for authentication, defaults to NULL")

    args = parser.parse_args()
    main(args)
