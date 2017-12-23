# HER, a new Text Format [![Build Status](https://travis-ci.org/hearot/HER.svg?branch=master)](https://travis-ci.org/hearot/HER)
<img src="https://hearot.it/assets/images/projects/Universe.jpg" width="700">

Search informations about the Syntax and Types using the [Wiki section](https://github.com/hearot/HER/wiki).

## Content table
  - [What's HER?](#whats-her)
  - [Why shall I use HER?](#why-shall-i-use-her)
  - [Why HER?](#why-her)
  - **Python Module**
    - [Installation](#installation)
    - [Import Module](#import-module)
    - [Encode a Dictionary](#encode-a-dictionary)
    - [Decode a String](#decode-a-string)
    - [Decode a File](#decode-a-file)
    - [Convert HER to JSON](#convert-her-to-json)
    - [Convert JSON to HER](#convert-json-to-her)

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

### Why HER?
__Because, however, if it isn't right, it's right.__

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
decoderObject = her.Decoder("- Category -\n    * hello world = True")
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
decoderObject = her.Decoder(open("file_path", "r"), True)
print(decoderObject.HER)
```

Output:
```
{'Category':{'hello world':True}}
```

## Convert JSON to HER
Just use the `Json2HER` class.
Call the `__init__` function assigning the object to a variable, then the `HER Document` will be available into the `self.HER` variable of the object.

```python
import her
json2HERObject = her.Json2HER("{\"Category\":{\"Cool\":true}}")
print(json2HERObject.HER)
```

Output:
```
- Category -
    * Cool = True
```

## Convert HER to JSON
Just use the `HER2Json` class.
Call the `__init__` function assigning the object to a variable, then the `JSON` will be available into the `self.JSON` variable of the object.

Remember: the second parameter **must** be `True` if the first parameter is `File` object.
```python
import her
HER2JsonObject = her.HER2Json("- Category -\n    * Cool = True")
print(HER2JsonObject.JSON)
```

Output:
```
{"Category":{"Cool":true}}
```
