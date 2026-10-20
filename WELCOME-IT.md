# Where Does Your Message Go? An Introduction to IT

[Watch the welcome video](https://www.youtube.com/watch?v=cE7i9PODDm8) — about 6 minutes 42 seconds.

Join Nico and Klic on a message adventure through computers, programming, networks and AI. This welcome lesson needs no prior coding experience. Watch with a grown-up, predict a result, then compare it with the experiment.

## The journey

- **Input:** information enters a computer through something like a keyboard, microphone, camera or touchscreen.
- **Processing:** instructions operate on that information.
- **Output:** a screen shows a result or speakers play sound. A touchscreen can provide both input and output.
- **Hardware and software:** physical components are hardware; programs and instructions are software.
- **Processor, memory and storage:** the processor carries out instructions, memory holds information in use, and storage keeps saved files. The work-table and cupboard comparison is a teaching model, not a picture of the real electronic components.
- **Networks and servers:** a client requests something and a server responds. A server can be a computer or a program. The internet connects networks, and cloud services use real computers.
- **Programming:** people write instructions. Predict, run, check, and change one thing to understand a program.
- **AI:** machine learning can learn patterns from examples. Predictions and fluent model-generated text can be wrong, so check useful sources and involve a trusted grown-up.

The traveling envelopes and physical props are illustrations. The experiments described below were actually executed; the code does not control the cartoon characters or props.

## Try the three-line program

With a grown-up and Python 3, save this as `letter.py` in a new practice folder:

```python
letter = input("Letter: ")
answer = letter.lower()
print(answer)
```

Run `python3 letter.py`. Enter uppercase `A` at the prompt. The next line displays lowercase `a`. Run it again and enter `B`; the output is `b`.

```text
Letter: A
a
```

Changed input:

```text
Letter: B
b
```

The typed input appears beside the prompt in an interactive terminal. Our automated run supplied the same input through standard input, so its captured output contained `Letter: a` and `Letter: b`. Both checks passed. Here `print()` displays terminal text; it does not print on paper or operate hardware.

## A saved message and a server

We wrote `Hello, Klic!` into a temporary message file, closed it, and read it with a fresh Python process. The saved text remained. We then ran a small server bound only to the local computer and requested `/message` from a client on that same computer.

| Test | Actual reply |
|---|---|
| First saved message | `Hello, Klic!` |
| Changed saved message, then another request | `Hello, Nico!` |

Both requests returned HTTP 200 with the expected text. The practice server was stopped and the temporary files were removed. This was a local demonstration, not a public website or a test of a remote service.

A grown-up can explain saving with a paper activity: put a message card in a labeled envelope, leave the table, return, and retrieve the card. Discuss how an unsaved change can disappear and why backups help.

## A model that makes a mistake

Our small nearest-average model used fictional number cards. These labels do not describe real objects or scientific categories.

| Training label | Numbers | Learned average |
|---|---|---|
| Pebble | 2, 3 | 2.5 |
| Comet | 7, 9 | 8.0 |

The model chose whichever average was closer to a new number. Its predictions were saved before the test answers were read.

| New test number | Prediction | Hidden answer | Result |
|---|---|---|---|
| 4 | Pebble | Comet | Does not match |
| 8 | Comet | Comet | Matches |

The training and test numbers were separate, and the model was unchanged between tests. One correct answer out of two toy examples is not evidence of reliable real-world accuracy. A large language model is a different kind of model that predicts pieces of text called tokens; fluent text still needs checking.

## Two activities without a computer

1. **Paper computer:** draw an input box, an instruction box and an output box. Choose the instruction “make the letter lowercase.” Send `A` through the boxes, then change it to `B`. Explain what stayed the same and what changed.
2. **Message station:** one person acts as a client and asks for a card. Another acts as a server and returns it. Change the saved card and make another request. No account, private information or internet connection is needed.

## Questions for a grown-up

- **Can one device provide input and output?** Yes. A touchscreen displays output and senses touch input.
- **Is the cloud made of clouds?** No. Cloud services run on real computers.
- **Does `print()` mean a paper printer?** In this program it displays text in the terminal.
- **Does one correct AI prediction prove the model is always right?** No. Test it and check the evidence.
- **What should we keep out of practice prompts?** Private information. Use fictional examples and ask a trusted grown-up for help.

## Keep exploring

Watch [Nico & Klic Shorts](https://www.youtube.com/@NicoAndKlic/shorts) for individual lessons in computers, coding, Linux, automation and AI. Browse the [curriculum](CURRICULUM.md) and [learning path](LEARNING-PATH.md). If you enjoyed learning with us, like the video and subscribe.
