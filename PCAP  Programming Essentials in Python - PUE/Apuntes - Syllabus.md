# 0. Introduction
### 0.1. Programming – absolute basics
#### 0.1.1. How does a computer program work?
This course aims to show you what the Python language is and what it is used for. Let’s start from the absolute basics.

A program makes a computer usable. Without a program, a computer, even the most powerful one, is nothing more than an object. Similarly, without a player, a piano is nothing more than a wooden box.

Computers are able to perform very complex tasks, but this ability is not innate. A computer’s nature is quite different.

It can execute only extremely simple operations, e.g., a computer cannot evaluate the value of a complicated mathematical function by itself, although this isn’t beyond the realms of possibility in the near future.

Contemporary computers can only evaluate the results of very fundamental operations, like adding or dividing, but they can do it very fast, and can repeat these actions virtually any number of times.

Imagine that you want to know the average speed you’ve reached during a long journey. You know the distance, you know the time, you need the speed.

Naturally, the computer will be able to compute this, but the computer is not aware of such things as distance, speed or time.

Therefore, it is necessary to instruct the computer to:
* accept a number representing the distance;
* accept a number representing the travel time;
* divide the former value by the latter and store the result in the memory;
* display the result (representing the average speed) in a readable format.

These four simple actions form a program. Of course, these examples are not formalized, and they are very far from what the computer can understand, but they are good enough to be translated into a language the computer can accept.

Language is the keyword.


#### 0.1.2. Natural languages vs. programming languages
A language is a means (and a tool) for expressing and recording thoughts.There are many languages all around us. Some of them require neither speaking nor writing, such as body language; it’s possible to express your deepest feelings very precisely without saying a word.

Another language you use each day is your mother tongue, which you use to manifest your will and to think about reality. Computers have their own language, too, called machine language, which is very rudimentary.

A computer, even the most technically sophisticated, is devoid of even a trace of intelligence. You could say that it is like a well-trained dog – it responds only to a predetermined set of known commands.

The commands it recognizes are very simple. We can imagine that the computer responds to orders like “take that number, divide by another and save the result”.

A complete set of known commands is called an instruction list, sometimes abbreviated to IL. Different types of computers may vary depending on the size of their ILs, and the instructions could be completely different in different models.

Note: machine languages are developed by humans.

No computer is currently capable of creating a new language. However, that may change soon.

On the other hand, people use a number of very different languages, too, but these languages created themselves. Moreover, they are still evolving.

New words are created every day and old words disappear. These languages are called natural languages.

What makes a language?

We can say that each language (machine or natural, it doesn’t matter) consists of the following elements:
* an alphabet: a set of symbols used to build words of a certain language (e.g., the Latin alphabet for English, the Cyrillic alphabet for Russian, Kanji for Japanese, and so on)

* a lexis aka a dictionary: a set of words the language offers its users (e.g., the word “computer” comes from the English language dictionary, while “cmoptrue” doesn’t; the word “chat” is present both in English and French dictionaries, but their meanings are different)

* a syntax: a set of rules (formal or informal, written or felt intuitively) used to determine if a certain string of words forms a valid sentence (e.g., “I am a python” is a syntactically correct phrase, while “I a python am” isn’t)

* semantics: a set of rules determining if a certain phrase makes sense (e.g., “I ate a doughnut” makes sense, but “A doughnut ate me” doesn’t)

The IL is, in fact, the alphabet of a machine language. This is the simplest and most primary set of symbols we can use to give commands to a computer. It’s the computer’s mother tongue.

Unfortunately, this tongue is a far cry from a human mother tongue. We all (both computers and humans) need something else, a common language for computers and humans, or a bridge between the two different worlds.

We need a language in which humans can write their programs and a language that computers may use to execute the programs, one that is far more complex than machine language and yet far simpler than natural language.

Such languages are often called high-level programming languages. They are at least somewhat similar to natural ones in that they use symbols, words and conventions readable to humans. These languages enable humans to express commands to computers that are much more complex than those offered by ILs.

A program written in a high-level programming language is called a source code (in contrast to the machine code executed by computers).

Similarly, the file containing the source code is called the source file.


#### 0.1.3. Compilations vs. interpretation
Computer programming is the act of composing the selected programming language’s elements in the order that will cause the desired effect. The effect could be different in every specific case – it’s up to the programmer’s imagination, knowledge and experience.

Of course, such a composition has to be correct in many senses:
* alphabetically – a program needs to be written in a recognizable script, such as Roman, Cyrillic, etc.
* lexically – each programming language has its dictionary and you need to master it; thankfully, it’s much simpler and smaller than the dictionary of any natural language;
* syntactically – each language has its rules and they must be obeyed;
* semantically – the program has to make sense.

Unfortunately, a programmer can also make mistakes with each of the above four senses. Each of them can cause the program to become completely useless.

Let’s assume that you’ve successfully written a program. How do we persuade the computer to execute it? You have to render your program into machine language.

Luckily, the translation can be done by a computer itself, making the whole process fast and efficient.

There are two different ways of transforming a program from a high-level programming language into machine language:
* compilation – the source program is translated once (however, this act must be repeated each time you modify the source code) by getting a file (e.g., an .exe file if the code is intended to be run under MS Windows) containing the machine code; now you can distribute the file worldwide; the program that performs this translation is called a compiler or translator;
* interpretation – you (or any user of the code) can translate the source program each time it has to be run; the program performing this kind of transformation is called an interpreter, as it interprets the code every time it is intended to be executed; it also means that you cannot just distribute the source code as-is, because the end-user also needs the interpreter to execute it.

Due to some very fundamental reasons, a particular high-level programming language is designed to fall into one of these two categories.

There are very few languages that can be both compiled and interpreted. Usually, a programming language is projected with this factor in its constructors’ minds – will it be compiled or interpreted?


### 0.2. Python – a tool, not a reptile
#### 0.2.1. What is Python?
#### 0.2.2. Who is Python's creator?
#### 0.2.4. Why Python?
#### 0.2.5. Why not Python?

### 0.3. There is more than one Python
#### 0.3.1. Python 2 vs. Python 3
#### 0.3.2. Python aka Cpython
#### 0.3.3. Cython
#### 0.3.4. Jython
#### 0.3.5. PyPy and Rpython

### 0.4. Begin your Python journey
#### 0.4.1. How to get Python and how to get to use it
#### 0.4.4. How to write and run your very first Python program
#### 0.4.8. How to spoil and fix your code

### 0.5. Edube Sandbox and Labs


#PART 1: BASICS
## 1. Basics I
### 1.1 Your first program
#### 1.1.1 Your first program
#### 1.1.2 The print() function – how the computer talks to you
#### 1.1.9 The print() function – formatting the output

### 1.2 Python literals
#### 1.2.1 Literals – what they are anyway?
#### 1.2.2 Literals – integers
#### 1.2.8 Literals – floats
#### 1.2.15 Literals – strings
#### 1.2.22 Literals – Boolean values

### 1.3 Operators – data manipulation tools
#### 1.3.1 Operators and expressions
#### 1.3.2 Arithmetic operators
#### 1.3.24 Operators and their priorities
#### 1.3.25 Operators and their bindings

### 1.4 Variables – data-shaped boxes
#### 1.4.1 Variables – how to name them
#### 1.4.2 Variable names vs. Python keywords
#### 1.4.3 How to assign a variable
#### 1.4.10 How to comment your code
#### 1.4.11 Shortcut operators

### 1.5 How to talk to computer?
#### 1.5.1 Output vs. input
#### 1.5.2 How to input data with the input() function
#### 1.5.6 How to convert strings into numbers
#### 1.5.7 Some simple interactive programs
#### 1.5.7 String operators
#### 1.5.16 How to convert numbers into strings

## 2. Basics II
### 2.1 Making decisions in Python
#### 2.1.1 How to ask questions and how to get answers
#### 2.1.2 Relational operators
#### 2.1.11 Making use of the answers
#### 2.1.13 Conditions and conditional execution – the if statements
#### 2.1.16 How indentation makes the code
#### 2.1.17 The more conditional execution – if-else statements
#### 2.1.21 The elif clause
#### 2.1.22 Some simple examples

### 2.2 Python's loops
#### 2.2.1 Looping your code with while
#### 2.2.12 Looping your code with for
#### 2.2.24 Controlling your loops with break and continue

### 2.3 Logic and bit operations in Python
#### 2.3.1 Computer logic and its operators
#### 2.3.8 Logical values vs. single bits
#### 2.3.9 Bitwise operators
#### 2.3.15 How to deal with single bits

### 2.4 Lists – collections of data
#### 2.4.1 Lists – why do we need them so much?
#### 2.4.2 How to create a list
#### 2.4.3 How to use a list
#### 2.4.8 Removing elements from a list
#### 2.4.9 How not to use a list
#### 2.4.12 List methods – methods vs. functions
#### 2.4.14 Adding elements to lists
#### 2.4.22 Making use of lists
#### 2.4.23 The second face of the for loop
#### 2.3.24 Lists in action

### 2.5 Sorting simple lists – the bubble sort algorithm

### 2.6 Lists – some more details
#### 2.6.1. How lists are stored
#### 2.6.2. Slices – the powerful tools
#### 2.6.14. The in and not in operators

### 2.7 Lists in advanced applications
#### 2.7.1 Lists in lists
#### 2.7.2 The list comprehension: why and how
#### 2.7.3 Lists in lists – matrices
#### 2.7.10 Lists in lists – 3rd dimension

## 3. Basics III
3.1 Writing functions in Python
3.1.1 Functions: why do we need them?
3.1.5 Where do functions come from?
3.1.6 Your first function

3.2 How functions communicate with their environment
3.2.1 Parametrized functions
3.2.2 How to define and use function parameters
3.2.6 What is shadowing?
3.2.7 Positional arguments
3.2.12 Keyword arguments
3.2.14 Mixed arguments
3.2.19 Setting parameters' default values

3.3 Returning a result from a function
3.3.1 A function's effects and results – the return statement
3.3.4 Returning a value
3.3.8 The None value
3.3.9 Returning the non-None value
3.3.11 Argument vs. parameter compatibility
3.3.12 A list as a function's result

3.4 Scopes in Python
3.4.1 Functions and scopes
3.4.2 How do scopes work?
3.4.5 How to make a variable global
3.4.6 How the parameters interact with their arguments

3.5 Creating functions
3.5.1 Some exercises with designing and writing functions
3.5.22 Recursion – how to make a function more powerful?

3.6 Tuples and dictionaries
3.6.1 Sequence types and mutability
3.6.2 What is a tuple?
3.6.3 How to create a tuple
3.6.5 How to use a tuple
3.6.11 What is a dictionary?
3.6.12 How to make a dictionary
3.6.13 How to use a dictionary
3.6.21 How a dictionary and a tuple can work together


PART 2: INTERMEDIATE

4. Intermediate I
4.1 Using modules
4.1 Using modules
4.1.1 What is a module?
4.1.2 How to make use of a module?
4.1.4 Importing a module

4.2. Some useful modules
4.2.1 Working with standard modules
4.2.4 Some functions from the math module
4.2.9 Some functions from the random module
4.2.15 Some functions from the platform module

4.3 What is a package?
4.3.1 Modules and packages
4.3.2 Your first module
4.3.14 Your first package

4.4 Errors – a programmer's daily bread
4.4.1 Errors, failures, and other plagues
4.4.2 Exceptions

4.5 The anatomy of an exception

4.6 Some of the most useful exceptions

4.7 Characters and strings vs. computers

4.8 The nature of Python's strings

4.9 String methods

4.10 Strings in action
4.10.1 Comparing strings
4.10.7 Sorting strings, and not only strings
4.10.10 Strings vs. numbers

4.11 Four simple programs
4.11.1 Caesar’s cipher – the coder
4.11.2 Caesar’s cipher – the decoder
4.11.3 Extracting numbers from a line of text
4.11.4 Checking the IBAN

5. Intermediate II
5.1 Basic concepts of object programming
5.1.1 What is an object?
5.1.5 The object – what is it again?
5.1.7 What does an object have?
5.1.8 Your first class

5.2 A short journey from the procedural to the object approach
5.2.1 What is a stack?
5.2.2 The stack – a procedural approach
5.2.7 The stack from scratch

5.3 Properties
5.3.1 Properties in detail
5.3.2 Instance variables
5.3.4 Class variables
5.3.8 Checking an attribute's existence

5.4 Methods
5.4.1 Methods in detail
5.4.a The inner life of classes and objects
5.4.b Reflection and introspection – two names of the same phenomenon
5.4.c Investigating classes – what can we find out about them?

5.5 Inheritance – one of object programming foundations
5.5.1 Inheritance – why and how
5.5.a How Python finds properties and methods
5.5.b How to build a hierarchy of classes
5.5.c Inheritance vs. composition
5.5.d Single inheritance vs. multiple inheritance
5.5.e Diamonds and why you don't want them

5.6 Exceptions once again
5.6.1 Exceptions are classes
5.6.a Detailed anatomy of an exception
5.6.b How to create your own exception
5.6.c How to use your own exception

5.7 Generators and closures
5.7.1 Generators – where to find them
5.7.a The yield statement
5.7.b How to build your own generator
5.7.c More about list comprehensions
5.7.d The lambda function
5.7.e How and when to use lambdas

5.8 Processing files
5.8.1 Accessing files from Python code
5.8.2 File names
5.8.6 File streams
5.8.9 File handles
5.8.13 Opening the streams
5.8.18 Selecting text and binary modes
5.8.19 Opening the stream for the first time
5.8.20 Pre-opened streams
5.8.24 Closing streams
5.8.26 Diagnosing stream problems

5.9 Working with real files
5.9.1 Dealing with text files
5.9.6 How to work with binary files
5.9.7 How to read bytes from the stream
5.9.a How to write bytes from the stream
5.9.b Copying files – a simple, but functional tool
