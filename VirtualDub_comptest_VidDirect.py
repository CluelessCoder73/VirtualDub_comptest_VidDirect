# This script generates a VirtualDub "vdscript" file for compressibility tests.
# The default configuration creates 100 cuts (starting with the 10,000th frame), keeping 500 frames and skipping the next 19,500 frames.
# The generated cutlist is then inserted into a .vdscript template and saved as 'output.vdscript'.
# You can customize the number of cuts, frames to keep, frames to skip, and start frame by modifying the variables.
# Note: Video mode is set to "Direct stream copy"!
# This script was tested and works with:
# - Python 3.12.5    
# - VirtualDub 1.10.4

# Author: CluelessCoder73
# Date: 22nd Aug 2024

# Define the total number of cuts
num_cuts = 100

# Define the number of frames to keep and skip
frames_to_keep = 500
frames_to_skip = 19500

# Start frame for the first cut
start_frame = 10000

# List to hold the generated VirtualDub.subset.AddRange lines
cut_lines = []

# Generate the cut ranges
for i in range(num_cuts):
    cut_lines.append(f"VirtualDub.subset.AddRange({start_frame},{frames_to_keep});")
    start_frame += frames_to_keep + frames_to_skip

# Define the template of the .vdscript file (V direct stream copy is enabled)
vdscript_template = """
VirtualDub.audio.SetSource(1);
VirtualDub.audio.SetMode(0);
VirtualDub.audio.SetInterleave(1,500,1,0,0);
VirtualDub.audio.SetClipMode(1,1);
VirtualDub.audio.SetEditMode(1);
VirtualDub.audio.SetConversion(0,0,0,0,0);
VirtualDub.audio.SetVolume();
VirtualDub.audio.SetCompression();
VirtualDub.audio.EnableFilterGraph(0);
VirtualDub.video.SetInputFormat(0);
VirtualDub.video.SetOutputFormat(7);
VirtualDub.video.SetMode(0);
VirtualDub.video.SetSmartRendering(0);
VirtualDub.video.SetPreserveEmptyFrames(0);
VirtualDub.video.SetFrameRate2(0,0,1);
VirtualDub.video.SetIVTC(0, 0, 0, 0);
VirtualDub.video.SetCompression();
VirtualDub.video.filters.Clear();
VirtualDub.audio.filters.Clear();
VirtualDub.subset.Clear();
{cut_lines}
VirtualDub.video.SetRange();
"""

# Join the generated cut lines with newlines
cut_lines_str = "\n".join(cut_lines)

# Fill in the cut lines into the template
vdscript_content = vdscript_template.format(cut_lines=cut_lines_str)

# Save the content to a .vdscript file
with open("output.vdscript", "w") as file:
    file.write(vdscript_content)

print("VirtualDub script generated successfully!")
