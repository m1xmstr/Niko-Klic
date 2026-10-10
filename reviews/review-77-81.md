# Can Python Save Our Picnic Plan? | Nico & Klic Review 77–81

Natively scheduled for 2026-10-12T12:00:00-05:00 (America/Chicago). Public playback and manual captions will be checked after release.

Practice five Python ideas, then combine them in **our saved-note and sharing plan**. All labels, equipment and decisions are fictional.

## Prerequisites

Complete lessons 77, 78, 79, 80, 81. Know Python strings, Boolean values, lists, indentation, function definitions and calls, and `print`. Ask a grown-up to help you use a local Python 3 editor. Never enter real private information.

## Individual lessons

- [Lesson 77](../episodes/77.md)
- [Lesson 78](../episodes/78.md)
- [Lesson 79](../episodes/79.md)
- [Lesson 80](../episodes/80.md)
- [Lesson 81](../episodes/81.md)

## Lesson 77: Borrow a function: modules

Save helpers.py and main.py in the same practice folder
### Save as `helpers.py`

```python
def double(n):
    return n * 2
```

### Save as `main.py`

```python
from helpers import double
print(double(3))
```

Run `main.py` from this folder. Expected terminal output:

```text
6
```

Change one input and run the complete example again:
### Save as `helpers.py`

```python
def double(n):
    return n * 2
```

### Save as `main.py`

```python
from helpers import double
print(double(4))
```

Run `main.py` from this folder. Expected terminal output:

```text
8
```

## Lesson 78: Save text: file writing

w creates a file or replaces its contents

```python
with open('note.txt', 'w') as note:
    note.write('Moon')
with open('note.txt') as note:
    print(note.read())
```

Expected terminal output:

```text
Moon
```

Change one input and run the complete example again:

```python
with open('note.txt', 'w') as note:
    note.write('Star')
with open('note.txt') as note:
    print(note.read())
```

Expected terminal output:

```text
Star
```

## Lesson 79: Read a selected file

Prepare moon.txt and sun.txt before running main.py

Prepare these text files in the same new practice folder, with no trailing newline:

### `moon.txt`

```text
Moon
```

### `sun.txt`

```text
Sun
```

```python
filename = 'moon.txt'
with open(filename) as note:
    text = note.read()
print(text)
```

Expected terminal output:

```text
Moon
```

Change one input and run the complete example again:

```python
filename = 'sun.txt'
with open(filename) as note:
    text = note.read()
print(text)
```

Expected terminal output:

```text
Sun
```

## Lesson 80: Read an exception

ZeroDivisionError identifies a zero divisor

```python
boxes = 2
print(6 // boxes)
```

Expected terminal output:

```text
3
```

Change one input and run the complete example again:

```python
boxes = 3
print(6 // boxes)
```

Expected terminal output:

```text
2
```

## Lesson 81: Respond with try and except

Catch the named error; test the successful path too

```python
boxes = 0
try:
    print(6 // boxes)
except ZeroDivisionError:
    print('Add boxes')
```

Expected terminal output:

```text
Add boxes
```

Change one input and run the complete example again:

```python
boxes = 3
try:
    print(6 // boxes)
except ZeroDivisionError:
    print('Add boxes')
```

Expected terminal output:

```text
2
```

## Complete project: Our saved-note and sharing plan

Save both Python files below in the same new empty practice folder; the two video pages are separate files. Save and reopen both, then run main.py. This writes or replaces note.txt in the practice folder. Never use an important document. Predict every output line before running.
### Save as `helpers.py`

```python
def share(total, boxes):
    return total // boxes
```

### Save as `main.py`

```python
from helpers import share
with open('note.txt', 'w') as note:
    note.write('Moon')
with open('note.txt') as note:
    print(note.read())
try:
    print(share(6, 0))
except ZeroDivisionError:
    print('Add boxes')
```

Run `main.py` from this folder. Expected terminal output:

```text
Moon
Add boxes
```

Change one input and rerun this complete version:
### Save as `helpers.py`

```python
def share(total, boxes):
    return total // boxes
```

### Save as `main.py`

```python
from helpers import share
with open('note.txt', 'w') as note:
    note.write('Moon')
with open('note.txt') as note:
    print(note.read())
try:
    print(share(6, 3))
except ZeroDivisionError:
    print('Add boxes')
```

Run `main.py` from this folder. Expected terminal output:

```text
Moon
2
```

## Try it with a grown-up

- Restore the original files and change the call to `share(6, 2)`. Predict `Moon`, then `3`.
- Change the fictional saved word to `Star` and keep `share(6, 3)`. Predict `Star`, then `2`.
- Reopen `note.txt` after each run. Confirm the saved word and explain why handling a later error does not undo the earlier write.
- Tell a grown-up which lesson was your favorite and explain one result.

The code displays terminal text. It does not operate equipment, control access or make real safety decisions. Explore our individual Nico & Klic Shorts for each lesson.
