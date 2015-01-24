__author__ = 'jslowik'
import argparse, binascii

#deobfuscate with key provided in hex
def deXor_hex(key,text):
    textHex = int(text, 16)
    textLength = len(key)
    outputStringHex = ""
    i=0
    while i < len(text):
        substring = textHex[i:(i+textLength)]
        outputStringHex += (key ^ textHex)
        i += (textLength+1)
    return binascii.unhexlify(outputStringHex)

#deobfuscate with key provided as string
def deXor(key, text):
    textLenth = len(key)
    outputString=""
    i=0
    while i < len(text):
        substring = text[i:(i+textLenth)]
        outputString+=(key ^ text)
        i+=(textLenth+1)
    return outputString

def argumentParser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f","--file", help="encoded file")
    parser.add_argument("-k","--key", help="xor key")
    parser.add_argument("-o","--output", help="output file")
    parser.add_argument("-x","--hexKey", help="key in hex", action="store_true")
    return parser.parse_args()

def if __name__ == '__main__':
    None
