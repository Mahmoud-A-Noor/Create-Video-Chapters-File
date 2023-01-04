# Youtube XML Chapters File Extractor (from youtube description)

## Requirements

- Python3
- MKVToolNix

## Usage

1. Create an empty text file
2. Copy chapters from youtube description and past them into the text file (make sure that no empty lines exists between lines and that all lines have the same format)
3. Run the script file using this command `python script.py` then open the text file from the dialog
4. Open MKVToolNix
    1. Drag and drop the video file
    2. Navigate to the output tab
        1. Under **chapter file** option choose the newly created **chapters.xml** file
    3. Start multiplexing