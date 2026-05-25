import os
from signature import magic_db
from signature import extension_map

print("----Welcome to the File Type Identifier----\n")

filePath = input("Enter file path: ").strip('"')

# Extract extension
extension = os.path.splitext(filePath)[1]
extension = extension.replace(".", "").lower()

with open(filePath, "rb") as readFile:
    header = readFile.read(64)

found = False
actualType = None

for fileType, signatures in magic_db.items():

    for offset, sig in signatures:

        if header[offset:offset + len(sig)] == sig:

            actualType = fileType
            found = True
            break

    if found:
        break

if found:

    print("Detected File Type:", actualType.upper())
    print("File Extension:", extension.upper())

    if extension in extension_map.get(actualType, []):
        print("Extension Status: VALID")
    else:
        print("WARNING: Extension does NOT match actual file type")

else:
    print("Unknown file type")

print("Actual filename:", os.path.basename(filePath))
