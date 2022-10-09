import random
def getChapter(chapterName, chapterStartTime):
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


chapters = ""
with open('chapters.txt') as f:
    for line in f:
        spaceIndex = line.find(' ')
        chapterStartTime = line[:spaceIndex]
        chapterName = line[spaceIndex+1:]
        chapters += getChapter(chapterName, chapterStartTime)
    
    chapters = """<?xml version="1.0" encoding="UTF-8"?>
<!-- <!DOCTYPE Chapters SYSTEM "matroskachapters.dtd"> -->
<Chapters>
  <EditionEntry>""" + chapters + """</EditionEntry>
</Chapters>"""
    with open('chapters.xml', 'w') as f2:
        f2.write(chapters)