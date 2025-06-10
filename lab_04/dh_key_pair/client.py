from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes


def generate_client_key_pair(parameters):
    """
    Generate client's DH private and public key using server's parameters.
    """
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key


def derive_shared_secret(private_key, server_public_key):
    """
    Derive shared secret from client's private key and server's public key.
    """
    shared_key = private_key.exchange(server_public_key)
    return shared_key


def main():
    # Load server's public key
    with open("server_public_key.pem", "rb") as f:
        server_public_key = serialization.load_pem_public_key(f.read())

    # Get parameters from server's key
    parameters = server_public_key.parameters()

    # Generate client key pair using same parameters
    private_key, public_key = generate_client_key_pair(parameters)

    # Derive shared secret
    shared_secret = derive_shared_secret(private_key, server_public_key)

    # Print shared secret in hex (for debug)
    print("[+] Shared Secret:", shared_secret.hex())


if __name__ == "__main__":
    main()
