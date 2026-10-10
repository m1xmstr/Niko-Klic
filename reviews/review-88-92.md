# Can Clear Python Code Plan Our Activity? | Nico & Klic Review 88–92

Video in preparation. This guide contains executed code, not a claim of publication.

Practice five Python ideas, then combine them in **our readable activity planner**. All labels, equipment and decisions are fictional.

## Prerequisites

Complete lessons 88, 89, 90, 91, 92. Know Python strings, Boolean values, lists, indentation, function definitions and calls, and `print`. Ask a grown-up to help you use a local Python 3 editor. Never enter real private information.

## Individual lessons

- [Lesson 88](../episodes/88.md)
- [Lesson 89](../episodes/89.md)
- [Lesson 90](../episodes/90.md)
- [Lesson 91](../episodes/91.md)
- [Lesson 92](../episodes/92.md)

## Lesson 88: Check an empty list

Check before asking for the first item

```python
tools = []
if tools:
    print(tools[0])
else:
    print('empty')
```

Expected terminal output:

```text
empty
```

Change one input and run the complete example again:

```python
tools = ['brush']
if tools:
    print(tools[0])
else:
    print('empty')
```

Expected terminal output:

```text
brush
```

## Lesson 89: Cap a count with min

The smaller argument becomes the allowed count

```python
requested = 7
capacity = 5
allowed = min(requested, capacity)
print(allowed)
```

Expected terminal output:

```text
5
```

Change one input and run the complete example again:

```python
requested = 3
capacity = 5
allowed = min(requested, capacity)
print(allowed)
```

Expected terminal output:

```text
3
```

## Lesson 90: Refactor repeated instructions

Keep the behavior for the same inputs

```python
def pair_count(boxes):
    return boxes * 2
print(pair_count(3))
print(pair_count(4))
```

Expected terminal output:

```text
6
8
```

Change one input and run the complete example again:

```python
def pair_count(boxes):
    return boxes * 2
print(pair_count(5))
print(pair_count(4))
```

Expected terminal output:

```text
10
8
```

## Lesson 91: Name values clearly

Meaningful names include the unit

```python
minutes_left = 9
break_minutes = 4
work_minutes = minutes_left - break_minutes
print(work_minutes)
```

Expected terminal output:

```text
5
```

Change one input and run the complete example again:

```python
minutes_left = 9
break_minutes = 2
work_minutes = minutes_left - break_minutes
print(work_minutes)
```

Expected terminal output:

```text
7
```

## Lesson 92: Name a combined condition

Calculate the condition again after changing inputs

```python
has_tool = True
clear_space = True
can_start = has_tool and clear_space
print(can_start)
```

Expected terminal output:

```text
True
```

Change one input and run the complete example again:

```python
has_tool = True
clear_space = False
can_start = has_tool and clear_space
print(can_start)
```

Expected terminal output:

```text
False
```

## Complete project: Our readable activity planner

Save the whole program below in one Python file. The video uses two source pages for readability; page two uses the definitions on page one. Predict every output line before running.

```python
def work_time(total, pause):
    return total - pause
tasks = ['draw']
requested = 7
capacity = 5
minutes_left = 9
break_minutes = 4
allowed = min(requested, capacity)
work_minutes = work_time(minutes_left, break_minutes)
can_start = tasks != [] and work_minutes > 0
print(can_start)
print(allowed)
print(work_minutes)
```

Expected terminal output:

```text
True
5
5
```

Change one input and rerun this complete version:

```python
def work_time(total, pause):
    return total - pause
tasks = []
requested = 7
capacity = 5
minutes_left = 9
break_minutes = 4
allowed = min(requested, capacity)
work_minutes = work_time(minutes_left, break_minutes)
can_start = tasks != [] and work_minutes > 0
print(can_start)
print(allowed)
print(work_minutes)
```

Expected terminal output:

```text
False
5
5
```

## Try it with a grown-up

- Restore tasks to `['draw']` and set `break_minutes = 9`. Predict `False`, `5`, `0`.
- Restore the four-minute break, then set `requested = 3`. Predict `True`, `3`, `5`.
- Explain why changing tasks does not change the count and time calculations. These are pretend values, not real safety checks.
- Tell a grown-up which lesson was your favorite and explain one result.

The code displays terminal text. It does not operate equipment, control access or make real safety decisions. Explore our individual Nico & Klic Shorts for each lesson.
