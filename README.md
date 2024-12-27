# VirtualDub_comptest_VidDirect
This script generates a VirtualDub "vdscript" file for compressibility tests.
The default configuration creates 100 cuts (starting with the 10,000th frame), keeping 500 frames and skipping the next 19,500 frames.
The generated cutlist is then inserted into a .vdscript template and saved as 'output.vdscript'.
You can customize the number of cuts, frames to keep, frames to skip, and start frame by modifying the variables.
Note: Video mode is set to "Direct stream copy"!
This script was tested and works with:
- Python 3.12.5    
- VirtualDub 1.10.4