# Can Five Python Ideas Plan Our Adventure? | Nico & Klic Review 62–66

[Watch the review](https://youtu.be/eCDvgX3h_Rw) — public with manual English captions.

Practice five Python ideas, then combine them in one explorer planner. All names, routes and equipment checks are fictional.

## Prerequisites

Complete lessons 62, 63, 64, 65, 66. Know Python strings, Boolean values, lists, indentation, function definitions and calls, and `print`. Ask a grown-up to help you use a local Python 3 editor. Never enter real private information.

## Individual lessons

- [Lesson 62](../episodes/62.md)
- [Lesson 63](../episodes/63.md)
- [Lesson 64](../episodes/64.md)
- [Lesson 65](../episodes/65.md)
- [Lesson 66](../episodes/66.md)

## Lesson 62: Both checks: and

```python
helmet = True
light = True
print(helmet and light)
```

Expected terminal output:

```text
True
```

Change one input and run the complete example again:

```python
helmet = True
light = False
print(helmet and light)
```

Expected terminal output:

```text
False
```

## Lesson 63: Another branch: elif

```python
color = 'yellow'
if color == 'green':
    print('GO')
elif color == 'yellow':
    print('SLOW')
else:
    print('WAIT')
```

Expected terminal output:

```text
SLOW
```

Change one input and run the complete example again:

```python
color = 'red'
if color == 'green':
    print('GO')
elif color == 'yellow':
    print('SLOW')
else:
    print('WAIT')
```

Expected terminal output:

```text
WAIT
```

## Lesson 64: Send a value back: return

```python
def add_one(number):
    return number + 1
answer = add_one(2)
print(answer)
```

Expected terminal output:

```text
3
```

Change one input and run the complete example again:

```python
def add_one(number):
    return number + 1
answer = add_one(4)
print(answer)
```

Expected terminal output:

```text
5
```

## Lesson 65: A new ordered list: sorted

```python
scores = [3, 1, 2]
print(sorted(scores))
print(scores)
```

Expected terminal output:

```text
[1, 2, 3]
[3, 1, 2]
```

Change one input and run the complete example again:

```python
scores = [4, 2, 1]
print(sorted(scores))
print(scores)
```

Expected terminal output:

```text
[1, 2, 4]
[4, 2, 1]
```

## Lesson 66: A fictional profile label

```python
profile = {'nickname': 'StarBot'}
print(profile['nickname'])
```

Expected terminal output:

```text
StarBot
```

Change one input and run the complete example again:

```python
profile = {'nickname': 'MoonBot'}
print(profile['nickname'])
```

Expected terminal output:

```text
MoonBot
```

## Complete explorer project

Save the whole program below in one Python file. The video uses two source pages for readability; page two uses the function defined on page one. Predict all three output lines before running.

```python
def choose_path(ready, tickets):
    if ready and tickets >= 3:
        return 'Trail'
    elif ready:
        return 'Garden'
    return 'Home'
profile = {'nickname': 'StarBot'}
weights = [3, 1, 2]
print(profile['nickname'])
print(sorted(weights))
print(choose_path(True, 3))
```

Expected terminal output:

```text
StarBot
[1, 2, 3]
Trail
```

Change only the last argument from `3` to `1` and rerun:

```python
def choose_path(ready, tickets):
    if ready and tickets >= 3:
        return 'Trail'
    elif ready:
        return 'Garden'
    return 'Home'
profile = {'nickname': 'StarBot'}
weights = [3, 1, 2]
print(profile['nickname'])
print(sorted(weights))
print(choose_path(True, 1))
```

Expected terminal output:

```text
StarBot
[1, 2, 3]
Garden
```

## Try it with a grown-up

- Change the call to `choose_path(False, 3)`. Predict `Home` on the final line; the other two output lines stay the same.
- Compare `choose_path(True, 2)` with `choose_path(True, 3)` to test the branch boundary.
- Explain why `sorted` leaves the original list unchanged, why `return` differs from `print`, and why `elif` only checks after the earlier branch fails.
- Tell a grown-up which lesson was your favorite. Use fictional labels; a nickname alone does not guarantee privacy.

The code displays terminal text. It does not control real traffic, move equipment, or make safety decisions. Explore our individual Nico & Klic Shorts for each lesson.
