import random
from tkinter import filedialog

def generate_xml_Chapter(chapterName, chapterStartTime):
    return f"""<ChapterAtom>
      <ChapterUID>{random.randint(0, 4294967295)}</ChapterUID>
      <ChapterTimeStart>{chapterStartTime}</ChapterTimeStart>
      <ChapterFlagHidden>0</ChapterFlagHidden>
      <ChapterFlagEnabled>1</ChapterFlagEnabled>
      <ChapterDisplay>
        <ChapterString>{chapterName}</ChapterString>
        <ChapterLanguage>eng</ChapterLanguage>
        <ChapLanguageIETF>en</ChapLanguageIETF>
      </ChapterDisplay>
    </ChapterAtom>"""


youtube_chapters = filedialog.askopenfilename()
SAVE_PATH = youtube_chapters[:youtube_chapters.rindex('/')]
chapters = ""
with open(f'{youtube_chapters}') as f:
    for line in f:
        spaceIndex = line.find(' ')
        chapterStartTime = line[:spaceIndex]
        chapterName = line[spaceIndex+1:]
        chapters += generate_xml_Chapter(chapterName, chapterStartTime)
    
    chapters = """<?xml version="1.0" encoding="UTF-8"?>
<!-- <!DOCTYPE Chapters SYSTEM "matroskachapters.dtd"> -->
<Chapters>
  <EditionEntry>""" + chapters + """</EditionEntry>
</Chapters>"""

with open(f'{SAVE_PATH}/chapters.xml', 'w') as f:
    f.write(chapters)