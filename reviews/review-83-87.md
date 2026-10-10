# Can We Trust This Python Answer? | Nico & Klic Review 83–87

Video in preparation. This guide contains executed code, not a claim of publication.

Practice five Python ideas, then combine them in **our tested packing planner**. All labels, equipment and decisions are fictional.

## Prerequisites

Complete lessons 83, 84, 85, 86, 87. Know Python strings, Boolean values, lists, indentation, function definitions and calls, and `print`. Ask a grown-up to help you use a local Python 3 editor. Never enter real private information.

## Individual lessons

- [Lesson 83](../episodes/83.md)
- [Lesson 84](../episodes/84.md)
- [Lesson 85](../episodes/85.md)
- [Lesson 86](../episodes/86.md)
- [Lesson 87](../episodes/87.md)

## Lesson 83: Debug a wrong answer

A successful run can still contain a logic error

```python
boxes = 3
slots = 2
print(boxes * slots)
```

Expected terminal output:

```text
6
```

Change one input and run the complete example again:

```python
boxes = 4
slots = 2
print(boxes * slots)
```

Expected terminal output:

```text
8
```

## Lesson 84: Trace changing values

Read the old value, calculate, then store the new value

```python
total = 2
total = total + 3
print(total)
```

Expected terminal output:

```text
5
```

Change one input and run the complete example again:

```python
total = 4
total = total + 3
print(total)
```

Expected terminal output:

```text
7
```

## Lesson 85: Test a function with assert

A passing example checks one case, not every possible input

```python
def double(n):
    return n * 2
assert double(3) == 6
print(double(4))
```

Expected terminal output:

```text
8
```

Change one input and run the complete example again:

```python
def double(n):
    return n * 2
assert double(3) == 6
print(double(5))
```

Expected terminal output:

```text
10
```

## Lesson 86: Use repeatable test data

A fixture supplies a known starting sample

```python
def label(data):
    return data.get('color', 'blue')
sample = {}
print(label(sample))
```

Expected terminal output:

```text
blue
```

Change one input and run the complete example again:

```python
def label(data):
    return data.get('color', 'blue')
sample = {'color': 'red'}
print(label(sample))
```

Expected terminal output:

```text
red
```

## Lesson 87: Check the boundary

Greater than or equal includes the threshold

```python
count = 5
if count >= 5:
    print('ready')
else:
    print('wait')
```

Expected terminal output:

```text
ready
```

Change one input and run the complete example again:

```python
count = 4
if count >= 5:
    print('ready')
else:
    print('wait')
```

Expected terminal output:

```text
wait
```

## Complete project: Our tested packing planner

Save the whole program below in one Python file. The video uses two source pages for readability; page two uses the definitions on page one. Predict every output line before running.

```python
def slots(data):
    boxes = data.get('boxes', 0)
    total = boxes * 2
    return total
assert slots({'boxes': 3}) == 6
sample = {'boxes': 3}
total = slots(sample)
if total >= 6:
    print('ready')
else:
    print('wait')
print(total)
```

Expected terminal output:

```text
ready
6
```

Change one input and rerun this complete version:

```python
def slots(data):
    boxes = data.get('boxes', 0)
    total = boxes * 2
    return total
assert slots({'boxes': 3}) == 6
sample = {'boxes': 2}
total = slots(sample)
if total >= 6:
    print('ready')
else:
    print('wait')
print(total)
```

Expected terminal output:

```text
wait
4
```

## Try it with a grown-up

- Set sample to `{'boxes': 0}`. Predict `wait`, then `0`.
- Restore three boxes, then replace multiplication with addition inside slots. The known assertion fails because three plus two is five, not six.
- Explain why checking two boxes alone misses that wrong operator: two plus two and two times two both equal four.
- Tell a grown-up which lesson was your favorite and explain one result.

The code displays terminal text. It does not operate equipment, control access or make real safety decisions. Explore our individual Nico & Klic Shorts for each lesson.
