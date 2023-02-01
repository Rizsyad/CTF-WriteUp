from pwn import *
import sys

# running the server: python3.9 payload.py RMT 0.0.0.0 8080
# running the local: python3.9 payload.py

def init():
    if args.RMT:
        log.info(f"Connected Server {sys.argv[1]}:{sys.argv[2]}")
        p = remote(sys.argv[1], sys.argv[2])
    else:
        log.info("Opened File")
        p = process('./chall')

    return Exploit(p), p

class Exploit:
    def __init__(self, p: process):
        self.p = p

    def debug(self, script=None):
        if not args.RMT:
            if script:
                attach(self.p, script)
            else:
                attach(self.p)
    
    def enter_whats_that(self, what):
        p = self.p
        log.info("Send Payload Input")
        p.sendlineafter(b"What's that?\n", what)

    def exploit(self):
        p = self.p
      

        


if __name__ == "__main__":
    x, p = init()
    # x.debug((
    #     "break *0x1000014a1"
    # ))

    x.exploit()
    p.interactive()