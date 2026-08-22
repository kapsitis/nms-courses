import sys
import zlib

def string_to_8hex(s):
    return '{:08x}'.format(zlib.crc32(s.encode('utf-8')) & 0xffffffff)

if __name__ == "__main__":
    if len(sys.argv) < 2: 
        print("Usage: python hash_value.py <arg>")
        sys.exit(1)
    val = string_to_8hex(sys.argv[1])
    print(f"hash({sys.argv[1]}) = {val}")
    
