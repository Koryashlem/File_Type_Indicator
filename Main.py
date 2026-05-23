from signature import magic_db

filePath = input("Enter file path: ").strip('"')

with open(filePath, "rb") as f:
    header = f.read(32)

matched = False

for fileType, signatures in magic_db.items():
    if any(header.startswith(sig) for sig in signatures):
        print("File Type:", fileType.upper())
        matched = True
        break

if not matched:
    print("Unknown file type")
