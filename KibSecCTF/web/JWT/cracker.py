import hmac
import hashlib
import base64

header_payload = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoidXNlcjU3MTRmN2Y4In0"
FILE = "jwt.secrets.list"
orig_sig = "Rek40LcNe-Daxf5o67y5MQmo1qstTL0mtET6OCUjblQ"

with open(FILE, 'r') as f:
	for secret in f:
		secret = base64.urlsafe_b64encode(secret.strip().encode('utf-8'))
		#print("Secret: ",secret)
		signature = hmac.new(
			secret,
			msg=bytes(header_payload, 'utf-8'), 
			digestmod=hashlib.sha256
			).digest()

		sig_base64url = base64.urlsafe_b64encode(signature).rstrip(b"=").decode('utf-8')
		#print(sig_base64url + "==" + orig_sig + "?")
		if (sig_base64url == orig_sig):
			print ("Found secret! ", secret)
			f.close()
			exit(1)
f.close()
print ("Secret not found :(")


