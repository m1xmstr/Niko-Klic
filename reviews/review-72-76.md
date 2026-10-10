# Can Python Pack Our Badge Kit? | Nico & Klic Review 72–76

Natively scheduled for 2026-10-11T13:00:00-05:00 (America/Chicago). Public playback and manual captions will be checked after release.

Practice five Python ideas, then combine them in **our pretend badge packing desk**. All labels, equipment and decisions are fictional.

## Prerequisites

Complete lessons 72, 73, 74, 75, 76. Know Python strings, Boolean values, lists, indentation, function definitions and calls, and `print`. Ask a grown-up to help you use a local Python 3 editor. Never enter real private information.

## Individual lessons

- [Lesson 72](../episodes/72.md)
- [Lesson 73](../episodes/73.md)
- [Lesson 74](../episodes/74.md)
- [Lesson 75](../episodes/75.md)
- [Lesson 76](../episodes/76.md)

## Lesson 72: Repeat while True

Update the counter so this loop can stop

```python
remaining = 3
while remaining > 0:
    print(remaining)
    remaining = remaining - 1
```

Expected terminal output:

```text
3
2
1
```

Change one input and run the complete example again:

```python
remaining = 2
while remaining > 0:
    print(remaining)
    remaining = remaining - 1
```

Expected terminal output:

```text
2
1
```

## Lesson 73: Stop the loop: break

Print before break includes the matching item

```python
labels = ['red', 'blue', 'gold']
for label in labels:
    print(label)
    if label == 'blue':
        break
```

Expected terminal output:

```text
red
blue
```

Change one input and run the complete example again:

```python
labels = ['red', 'blue', 'gold']
for label in labels:
    print(label)
    if label == 'red':
        break
```

Expected terminal output:

```text
red
```

## Lesson 74: Skip this turn: continue

Skip the empty string and keep searching

```python
names = ['Moon', '', 'Star']
for name in names:
    if name == '':
        continue
    print(name)
```

Expected terminal output:

```text
Moon
Star
```

Change one input and run the complete example again:

```python
names = ['Moon', 'Sun', 'Star']
for name in names:
    if name == '':
        continue
    print(name)
```

Expected terminal output:

```text
Moon
Sun
Star
```

## Lesson 75: Functions can call helpers

Return the helper result, then add one

```python
def wheels(pairs):
    return pairs * 2
def with_spare(pairs):
    return wheels(pairs) + 1
print(with_spare(2))
```

Expected terminal output:

```text
5
```

Change one input and run the complete example again:

```python
def wheels(pairs):
    return pairs * 2
def with_spare(pairs):
    return wheels(pairs) + 1
print(with_spare(3))
```

Expected terminal output:

```text
7
```

## Lesson 76: Use the math module: import

math.ceil rounds upward to a whole number

```python
import math
badges = 5
sleeves = math.ceil(badges / 2)
print(sleeves)
```

Expected terminal output:

```text
3
```

Change one input and run the complete example again:

```python
import math
badges = 7
sleeves = math.ceil(badges / 2)
print(sleeves)
```

Expected terminal output:

```text
4
```

## Complete project: Our pretend badge packing desk

Save the whole program below in one Python file. The video uses two source pages for readability; page two uses the definitions on page one. Predict every output line before running.

```python
import math
def sleeve_count(badges):
    return math.ceil(badges / 2)
def packing_count(badges):
    return sleeve_count(badges)
names = ['Moon', '', 'Star', 'Stop']
for name in names:
    if name == 'Stop': break
    if name == '': continue
    print(name)
count = packing_count(5)
while count > 0:
    print(count)
    count -= 1
```

Expected terminal output:

```text
Moon
Star
3
2
1
```

Change one input and rerun this complete version:

```python
import math
def sleeve_count(badges):
    return math.ceil(badges / 2)
def packing_count(badges):
    return sleeve_count(badges)
names = ['Moon', '', 'Star', 'Stop']
for name in names:
    if name == 'Stop': break
    if name == '': continue
    print(name)
count = packing_count(7)
while count > 0:
    print(count)
    count -= 1
```

Expected terminal output:

```text
Moon
Star
4
3
2
1
```

## Try it with a grown-up

- In the original program, set `names = ['Moon', 'Stop', 'Star']`. Predict `Moon`, then `3`, `2`, `1`; Star is never reached.
- Restore the original names and call `packing_count(6)`. Predict the same output as five badges: Moon, Star, 3, 2, 1.
- Trace the while counter on paper until its condition becomes False. Explain how break and continue differ.
- Tell a grown-up which lesson was your favorite and explain one result.

The code displays terminal text. It does not operate equipment, control access or make real safety decisions. Explore our individual Nico & Klic Shorts for each lesson.
