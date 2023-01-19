import os
import struct

def generate_uuid_v4():
    # Get random bytes from the operating system
    random_bytes = bytearray(os.urandom(16))
    # Set the version number (4 bits) and variant (2 bits)
    random_bytes[6] = (random_bytes[6] & 0x0f) | 0x40
    random_bytes[8] = (random_bytes[8] & 0x3f) | 0x80
    random_bytes = bytes(random_bytes)
    # Format the bytes as a string
    return '{:02x}{:02x}{:02x}{:02x}-{:02x}{:02x}-{:02x}{:02x}-{:02x}{:02x}-{:02x}{:02x}{:02x}{:02x}{:02x}{:02x}'.format(*struct.unpack('16B', random_bytes))
