'''
Three methods to test the existence of a file
'''

# Force with a try-except block
try: 
    fh = open('/path/to/file', 'r') 
except FileNotFoundError: 
    pass

# Leverage the OS package
import os 
exists = os.path.isfile('/path/to/file')

# Wrap the path in an object for enhanced functionality
from pathlib import Path
config = Path('/path/to/file') 
if config.is_file(): 
    pass