# Can Python Get Our Workshop Ready? | Nico & Klic Review 67–71

Natively scheduled for 2026-10-11T12:00:00-05:00 (America/Chicago). Public playback and manual captions will be checked after release.

Practice five Python ideas, then combine them in **our pretend repair desk**. All labels, equipment and decisions are fictional.

## Prerequisites

Complete lessons 67, 68, 69, 70, 71. Know Python strings, Boolean values, lists, indentation, function definitions and calls, and `print`. Ask a grown-up to help you use a local Python 3 editor. Never enter real private information.

## Individual lessons

- [Lesson 67](../episodes/67.md)
- [Lesson 68](../episodes/68.md)
- [Lesson 69](../episodes/69.md)
- [Lesson 70](../episodes/70.md)
- [Lesson 71](../episodes/71.md)

## Lesson 67: Check the collection: in

Membership checks the values in this list

```python
tools = ['sponge', 'cloth']
print('brush' in tools)
```

Expected terminal output:

```text
False
```

Change one input and run the complete example again:

```python
tools = ['sponge', 'cloth', 'brush']
print('brush' in tools)
```

Expected terminal output:

```text
True
```

## Lesson 68: Choose a fallback: get

Missing key uses fallback; existing key keeps its value

```python
settings = {}
print(settings.get('color', 'white'))
```

Expected terminal output:

```text
white
```

Change one input and run the complete example again:

```python
settings = {'color': 'blue'}
print(settings.get('color', 'white'))
```

Expected terminal output:

```text
blue
```

## Lesson 69: Reverse a Boolean: not

not changes True to False, and False to True

```python
raining = True
print(not raining)
```

Expected terminal output:

```text
False
```

Change one input and run the complete example again:

```python
raining = False
print(not raining)
```

Expected terminal output:

```text
True
```

## Lesson 70: Either works: or

or passes when either Boolean is True

```python
ticket = False
pass_card = True
print(ticket or pass_card)
```

Expected terminal output:

```text
True
```

Change one input and run the complete example again:

```python
ticket = False
pass_card = False
print(ticket or pass_card)
```

Expected terminal output:

```text
False
```

## Lesson 71: Explain the reason: comments

A # comment is source text; Python skips it

```python
# Use a made-up name.
nickname = 'StarBot'
print(nickname)
```

Expected terminal output:

```text
StarBot
```

Change one input and run the complete example again:

```python
# Use a made-up name.
nickname = 'MoonBot'
print(nickname)
```

Expected terminal output:

```text
MoonBot
```

## Complete project: Our pretend repair desk

Save the whole program below in one Python file. The video uses two source pages for readability; page two uses the definitions on page one. Predict every output line before running.

```python
def ready_for_repair(tools, resting):
    return 'brush' in tools and not resting
# Practice with pretend workshop settings.
tools = ['cloth', 'brush']
settings = {}
ticket = False
pass_card = True
print(settings.get('color', 'white'))
print(ticket or pass_card)
print(ready_for_repair(tools, False))
```

Expected terminal output:

```text
white
True
True
```

Change one input and rerun this complete version:

```python
def ready_for_repair(tools, resting):
    return 'brush' in tools and not resting
# Practice with pretend workshop settings.
tools = ['cloth']
settings = {}
ticket = False
pass_card = True
print(settings.get('color', 'white'))
print(ticket or pass_card)
print(ready_for_repair(tools, False))
```

Expected terminal output:

```text
white
True
False
```

## Try it with a grown-up

- Restore `tools = ['cloth', 'brush']` and change the last call to `ready_for_repair(tools, True)`. Predict `white`, `True`, `False`.
- Keep the original tools and call, but change settings to `{'color': 'blue'}`. Predict `blue`, `True`, `True`.
- Explain why the comment is skipped and why the missing color uses the fallback.
- Tell a grown-up which lesson was your favorite and explain one result.

The code displays terminal text. It does not operate equipment, control access or make real safety decisions. Explore our individual Nico & Klic Shorts for each lesson.
