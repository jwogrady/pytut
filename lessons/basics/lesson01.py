# Python Basics: Lesson 01

# The first thing you need to know is "#" denotes a `single line comment`.
"""
This is a `multi-line comment`.
The comment is everything between the triple quotes.
Regardless of format, comments are notes to future users that are ignored by the Python interpreter.
"""

# Python Facts
"""
- Python is a 'high-level language'. This means it is closer to human language than machine language.
- Python is an 'interpreted language'. That means it is not compiled before running. Instead, the Python interpreter reads the code line by line and executes it.
- Python is 'dynamically typed'. This means you do not have to declare the type of a variable when you create one.
- Python is 'object-oriented'. This means that Python treats everything as an object.
- Python is 'extensible'. This means you can write Python code in other languages like C++.
- Python is 'portable'. This means you can run Python on a wide variety of hardware platforms and has the same interface on all platforms.
- Python is 'open-source'. This means the Python source code is freely available and distributable.
- Python is a powerful, beginner-friendly programming language. This means it is easy to learn and use.
"""

# Why Python?
"""
- Python is a versatile language. It is used for web development, data analysis, artificial intelligence, scientific computing, and more.
- Python has a large community. This means you can find help and support easily.
- Python has a large standard library. This means you can find pre-written code for common tasks.
- Python has a large number of third-party libraries. This means you can find pre-written code for almost anything.
- Python just works.
"""

# How to execute Python code
"""
- Command Line: This is the simplest way to run Python code. You can type Python code directly into the interpreter and see the results
- Online Python interpreters: There are many online Python interpreters that allow you to write and run Python code in your browser.
- Jupyter Notebook: This is a web-based interactive computing notebook. It is a great way to write and run Python code.
- Create a file and run it: You can use a Python IDE (Integrated Development Environment). This is a program that provides a graphical user interface for writing and running Python code.

When you hear programmers use the term `environment`, it means the place and tools used to write and run code. On big projects, you may have multiple environments for different tasks.

For example, if you were using Python to create a website.
`Development` typically means the environment where the code is being written and tested.
`Staging` typically means the environment where content and media is loaded into the database and file system where it can be tested, reviewed, and approved.
`Production` is the `live` version of the site that is available to the public.

Every team has a different workflow, so the terms and steps may vary. The important thing remember right now is the `environment` is where your code lives, and the configuration used to run it.

"""

# Python Syntax

def example():
    print("Hello, World!")

"""The above code is a simple Python function that prints `Hello, World!`. You can type that directly into the Python interpreter and see the result. However, to save your work you will probably want to create a file and run it.
"""

example()

"""
I'm working in Visual Studio Code, so all I have to do is press the run button. Should you use Visual Studio Code? That's up to you. There are many Python IDEs to choose from. Some are free, some are not. Some are simple, some are complex. Some are for beginners, some are for experts. The important thing is to find one that works for you. But the best answer is, yes!
"""

# Python Indentation
"""
So many "professional" programmers will tell you that Python's use of indentation is a bad thing. I've never had a problem with it. In fact, I like clean, consistent, beautifully formatted code that is easy to read and understand across teams.

Yes, tabs are supported. Don't use tabs. Use spaces. The Python Style Guide (PEP 8) recommends using 4 spaces for indentation. Nerds use 2 spaces because they think different means smarter, faster and better. My suggestion is that if you are working on a team, use whatever the team uses. If you are working on a project, use whatever the project uses. If you are working on your own, use whatever you want. Just be consistent, and don't use tabs. You'll thank me later.
"""

# Python Variables
"""
Variables are used to store data. Python has no command for declaring a variable. A variable is created the moment you first assign a value to it. It's easy. Like this.
"""
y = 5 #integer
x = "Hello, World!" #string
z = 3.14 #float

# Remember, everything after the '#' is a comment. It's for the reader since the Python interpreter ignores it.

"""
The important concept here is you didn't have to declare anything. You typed it and the Python interpreter figured it out, like magic.
"""

# Python Standard Library
"""
Now is as good as any to talk about Python's Standard Library. All you need to know right now is that Python's standard library is huge. It litterally has hundreds, if not thousands, of commands ready to work for you. It's all documented in the help files, that I'm about to show you how to access quickly at your finger tips. But for now, just note this command is part of the standard library so I didn't have to install, declare, or even import anything to run it.
"""

print(type(x))
print(type(y))
print(type(z))

"""
Voila! If you run this file through your Python interpreter, you will see the first example, `Hello, World!`, and then the type of each variable. Both print and `type()` are built-in Python commands. The print command is used to display text on the screen. The `type()` command is used to determine the type of a variable. Astute readers will notice that `type()` is a function. It didn't just return a string value, it returned an entire class object. That's going to be important later, but for now, just know that Python is an object-oriented language, and everything it returns is actually an object. You want proof?
"""

print(type(x))
print(type(x).__base__)
print(type(x).__name__)

"""
The first example returns the object by default.
The second example returns the base class of the object.
The third example returns the name of the object which is string.

Don't get discouraged if you don't immediately grasp the significance of this. It's a lot to take in all at once. All you need to remember now is Python is an object-oriented language, and that every function returns an object that packs in all kinds of useful information.
"""

# Python Variables
"""
Variables are just containers for data. You could ask users to input and store it as a variable, but the most common way is to assign the variable to a value.

Remember these?
"""
y = 5
x = "Hello, World!"
z = 3.14

"""
Now you can do all kinds of fun tricks like this.
"""

print(y + z)


me = "John"
x = f"Hello, {me}"
print(x)

"""
Did you notice that we changed the value of `x`? The "f" tells the Python interpreter `x` is a formatted string. The `{me}` is a placeholder for the variable `me`. Then we just print(x) to return text to the screen.

This concludes Python Basics: Lesson 01. Most tutorials would cover variables, data types, and operators in the first lesson, but I find that stuff really boring because it is more like reading a reference manual than actually doing stuff. You'll learn that stuff better anyway by putting Python to work, so we'll head over to functions. Functions are the building blocks of Python, and you can't do anything without them. So, let's get started with Python Basics: Lesson 02.

"""