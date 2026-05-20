filePath = input("Enter file path: ").strip('"')

magic_db = {
    "pdf": [b"%PDF"],
    "png": [bytes.fromhex("89504E470D0A1A0A")],
    "jpg": [bytes.fromhex("FFD8FF")],
    "gif": [b"GIF87a", b"GIF89a"],
    "mp3": [bytes.fromhex("494433")],
    "wav": [b"RIFF"],
    "exe": [b"MZ"],
    "rar": [bytes.fromhex("526172211A0700")],

}
with open(filePath, "rb") as readFile:
    header = readFile.read(32)
print("File Hex:", header.hex())

# PDF
if header.startswith(magic_db["pdf"][0]):
    print("File Type: PDF")

# PNG
elif header.startswith(magic_db["png"][0]):
    print("File Type: PNG")

# JPG
elif header.startswith(magic_db["jpg"][0]):
    print("File Type: JPG/JPEG")

# GIF
elif any(header.startswith(sig) for sig in magic_db["gif"]):
    print("File Type: GIF")


# MP3
elif header.startswith(magic_db["mp3"][0]):
    print("File Type: MP3")

# WAV
elif header.startswith(magic_db["wav"][0]):
    print("File Type: WAV")

# Windows EXE
elif header.startswith(magic_db["exe"][0]):
    print("File Type: Windows Executable (EXE)")


# RAR
elif header.startswith(magic_db["rar"][0]):
    print("File Type: RAR Archive")

else:
    print("Unknown file type")
