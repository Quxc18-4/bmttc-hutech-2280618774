from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization


def generate_dh_parameters():
    """
    Generate DH parameters (shared between both server and client).
    """
    parameters = dh.generate_parameters(generator=2, key_size=2048)
    return parameters


def generate_server_key_pair(parameters):
    """
    Generate server's DH private and public key using given parameters.
    """
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key


def save_public_key(public_key, filename="server_public_key.pem"):
    """
    Save public key to a PEM file.
    """
    with open(filename, "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))


def main():
    parameters = generate_dh_parameters()
    private_key, public_key = generate_server_key_pair(parameters)
    save_public_key(public_key)
    print("[+] Server DH public key saved to 'server_public_key.pem'")


if __name__ == "__main__":
    main()
