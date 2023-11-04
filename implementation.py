import falcon

secret_key = falcon.SecretKey(512)
public_key = falcon.PublicKey(secret_key)

print(secret_key)
print()
print(public_key)
print()

message = b"Hello!"

signature = secret_key.sign(message)
print(f"Message = {message}")
print(f"Signature = {signature}")

print()
print(f"Legit? {public_key.verify(message, signature)}")

print(signature[5])
print((ord(b"\x01")^signature[5]))

tampered_byte = ord(b"\x01") ^ signature[5]
bad_signature = signature[0:5] + tampered_byte.to_bytes(1, 'little') + signature[6:]
print(bad_signature)

print(f"Legit after modification? {public_key.verify(message, bad_signature)}")