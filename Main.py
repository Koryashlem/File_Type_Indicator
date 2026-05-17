filePath = input("Enter file path: ").strip('"')

magic_db = {
    "pdf": [b"%PDF"],
    "png": [bytes.fromhex("89504E470D0A1A0A")],
    "jpg": [bytes.fromhex("FFD8FF")],

}


with open(filePath, "rb") as readFile:
    header = readFile.read(16)

print("File Hex: ",header.hex())


# PNG
if header.startswith(magic_db["png"][0]):
    print("File Type: PNG file")

# JPG / JPEG
elif header.startswith(magic_db["jpg"][0]):
    print("File Type: JPG/JPEG file")

# PDF
elif header.startswith(magic_db["pdf"][0]):
    print("File Type: PDF file")

