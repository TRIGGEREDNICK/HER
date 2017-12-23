# HER, a new Text Format
<img src="https://hearot.it/assets/images/projects/Universe.jpg" width="700">

Search informations about the Syntax and Types using the [Wiki section](https://github.com/hearot/HER/wiki).

## Content table
  - [0. What's HER?](#what's-her?)
  - [1. Why shall I use HER?](#why-shall-i-use-her?)
  - [2. Why HER?](#why-her?)
  - **Python Module**
    - [Installation](#installation)
    - [Import Module](#import-module)
    - [Encode a Dictionary](#encode-a-dictionary)
    - [Decode a String](#decode-a-string)
    - [Decode a File](#decode-a-file)

## What's HER?
HER is text format, like XML/Json. The difference is that HER is easier than others.
Just see:
```
- Category -
    >> Array[]
    * Array[] = "Umh, that's pretty good!"
```

## Why shall I use HER?
As I said before, HER is **simple** and **easy to use**. You can pass informations, or better, store informations* and document them.

Feel the difference:

**XML:**
```XML
<category>Christmas
    <greetings>Merry christmas!</greetings>
    <greetings>Spam, Python, Eggs</greetings>
</category>
```

**HER:**
```
- Christmas -
    >> Greetings[]
    * Greetings[] = "Merry christmas!"
    * Greetings[] = "Spam, Python, Eggs"
```

### Why "HER"?
__Because, if it doesn't want to understant, however, it's right.__

* Like a document, you can read it clearly.

# Python Module

## Installation
You can easily install that module using PiP:
```bash
pip install her
```

Or, if you want to upgrade the module:
```bash
pip install --upgrade her
```

## Import Module
You must use `import her` to import all HER module.
```python
import her
encoderObject = her.Encoder({'Category':{'hello world':True}})
...
```

## Encode a Dictionary
Just use the `Encoder` class.
Call the `__init__` function assigning the object to a variable, then the `Encoded String` will be available into the `self.HER` variable of the object.
```python
import her
encoderObject = her.Encoder({'Category':{'hello world':True}})
print(encoderObject.HER)
```

Output:
```
- Category -
    * hello world = True
```

## Decode a String
Just use the `Decoder` class.
Call the `__init__` function assigning the object to a variable, then the `Decoded Dictionary` will be available into the `self.HER` variable of the object.
```python
import her
decoderObject = her.Decode("- Category -\n    * hello world = true")
print(decoderObject.HER)
```

Output:
```
{'Category':{'hello world':True}}
```

## Decode a File
Just use the `Decoder` class.
Call the `__init__` function assigning the object to a variable, then the `Decoded Dictionary` will be available into the `self.HER` variable of the object.

Remember: the second parameter **must** be `True` and the first parameter must be a `File` object.
```python
import her
decoderObject = her.Decode(open("file_path", "r"), True)
print(decoderObject.HER)
```

Output:
```
{'Category':{'hello world':True}}
```
