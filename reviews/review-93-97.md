# Where Did Our File Go? Python File Skills | Nico & Klic Review 93–97

Natively scheduled for 2026-10-15T12:00:00-05:00 (America/Chicago). Public playback and manual captions will be checked after release.

Practice five Python ideas, then combine them in **our practice-file organizer**. Examples use fictional practice values. File exercises create real disposable local files in the practice folder.

## Prerequisites

Complete lessons 93, 94, 95, 96, 97. Know Python strings, Boolean values, lists, indentation, function definitions and calls, and `print`. Ask a grown-up to help you use a local Python 3 editor. Never enter real private information.

## Individual lessons

- [Lesson 93](../episodes/93.md)
- [Lesson 94](../episodes/94.md)
- [Lesson 95](../episodes/95.md)
- [Lesson 96](../episodes/96.md)
- [Lesson 97](../episodes/97.md)

## Lesson 93: Read a Path

An address has a name and a parent

```python
from pathlib import Path
p = Path("practice/note.txt")
print(p.name)
print(p.parent)
```

Expected terminal output:

```text
note.txt
practice
```

Change one input and run the complete example again:

```python
from pathlib import Path
p = Path("practice/star.txt")
print(p.name)
print(p.parent)
```

Expected terminal output:

```text
star.txt
practice
```

## Lesson 94: Check exists

Check the exact address after saving

```python
from pathlib import Path
Path("note.txt").write_text("blue")
p = Path("note.txt")
print(p.exists())
```

Expected terminal output:

```text
True
```

Change one input and run the complete example again:

```python
from pathlib import Path
Path("note.txt").write_text("blue")
p = Path("missing.txt")
print(p.exists())
```

Expected terminal output:

```text
False
```

## Lesson 95: Read a suffix

A filename label does not prove its contents

```python
from pathlib import Path
p = Path("story.txt")
print(p.suffix)
print(p.suffix == ".txt")
```

Expected terminal output:

```text
.txt
True
```

Change one input and run the complete example again:

```python
from pathlib import Path
p = Path("story.png")
print(p.suffix)
print(p.suffix == ".txt")
```

Expected terminal output:

```text
.png
False
```

## Lesson 96: Create a directory

Make a folder and check its location

```python
from pathlib import Path
folder = Path("practice")
folder.mkdir(exist_ok=True)
print(folder.name)
print(folder.is_dir())
```

Expected terminal output:

```text
practice
True
```

Change one input and run the complete example again:

```python
from pathlib import Path
folder = Path("sketches")
folder.mkdir(exist_ok=True)
print(folder.name)
print(folder.is_dir())
```

Expected terminal output:

```text
sketches
True
```

## Lesson 97: Copy a saved file

Keep the source and reopen the destination

```python
from pathlib import Path
from shutil import copyfile
Path("note.txt").write_text("blue")
copyfile("note.txt", "copy.txt")
print(Path("copy.txt").read_text())
```

Expected terminal output:

```text
blue
```

Change one input and run the complete example again:

```python
from pathlib import Path
from shutil import copyfile
Path("note.txt").write_text("green")
copyfile("note.txt", "copy.txt")
print(Path("copy.txt").read_text())
```

Expected terminal output:

```text
green
```

## Complete project: Our practice-file organizer

Save the whole program below in one Python file. The video uses two source pages for readability; page two uses the definitions on page one. Predict every output line before running.

```python
from pathlib import Path
from shutil import copyfile
folder = Path("practice")
folder.mkdir(exist_ok=True)
source = folder / "note.txt"
source.write_text("blue")
dest = folder / "copy.txt"
copyfile(source, dest)
print(dest.name)
print(dest.parent)
print(dest.exists())
print(dest.suffix)
print(dest.read_text())
```

Expected terminal output:

```text
copy.txt
practice
True
.txt
blue
```

Change one input and rerun this complete version:

```python
from pathlib import Path
from shutil import copyfile
folder = Path("practice")
folder.mkdir(exist_ok=True)
source = folder / "note.txt"
source.write_text("green")
dest = folder / "copy.txt"
copyfile(source, dest)
print(dest.name)
print(dest.parent)
print(dest.exists())
print(dest.suffix)
print(dest.read_text())
```

Expected terminal output:

```text
copy.txt
practice
True
.txt
green
```

## Try it with a grown-up

- Use a new empty practice folder with a grown-up. Writing and copying replace existing destination contents; keep important files elsewhere.
- Keep green and change the destination from `copy.txt` to `second.txt`. Predict `second.txt`, `practice`, `True`, `.txt`, then `green`.
- Reopen both `practice/note.txt` and `practice/second.txt`; each must contain green. Explain why matching names alone would not prove matching contents.
- Tell a grown-up which lesson was your favorite and explain one result.

The code displays terminal text; file exercises also create, write, or copy local practice files. It does not operate equipment, control access or make real safety decisions. Explore our individual Nico & Klic Shorts for each lesson.
