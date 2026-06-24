# Python_file_integrity_checker
A simple Python file integrity checker using SHA-256 hashing. It reads files in chunks for memory efficiency and verifies if the file has been tampered with. 

## Features
- SHA-256 hashing via `hashlib`
- Memory-friendly chunked file reading
- Straightforward integrity check function
- Perfect for learning about hashing and basic security monitoring

## Usage
**1. Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/file-integrity-checker.git
   cd file-integrity-checker
   ```
 **2. run the script**
   ```bash
   python integrity_checker.py
   ```
## Customization
Change the target file by modifying ```file_path = "your_file.ext".```

Adjust the read block size by replacing``` 4096``` with any value.

Switch to a different hash algorithm (e.g., MD5, SHA-1) by changing `hashlib.sha256()` to `hashlib.md5()` or `hashlib.sha1()`, but note SHA-256 is recommended for integrity checks from wat i heared.
## licence
- this is published under the MIT [licenece](https://mit-license.org/)
## have fun
