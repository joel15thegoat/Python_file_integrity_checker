import hashlib 
import os 
def calculate_hash (file_path) : 
  sha256_hash = hashlib. sha256()  
  with open(file_path, "rb") as f: 
    for byte_block in iter( lambda: f.read(4096), b"") : 
      sha256_hash.update(byte_block) 
  return sha256_hash. hexdigest ()  
def monitor_integrity(file_path, expected_hash) : 
  current_hash = calculate_hash(file_path)  
  if current_hash == expected_hash: 
    print ("File integrity is maintained.")  
  else: 
    print ("File integrity has been compromised. ") 
# Usage 
file_path = "important_file. txt" 
expected_hash = calculate_hash (file_path) 
monitor_integrity(file_path, expected_hash)  
