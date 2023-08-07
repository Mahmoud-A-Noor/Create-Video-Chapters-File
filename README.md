# Youtube XML Chapters File Extractor (from youtube description)

## Requirements

- Python3
- MKVToolNix

## Usage

1. Create an empty text file
2. Copy chapters from the youtube description and past them into the text file (make sure that no empty lines exist between lines and that all lines have the same format)
    ![youtube chapters](https://user-images.githubusercontent.com/59361888/210526853-46e1014f-8a97-4785-9155-9f62be9219fb.PNG)
    ![youtube chapters formatted](https://user-images.githubusercontent.com/59361888/210526864-e4b21723-e2f1-454e-bc1f-7fae5bc85dd8.PNG)

3. Run the script file using this command `python script.py` then choose the text file from the dialog
    ![open youtube chapters file](https://user-images.githubusercontent.com/59361888/210527023-a8e494e2-dfc3-439c-af02-16ce479e9576.PNG)

4. Open MKVToolNix
    1. Drag and drop the video file
        ![drag video file](https://user-images.githubusercontent.com/59361888/210527112-fed3ef3f-cb67-4017-9082-6ffba0a6b71e.png)

    2. Navigate to the output tab
        1. Under **chapter file** option choose the newly created **chapters.xml** file
            ![add chapters xml](https://user-images.githubusercontent.com/59361888/210527174-3d82aed8-e99f-44eb-8850-41ac0d1c604c.png)

    3. Start multiplexing
    

![overview](https://user-images.githubusercontent.com/59361888/210527489-e645a81a-e1c0-4716-bfd3-19f477bf439b.png)
