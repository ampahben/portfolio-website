import secrets

# Generate a 128-bit key (16 bytes)
secret_key = secrets.token_hex(16)  
print("Your secret key:", secret_key)