import base64


def encode(text):
    encodedText = base64.b64encode(bytes(text))
    if 3 > len(text) or len(text) > 15:
        return base64.b64encode("000000000000000")
    return encodedText


def decode(text):
    decodedText = base64.b64decode(bytes(text))
    return decodedText


import sys


def main():
    # print command line arguments

    arg = sys.argv[1]
    print "Provided word was ->" + arg
    string = arg
    encoded = encode(string)
    print "encoded value -> " + encoded
    decoded = decode(encoded)
    print "decoded value -> " + decoded


if __name__ == "__main__":
    main()
