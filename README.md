File Type Identifier
This is a beginner-friendly Python project that identifies a file’s real type using magic numbers (file signatures) instead of relying on file extensions.
The program reads the first few bytes of a file and compares them with known binary signatures stored in a dictionary.

Example:
A file renamed from .exe to .jpg will still be detected as an executable file.
A valid PNG image will be identified correctly even if its extension is changed.

Features:
Detects files using binary signatures
Works regardless of file extension
Lightweight and fast
Easy to understand for beginners
Easy to expand with more file types

How the Program Works:
Takes the file path from the user
Opens the file in binary mode (rb)
Reads the first 32 bytes from the file
Converts the bytes into hexadecimal format
Compares the file header with known signatures
Prints the detected file type

Code Concepts Used
This project helps beginners learn:
File handling
Binary file reading
Dictionaries
Byte strings
Hexadecimal values
Conditional statements (if-elif)
Loops with any()
Basic cybersecurity/file forensics concepts

Future Improvements:
Add ZIP file support
Detect DOCX, XLSX, and PPTX files
Add more image/audio/video formats
Create a graphical user interface (GUI)
Scan folders recursively
Export scan results to a text file
Detect corrupted files
Build a command-line tool

License
This project is free to use for educational and learning purposes.
