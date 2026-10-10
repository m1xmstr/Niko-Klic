# What Does This Address Really Tell Us? Python Network Basics | Nico & Klic Review 98–102

Video in preparation. This guide contains executed code, not a claim of publication.

Practice five Python ideas, then combine them in **our local address inspection card**. Examples use fictional practice values. File exercises create real disposable local files in the practice folder.

## Prerequisites

Complete lessons 98, 99, 100, 101, 102. Know Python strings, Boolean values, lists, indentation, function definitions and calls, and `print`. Ask a grown-up to help you use a local Python 3 editor. Never enter real private information.

## Individual lessons

- [Lesson 98](../episodes/98.md)
- [Lesson 99](../episodes/99.md)
- [Lesson 100](../episodes/100.md)
- [Lesson 101](../episodes/101.md)
- [Lesson 102](../episodes/102.md)

## Lesson 98: URL parts

Read a host and a path without opening a website

```python
from urllib.parse import urlsplit
link = "https://example.com/garden"
parts = urlsplit(link)
print(parts.hostname)
print(parts.path)
```

Expected terminal output:

```text
example.com
/garden
```

Change one input and run the complete example again:

```python
from urllib.parse import urlsplit
link = "https://example.com/pond"
parts = urlsplit(link)
print(parts.hostname)
print(parts.path)
```

Expected terminal output:

```text
example.com
/pond
```

## Lesson 99: Loopback address

Recognize an address that refers back to this device

```python
from ipaddress import ip_address
address = ip_address("127.0.0.1")
print(address.version)
print(address.is_loopback)
```

Expected terminal output:

```text
4
True
```

Change one input and run the complete example again:

```python
from ipaddress import ip_address
address = ip_address("192.0.2.8")
print(address.version)
print(address.is_loopback)
```

Expected terminal output:

```text
4
False
```

## Lesson 100: Explicit URL port

Read a number separately from the host

```python
from urllib.parse import urlsplit
link = "https://example.com:8000/map"
parts = urlsplit(link)
print(parts.hostname)
print(parts.port)
```

Expected terminal output:

```text
example.com
8000
```

Change one input and run the complete example again:

```python
from urllib.parse import urlsplit
link = "https://example.com:8080/map"
parts = urlsplit(link)
print(parts.hostname)
print(parts.port)
```

Expected terminal output:

```text
example.com
8080
```

## Lesson 101: URL scheme

A text comparison is not a safety verdict

```python
from urllib.parse import urlsplit
link = "https://example.com/map"
parts = urlsplit(link)
print(parts.scheme)
print(parts.scheme == "https")
```

Expected terminal output:

```text
https
True
```

Change one input and run the complete example again:

```python
from urllib.parse import urlsplit
link = "http://example.com/map"
parts = urlsplit(link)
print(parts.scheme)
print(parts.scheme == "https")
```

Expected terminal output:

```text
http
False
```

## Lesson 102: Field allowlist

Copy only the fields that were deliberately selected

```python
profile = {"nickname": "Star", "room": "Blue"}
allowed = ["nickname"]
public = {}
for key in allowed:
    public[key] = profile[key]
print(public)
```

Expected terminal output:

```text
{'nickname': 'Star'}
```

Change one input and run the complete example again:

```python
profile = {"nickname": "Moon", "room": "Blue"}
allowed = ["nickname"]
public = {}
for key in allowed:
    public[key] = profile[key]
print(public)
```

Expected terminal output:

```text
{'nickname': 'Moon'}
```

## Complete project: Our local address inspection card

Save the whole program below in one Python file. The video uses two source pages for readability; page two uses the definitions on page one. Predict every output line before running.

```python
from urllib.parse import urlsplit
from ipaddress import ip_address
link = "https://127.0.0.1:8000/map"
parts = urlsplit(link)
profile = {"nickname": "Star", "room": "Blue"}
allowed = ["nickname"]
public = {}
for key in allowed:
    public[key] = profile[key]
print(public["nickname"])
print(parts.hostname)
print(parts.path)
print(parts.port)
print(parts.scheme == "https")
print(ip_address(parts.hostname).is_loopback)
```

Expected terminal output:

```text
Star
127.0.0.1
/map
8000
True
True
```

Change one input and rerun this complete version:

```python
from urllib.parse import urlsplit
from ipaddress import ip_address
link = "https://127.0.0.1:8080/map"
parts = urlsplit(link)
profile = {"nickname": "Star", "room": "Blue"}
allowed = ["nickname"]
public = {}
for key in allowed:
    public[key] = profile[key]
print(public["nickname"])
print(parts.hostname)
print(parts.path)
print(parts.port)
print(parts.scheme == "https")
print(ip_address(parts.hostname).is_loopback)
```

Expected terminal output:

```text
Star
127.0.0.1
/map
8080
True
True
```

## Try it with a grown-up

- Change only `/map` to `/garden`. Predict the third line changes, while the port and both Boolean results stay the same.
- Change the fictional nickname from Star to Moon. Predict only the first output line changes.
- Explain why reading address text opens no connection and why the original profile still contains room. Never substitute private information.
- Tell a grown-up which lesson was your favorite and explain one result.

The code displays terminal text; file exercises also create, write, or copy local practice files. It does not operate equipment, control access or make real safety decisions. Explore our individual Nico & Klic Shorts for each lesson.
