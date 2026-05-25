from signature import magic_db

try:
    filePath = input("Enter file path: ").strip('"')
    with open(filePath, "rb") as readFile:
        header = readFile.read(64)

    found = False
    for fileType, signatures in magic_db.items():
        for offset, sig in signatures:
            if header[offset:offset + len(sig)] == sig:
                print("File Type:", fileType.upper())
                found = True
                break
        if found:
            break
    if not found:
        print("Unknown file type")
except Exception as e:
    print("Error:", e)

input("Press Enter to exit...")
