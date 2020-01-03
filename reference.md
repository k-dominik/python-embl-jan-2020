---
layout: reference
permalink: /reference/
root: ..
---

## Reference

## [Running and Quitting]({{ page.root }}/01-run-quit/)
- Python files have the `.py` extension.
- Can be written in a text file or a [Jupyter Notebook][jupyter].
  - Jupyter notebooks have the extension `.ipynb`
  - Jupyter notebooks can be opened from [Anaconda](https://docs.continuum.io/anaconda/install) or through the command line by entering `$ jupyter notebook`
    - Markdown and HTML are allowed in markdown cells for documenting code.

## [Variables and Assignment]({{ page.root }}/02-variables/)
- Variables are stored using `=`.
  - Strings are defined in quotations `'...'`.
  - Integers and floating point numbers are defined without quotations.
- Variables can contain letters, digits, and underscores `_`.
  - Cannot start with a digit.
  - Variables that start with underscores should be avoided.
- Use `print(...)` to display values as text.
- Can use indexing on strings.
  - Indexing starts at 0.
  - Position is given in square brackets `[position]` following the variable name.
  - Take a slice using `[start:stop]`. This makes a copy of part of the original string.
    - `start` is the index of the first element.
    - `stop` is the index of the element after the last desired element.
- Use `len(...)` to find the length of a variable or string.

## [Data Types and Type Conversion]({{ page.root }}/03-types-conversion/)
- Each value has a type. This controls what can be done with it.
  - `int` represents an integer
  - `float` represents a floating point number.
  - `str` represents a string.
- To determine a variables type, use the built-in function `type(...)`, including the variable name in the parenthesis.
- Modifying strings:
  - Use `+` to concatenate strings.
  - Use `*` to repeat a string.
  - Numbers and strings cannot be added to on another.
    - Convert string to integer: `int(...)`.
    - Convert integer to string: `str(...)`.

## [Built-in Functions and Help]({{ page.root }}/04-built-in/)
- To add a comment, place `#` before the thing you do not with to be executed.
- Commonly used built-in functions:
  - `min()` finds the smallest value.
  - `max()` finds the largest value.
  - `round()` rounds off a floating point number.
  - `help()` displays documentation for the function in the parenthesis.
    - Other ways to get help include holding down `shift` and pressing `tab` in Jupyter Notebooks.

## [Libraries]({{ page.root }}/06-libraries/)
- Importing a library:
  - Use `import ...` to load a library.
  - Refer to this library by using `module_name.thing_name`.
    - `.` indicates 'part of'.
- To import a specific item from a library: `from ... import ...`
- To import a library using an alias: `import ... as ...`
- Importing the math library: `import math`
  - Example of referring to an item with the module's name: `math.cos(math.pi)`.
- Importing the plotting library as an alias: `import matplotlib as mpl`

## [Reading Tabular Data into DataFrames]({{ page.root }}/07-reading-tabular/)
- Use the pandas library to do statistics on tabular data. Load with `import pandas as pd`.
  - To read in a csv: `pd.read_csv()`, including the path name in the parenthesis.
    - To specify a column's values should be used as row headings: `pd.read_csv('path',index_col='column name')`, where path and column name should be replaced with the relevant values.
- To get more information about a DataFrame, use `DataFrame.info`, replacing `DataFrame` with the variable name of your DataFrame.
- Use `DataFrame.columns` to view the column names.
- Use `DataFrame.T` to transpose a DataFrame.
- Use `DataFrame.describe` to get summary statistics about your data.

## [Pandas DataFrames]({{ page.root }}/08-data-frames/)
- Select data using `[i,j]`
  - To select by entry position: `DataFrame.iloc[..., ...]`
    - This is inclusive of everything except the final index.
  - To select by entry label: `DataFrame.loc[..., ...]`
    - Can select multiple rows or columns by listing labels.
    - This is inclusive to both ends.
  - Use `:` to select all rows or columns.
- Can also select data based on values using `true` and `false`. This is a Boolean mask.
  - `mask = subset > 10000`
  - We can then use this to select values.
- To use a select-apply-combine operation we use `data.apply(lambda x: x>x.mean())` where `mean()` can be any operation the user would like to be applied to x.

## [Plotting]({{ page.root }}/09-plotting/)
- The most widely used plotting library is `matplotlib`.
  - Usually imported using `import matplotlib.pyplot as plt`.
  - To plot we use the command `plt.plot(time, position)`.
  - To create a legend use `plt.legend(['label1','label2', loc='upper left'])`
    - Can also define labels within the plot statements by using `plt.plot(time, position, label='label')`. To make the legend show up, use `plt.legend()`
  - To label x and y axis `plt.xlabel('label')` and `plt.ylabel('label')` are used.
- Pandas DataFrames can be used to plot by using `DataFrame.plot()`. Any operations that can be used on a DataFrame can be applied while plotting.
  - To plot a bar plot `data.plot(kind='bar')`

~~~
import matplotlib.puplot as plot
plt.plot(time,position,label='label')
plt.xlabel('x axis label')
plt.ylabel('y axis label')
plt.legend()
~~~
{: .language-python}

## [Lists]({{ page.root }}/11-lists/)
- Defined within `[...]` and separated by `,`.
  - An empty list can be created by using `[]`.
- Can use `len(...)` to determine how many values are in a list.
- Can index just as done in previous lessons.
  - Indexing can be used to reassign values `list_name[0] = newvalue`.
- To add an item to a list use `list_name.append()`, with the item to append in the parenthesis.
- To combine two lists use `list_name_1.extend(list_name_2)`.
- To remove an item from a list use `del list_name[index]`.

## [For Loops]({{ page.root }}/12-for-loops/)
- Start a for loop with `for number in [1,2,3]:`, with the following lines indented.
  - `[1, 2, 3]` is considered the collection.
  - `number` is the loop variable.
  - The action following the collection is the body.
- To iterate over a sequence of numbers use `range(start, end)`

~~~
for number in range(0,5):
  print(number)
~~~
{: .language-python}

## [Looping Over Data Sets]({{ page.root }}/13-looping-data-sets/)
- Use a for loop: `for filename in [file1, file2]:`
- To find a set of files using a pattern use `glob.glob`
  - Must import first using `import glob`.
  - `*` indicates "match zero or more characters"
  - `?` indicates "match exactly one character"
    - For example: `glob.glob(*.txt)` will find all files that end with .txt in the current directory.
- Combine these by writing a loop using: `for filename in glob.glob(*.txt):`

~~~
for filename in glob.glob(*.txt):
  data = pd.read_csv(filename)
~~~
{: .language-python}

## [Writing Functions]({{ page.root }}/14-writing-functions/)
- Define a function using `def function_name(parameters):`. Replace `parameters` with the variables to use when the function is executed.
- Run by using `function_name(parameters)`.
- To return a result to the caller use `return ...` in the function.

~~~
def add_numbers(a, b):
  result = a + b
  return result

add_numbers(1, 4)
~~~
{: .language-python}

## [Variable Scope]({{ page.root }}/15-scope/)
- A local variable is defined in a function and can only be seen and used within that function.
- A global variable is defined outside of a function and can be seen or used anywhere after definition.

## [Conditionals]({{ page.root }}/17-conditionals/)
- Defined similarly to a loop, using `if variable conditional value:`.
  - For example, `if variable > 5:`.
- Use `elif:` for additional tests.
- Use `else:` for when if statement is not true.
- Can Combine more than one conditional by using `and` or `or`.
- Often used in combination with for loops.
- Conditions that can be used:
  - `==` equal to.
  - `>=` greater than or equal to.
  - `<=` less than or equal to.
  - `>` greater than.
  - `<` less than.

~~~
for m in [3, 6, 7, 2, 8]:
  if m > 5:
    print(m, 'is large')
  elif m == 5:
    print(m, 'is 5')
  else:
    print(m, 'is small')
~~~
{: .language-python}

## [Programming Style]({{ page.root }}/18-style/)
- Document your code.
- Use clear and meaningful variable names.
- Follow [the PEP8 style guide](https://www.python.org/dev/peps/pep-0008) when setting up your code.
- Use assertions to check for internal errors.
- Use docstrings to provide help.

## Glossary

{:auto_ids}
Additive color model
:   A way to represent colors as the sum of contributions from primary colors
    such as [red, green, and blue](#rgb).

Argument
:   A value given to a function or program when it runs.
    The term is often used interchangeably (and inconsistently) with [parameter](#parameter).

Array
:   A container holding elements of the same type.

Assertion
:   An expression which is supposed to be true at a particular point in a program.
    Programmers typically put assertions in their code to check for errors;
    if the assertion fails (i.e., if the expression evaluates as false),
    the program halts and produces an error message.
    See also: [invariant](#invariant), [precondition](#precondition),
    [postcondition](#postcondition).

Assign
:   To give a value a name by associating a variable with it.

Body
:   (of a function): the statements that are executed when a function runs.

Boolean
:     An object composed of `true` and `false`.

Call stack
:   A data structure inside a running program that keeps track of active function calls.

Case-insensitive
:   Treating text as if upper and lower case characters of the same letter were the same.
    See also: [case-sensitive](#case-sensitive).

Case-sensitive
:   Treating text as if upper and lower case characters of the same letter are different.
    See also: [case-insensitive](#case-insensitive).

Comment
:   A remark in a program that is intended to help human readers understand what is going on,
    but is ignored by the computer.
    Comments in Python, R, and the Unix shell start with a `#` character and
    run to the end of the line;
    comments in SQL start with `--`,
    and other languages have other conventions.

Compose
:   To apply one function to the result of another, such as `f(g(x))`.

Conditional statement
:   A statement in a program that might or might not be executed
    depending on whether a test is true or false.

Comma-separated values
:   (CSV) A common textual representation for tables
    in which the values in each row are separated by commas.

DataFrame
:     The way Pandas represents a table; a collection of series.

Default value
:   A value to use for a [parameter](#parameter) if nothing is specified explicitly.

Defensive programming
:   The practice of writing programs that check their own operation
    to catch errors as early as possible.

Delimiter
:   A character or characters used to separate individual values,
    such as the commas between columns in a [CSV](#comma-separated-values) file.

Docstring
:   Short for "documentation string",
    this refers to textual documentation embedded in Python programs.
    Unlike comments, docstrings are preserved in the running program
    and can be examined in interactive sessions.

Documentation
:   Human-language text written to explain what software does,
    how it works, or how to use it.

Dotted notation
:   A two-part notation used in many programming languages
    in which `thing.component` refers to the `component` belonging to `thing`.

Element
:     An item in a list or an array. For a string, these are the individual characters.

Empty string
:   A character string containing no characters,
    often thought of as the "zero" of text.

Encapsulation
:   The practice of hiding something's implementation details
    so that the rest of a program can worry about *what* it does
    rather than *how* it does it.

Floating-point number
:   A number containing a fractional part and an exponent.
    See also: [integer](#integer).

For loop
:   A loop that is executed once for each value in some kind of set, list, or range.
    See also: [while loop](#while-loop).

Function
:     A block of code that can be called and re-used elsewhere. Occurrence of a function name in the code is a [function call](#function-call).
    Functions may process input [arguments](#argument) and return the result back. Functions
    may also be used for logically grouping together pieces of code. In such cases, they don't
    need to return any meaningful value and can be written without the
    [`return` statement](#return-statement) completely.
    Such functions return a special value `None`, which is a way of saying "nothing" in Python.

Function call
:   A use of a function in another piece of software.

Global variable
:     A variable defined outside of a function that can be used anywhere.

Immutable
:   Unchangeable.
    The value of immutable data cannot be altered after it has been created.
    See also: [mutable](#mutable).

Import
:   To load a [library](#library) into a program.

In-place operators
:   An operator such as `+=` that provides a shorthand notation for
    the common case in which the variable being assigned to
    is also an operand on the right hand side of the assignment.
    For example, the statement `x += 3` means the same thing as `x = x + 3`.

Index
:   A subscript that specifies the location of a single value in a collection,
    such as a single pixel in an image.

Inner loop
:   A loop that is inside another loop. See also: [outer loop](#outer-loop).

Integer
:   A whole number, such as -12343. See also: [floating-point number](#floating-point-number).

Invariant
:   An expression whose value doesn't change during the execution of a program,
    typically used in an [assertion](#assertion).
    See also: [precondition](#precondition), [postcondition](#postcondition).

Jupyter Notebook
:     Interactive coding environment allowing a combination of code and markdown.

Library
:     A collection of files containing functions used by other programs.

Local Variable
:     A variable defined inside of a function that can only be used inside of that function.

Loop Variable
:   The variable that keeps track of the progress of the loop.

Mask
:     A boolean object used for selecting data from another object.

Member
:   A variable contained within an [object](#object).

Method
:   A function which is tied to a particular [object](#object).
    Each of an object's methods typically implements one of the things it can do,
    or one of the questions it can answer.

Modules
:     The files within a library containing functions used by other programs.

Mutable
:   Changeable. The value of mutable data can be altered after it has been
    created. See [immutable](#immutable)."

Object
:   A collection of conceptually related variables ([members](#member)) and
    functions using those variables ([methods](#method)).

Outer loop
:   A loop that contains another loop.
    See also: [inner loop](#inner-loop).

Parameter
:   A variable named in the function's declaration that is used to
    hold a value passed into the call.
    The term is often used interchangeably (and inconsistently) with [argument](#argument).

Pipe
:   A connection from the output of one program to the input of another.
    When two or more programs are connected in this way, they are called a "pipeline".

Postcondition
:   A condition that a function (or other block of code) guarantees is true
    once it has finished running.
    Postconditions are often represented using [assertions](#assertion).

Precondition
:   A condition that must be true in order for a function (or other block of code)
    to run correctly.

Regression
:   To re-introduce a bug that was once fixed.

Return statement
:   A statement that causes a function to stop executing and return a value
    to its caller immediately.

RGB
:   An [additive model](#additive-color-model)
    that represents colors as combinations of red, green, and blue.
    Each color's value is typically in the range 0..255
    (i.e., a one-byte integer).

Sequence
:   A collection of information that is presented in a specific order.
    For example, in Python, a [string](#string) is a sequence of characters,
    while a list is a sequence of any variable.

Series
:     A Pandas data structure to represent a column.

Shape
:   An array's dimensions, represented as a vector.
    For example, a 5×3 array's shape is `(5,3)`.

Silent failure
:   Failing without producing any warning messages.
    Silent failures are hard to detect and debug.

Slice
:   A regular subsequence of a larger sequence,
    such as the first five elements or every second element.

Stack frame
:   A data structure that provides storage for a function's local variables.
    Each time a function is called, a new stack frame is created
    and put on the top of the [call stack](#call-stack). When the function returns,
    the stack frame is discarded.

Standard input
:   A process's default input stream.
    In interactive command-line applications,
    it is typically connected to the keyboard; in a [pipe](#pipe),
    it receives data from the [standard output](#standard-output) of the preceding process.

Standard output
:   A process's default output stream.
    In interactive command-line applications,
    data sent to standard output is displayed on the screen;
    in a [pipe](#pipe),
    it is passed to the [standard input](#standard-input) of the next process.

String
:   Short for "character string",
    a [sequence](#sequence) of zero or more characters.
    
Substring
:     A part of a [string](#string).

Syntax
:   The rules that define how code must be written for a computer to understand.

Syntax error
:   A programming error that occurs when statements are in an order
    or contain characters not expected by the programming language.


Test oracle
:   A program, device, data set, or human being
    against which the results of a test can be compared.

Test-driven development
:   The practice of writing unit tests *before* writing the code they test.

Traceback
:   The sequence of function calls that led to an error.

Tuple
:   An [immutable](#immutable) [sequence](#sequence) of values.

Type
:   The classification of something in a program
    (for example, the contents of a variable)
    as a kind of number (e.g. [floating-point](#float), [integer](#integer)),
    [string](#string), or something else.

Type of error
:   Indicates the nature of an error in a program. For example, in Python,
    an `IOError` to problems with file input/output.
    See also: [syntax error](#syntax-error).

Variable
:   A value that has a name associated with it.

While loop
:   A loop that keeps executing as long as some condition is true.
    See also: [for loop](#for-loop).
