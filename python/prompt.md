# 🐍 CURSOR PROMPT: EPAM Junior AI Python Developer — Python Core Preparation Notebooks

## ⚠️ IMPORTANT CONTEXT

I have applied for the **Junior AI Python Developer** position at EPAM. I have a Python Core assessment test — **65 questions, 19 minutes**. The questions will be in **multiple choice** format. I need **complete, comprehensive, detailed Jupyter Notebook (.ipynb)** files to learn and practice all Python Core topics.

---

## 📋 WHAT I WANT

Create a **separate .ipynb file for each section** below. Each notebook should follow this structure:

### Structure of Each Notebook:

1. **📖 Theory** — Fully explain the topic. Add short comments in English. Demonstrate every concept with a **code example**. Don't just write text — show everything with real code in `code cells`.

2. **🔬 Deep Dive** — The "trick" and "gotcha" parts of each topic. Areas where people commonly make mistakes. Examples for "trap" questions that could appear on the EPAM test.

3. **🧪 Interactive Examples** — Examples that show results with `print()`, modify-and-observe type examples. Before each example, there should be a "What will this code print?" question (as a comment), with the answer below.

4. **📝 Quiz Section** — At the end of each notebook, there should be **at least 20-25 multiple choice questions**. EPAM style — short, tricky, attention-demanding questions. Format should be:

```python
# ❓ Question 1: What is the output of the following code?
# 
# x = [1, 2, 3]
# y = x
# y.append(4)
# print(x)
#
# A) [1, 2, 3]
# B) [1, 2, 3, 4]
# C) Error
# D) None
#
# 🤔 Write your answer, then run the cell below

# Answer (don't run this cell first!)
print("✅ Correct Answer: B) [1, 2, 3, 4]")
print("📖 Explanation: y = x creates a reference, not a copy. Both point to the same list object.")
```

5. **💻 Exercises** — **5-10 coding exercises** for each topic. First provide an empty function/code, with `assert` tests below. Then show the solution in a separate cell.

```python
# Exercise 1: Write a function that returns the second largest number in a list
def second_largest(lst):
    # YOUR CODE HERE
    pass

# Tests (don't modify)
assert second_largest([1, 2, 3, 4, 5]) == 4
assert second_largest([10, 10, 9]) == 9
assert second_largest([1, 1, 1, 1]) == 1
print("✅ All tests passed!")
```

6. **⚡ Speed Round** — 10 questions, 17 seconds per question (EPAM test simulation). Even without a timer, questions should be very short to practice rapid answering.

---

## 📚 NOTEBOOKS (Each one is a separate .ipynb file)

### 📁 Notebook 01: `01_Data_Types_and_Variables.ipynb`

Topics to cover:
- All built-in data types: `int`, `float`, `complex`, `bool`, `str`, `bytes`, `bytearray`, `memoryview`, `NoneType`
- Type checking: `type()`, `isinstance()`, `issubclass()`
- Type conversion / casting: `int()`, `float()`, `str()`, `bool()`, `list()`, `tuple()`, `set()`, `dict()`, `complex()`
- Dynamic typing — how Python determines types
- **Mutable vs Immutable** (most important topic!):
  - Mutable: `list`, `dict`, `set`, `bytearray`
  - Immutable: `int`, `float`, `str`, `tuple`, `frozenset`, `bytes`, `bool`
  - Its effect on functions, aliasing problem
- Variable assignment — reference semantics
- Multiple assignment: `a, b, c = 1, 2, 3` and `a = b = c = 0`
- `id()` function — object identity
- Integer caching/interning: `-5` to `256` range
- String interning
- `sys.getsizeof()` for measuring memory
- `None` — NoneType, `is None` vs `== None`
- Boolean context of data types: Truthy vs Falsy values
  - Falsy: `0`, `0.0`, `""`, `[]`, `()`, `{}`, `set()`, `None`, `False`, `0j`
  - Truthy: everything else
- Numeric systems: `0b` (binary), `0o` (octal), `0x` (hex)
- `bin()`, `oct()`, `hex()` functions
- Underscore in numbers: `1_000_000`
- Float precision issues: `0.1 + 0.2 != 0.3` (classic question!)
- `decimal` module basics
- `math.isclose()` for float comparison

**Trap questions that should be in the quiz:**
- What is `bool("")`? What is `bool(" ")`? (string with space is truthy!)
- What is `type(True + True)`? (int, value is 2)
- What is `isinstance(True, int)`? (True! bool is a subclass of int)
- What is `[] is []`? (False — different objects)
- `a = 256; b = 256; a is b` vs `a = 257; b = 257; a is b`

---

### 📁 Notebook 02: `02_Operators.ipynb`

Topics to cover:
- **Arithmetic Operators**: `+`, `-`, `*`, `/`, `//` (floor division), `%` (modulo), `**` (power)
  - `/` vs `//` difference — `/` always returns float, `//` floors the result
  - `//` and `%` with negative numbers: `-7 // 2 = -4` (not -3!)
  - `divmod()` function
- **Comparison Operators**: `==`, `!=`, `>`, `<`, `>=`, `<=`
  - Chained comparisons: `1 < x < 10`, `a == b == c`
  - Float comparison trap: `0.1 + 0.2 == 0.3` → `False`
- **Logical Operators**: `and`, `or`, `not`
  - Short-circuit evaluation
  - `and` — returns first Falsy or last Truthy value
  - `or` — returns first Truthy or last Falsy value
  - `not` — always returns `True`/`False`
  - `0 or "" or [] or "hello" or 42` → `"hello"` (know this!)
  - `1 and 2 and 3` → `3`
  - `1 and 0 and 3` → `0`
- **Bitwise Operators**: `&`, `|`, `^`, `~`, `<<`, `>>`
  - Explain with real examples
  - `~x = -(x+1)` rule
- **Identity Operators**: `is`, `is not`
  - `is` vs `==` difference (most important question!)
  - `is` — compares id, `==` — compares value
  - Always use `is` with `None`
- **Membership Operators**: `in`, `not in`
  - Usage in list, tuple, set, dict, string
  - `in` for dict checks keys, not values!
- **Assignment Operators**: `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`, `&=`, `|=`, `^=`, `<<=`, `>>=`
  - `+=` difference with immutable vs mutable:
    - `x = (1,2); x += (3,)` — creates a new tuple
    - `x = [1,2]; x += [3]` — modifies the existing list (like extend)
- **Walrus Operator `:=`** (Python 3.8+)
  - `if (n := len(a)) > 10:` example
  - Usage in while loops
- **Operator Precedence** (priority order) — show full table
  - `()` > `**` > `~, +, -` (unary) > `*, /, //, %` > `+, -` > `<<, >>` > `&` > `^` > `|` > comparisons > `not` > `and` > `or`
  - Trap examples: `2 ** 3 ** 2` = `2 ** 9` = `512` (right-associative!)
  - `not 1 == 2` vs `(not 1) == 2`
- **Operator Overloading** — brief explanation of relation with dunder methods

**Quiz trap questions:**
- What is `-11 % 3`? (1, because Python modulo is consistent with floor division)
- `True + True + True`? (3)
- `"hello" * 3` vs `3 * "hello"` — both are the same
- What is `2 ** 3 ** 2`? (512 — right-to-left associativity)
- What is `not not not True`? (False)
- What is `[] and "hello"`? (`[]` — short-circuit)

---

### 📁 Notebook 03: `03_Strings.ipynb`

Topics to cover:
- String creation: single quotes, double quotes, triple quotes (multiline)
- Raw strings: `r"hello\nworld"` — ignores backslash
- **String Immutability** — `s[0] = "H"` → Error
- **Indexing & Slicing**: `s[0]`, `s[-1]`, `s[start:stop:step]`
  - Reverse string: `s[::-1]`
  - `s[::2]` — every second character
  - Out of range index → Error, but out of range slice → empty string
- **String Methods** (all must be memorized):
  - Case: `.upper()`, `.lower()`, `.title()`, `.capitalize()`, `.swapcase()`, `.casefold()`
  - Search: `.find()`, `.rfind()`, `.index()`, `.rindex()`, `.count()`
    - `.find()` vs `.index()` difference (find returns -1, index raises Error)
  - Validation: `.isalpha()`, `.isdigit()`, `.isalnum()`, `.isnumeric()`, `.isdecimal()`, `.isspace()`, `.istitle()`, `.isupper()`, `.islower()`, `.isidentifier()`
  - Modify: `.strip()`, `.lstrip()`, `.rstrip()`, `.replace()`, `.expandtabs()`
  - Split/Join: `.split()`, `.rsplit()`, `.splitlines()`, `.join()`, `.partition()`, `.rpartition()`
  - Alignment: `.center()`, `.ljust()`, `.rjust()`, `.zfill()`
  - Check: `.startswith()`, `.endswith()`
  - `.encode()`, `.decode()`
  - `.maketrans()`, `.translate()`
- **String Formatting** (3 methods):
  1. `%` formatting: `"Hello %s, age %d" % ("John", 25)`
  2. `.format()`: `"Hello {}, age {}".format("John", 25)`, `"{name}".format(name="John")`
  3. **f-strings** (Python 3.6+): `f"Hello {name}, age {age}"`, `f"{value:.2f}"`, `f"{num:>10}"`, `f"{num:08b}"`
  - f-string expressions: `f"{2+3}"`, `f"{'hello':>10}"`, `f"{lst[0]}"`, `f"{obj.attr}"`
  - f-string `=` debugging: `f"{variable=}"` (Python 3.8+)
- **Escape Sequences**: `\n`, `\t`, `\\`, `\'`, `\"`, `\0`, `\a`, `\b`, `\r`, `\f`, `\ooo`, `\xhh`, `\uXXXX`, `\UXXXXXXXX`
- **`ord()` & `chr()`** — ASCII/Unicode conversion
- **String concatenation**: `+` vs `.join()` (performance difference — `.join()` is faster)
- **String multiplication**: `"abc" * 3`
- **`in` operator for substring check**: `"hello" in "hello world"` → `True`
- **Bytes vs Strings**: `b"hello"` vs `"hello"`, encoding/decoding
- **String interning** — Python caches small strings

**Quiz trap questions:**
- What does `"hello"[1:100]` return? (No Error, returns `"ello"` — slicing can exceed bounds)
- What is `"abc" > "abd"`? (`False` — lexicographic comparison)
- `"hello world".split()` vs `"hello world".split(" ")` difference
- What is `"   ".isspace()`? (`True`)
- What is `"" == False`? (`False` — `bool("") == False` but `"" == False` is `False`)
- `"123".isdigit()` vs `"123".isnumeric()` vs `"123".isdecimal()`

---

### 📁 Notebook 04: `04_Lists.ipynb`

Topics to cover:
- List creation: `[]`, `list()`, `list(range(10))`, `list("hello")`
- Indexing, slicing (same rules as strings)
- **List Methods** (all of them):
  - `.append(x)` — adds to end (one element)
  - `.extend(iterable)` — adds to end (multiple elements)
  - `.insert(i, x)` — inserts at specific position
  - `.remove(x)` — removes first occurrence (ValueError if not found)
  - `.pop(i)` — removes by index and returns (default: last element)
  - `.clear()` — removes all
  - `.index(x, start, end)` — finds element
  - `.count(x)` — how many times present
  - `.sort(key=None, reverse=False)` — in-place sort (returns None!)
  - `.reverse()` — in-place reverse (returns None!)
  - `.copy()` — shallow copy
  - `.append()` vs `.extend()` difference: `[1,2].append([3,4])` → `[1,2,[3,4]]`
- **`sorted()` vs `.sort()`** — sorted() returns a new list, .sort() returns None
- **List Comprehension**:
  - Basic: `[x for x in range(10)]`
  - Conditional: `[x for x in range(10) if x % 2 == 0]`
  - If-else: `[x if x > 0 else -x for x in lst]` (if-else comes first!)
  - Nested: `[x for sublist in matrix for x in sublist]`
  - Multiple conditions: `[x for x in range(100) if x % 2 == 0 if x % 3 == 0]`
- **Shallow Copy vs Deep Copy** (very important!):
  - `b = a` — reference copy (same object)
  - `b = a[:]` / `b = a.copy()` / `b = list(a)` — shallow copy
  - `b = copy.deepcopy(a)` — deep copy
  - Show the difference with nested lists: in shallow copy, nested lists are still shared!
- **List as Stack**: `.append()` + `.pop()` (LIFO)
- **List as Queue**: use `collections.deque` (list is slow)
- **List unpacking**: `a, b, *rest = [1, 2, 3, 4, 5]`
- **`del` statement**: `del lst[0]`, `del lst[1:3]`, `del lst`
- **List multiplication trap**: `[[0]*3]*3` — inner lists are the same reference!
- **Iterating**: `for item in lst`, `for i, item in enumerate(lst)`, `for a, b in zip(lst1, lst2)`
- **Nested Lists / Matrix operations**
- **`*` unpacking**: `print(*[1,2,3])` → `1 2 3`

**Quiz trap questions:**
- `a = [[]] * 3; a[0].append(1); print(a)` → `[[1], [1], [1]]` (same reference!)
- What does `lst.sort()` return? (`None`)
- `[1,2,3] + [4,5]` vs `[1,2,3].extend([4,5])` — what's the difference?
- `a = [1,2,3]; b = a; b += [4]; print(a)` → `[1,2,3,4]`
- `a = [1,2,3]; b = a; b = b + [4]; print(a)` → `[1,2,3]` (this is different! `+=` extends, `+` creates a new list)

---

### 📁 Notebook 05: `05_Tuples.ipynb`

Topics to cover:
- Tuple creation: `()`, `(1,)` (single element — comma is essential!), `tuple()`, `tuple([1,2,3])`
- `(1)` vs `(1,)` difference — `(1)` is not a tuple, it's an `int`!
- **Immutability** — cannot change elements, but mutable elements (list) can be modified!
  - `t = ([1,2], [3,4]); t[0].append(5)` — this works!
- Tuple methods: `.count()`, `.index()` (only 2 methods!)
- **Tuple Unpacking**: `a, b, c = (1, 2, 3)`
- **Extended Unpacking**: `a, *b, c = (1, 2, 3, 4, 5)` → `a=1, b=[2,3,4], c=5`
- **Swap trick**: `a, b = b, a`
- **Named Tuples**: `collections.namedtuple`
  - `Point = namedtuple('Point', ['x', 'y'])`
  - `._asdict()`, `._replace()`, `._fields`
- **Tuple vs List** — when to use which:
  - Tuple: hashable (can be dict key), less memory, faster
  - List: mutable, more flexible
- **Tuple as dict key**: `{(1,2): "value"}` — works because hashable
- **`*` unpacking with tuple**: `def func(*args)` — args is a tuple
- **Tuple concatenation**: `(1,2) + (3,4)` → creates a new tuple
- **No tuple comprehension!** — `(x for x in range(10))` is a generator expression

**Quiz trap questions:**
- What is `type((1))`? (`int`) vs `type((1,))` → `tuple`
- `t = (1, [2, 3]); t[1].append(4)` — does it raise an Error? (No!)
- `t = (1, [2, 3]); t[1] += [4]` — raises Error, but the list still changes! (classic trap)
- `hash((1, 2, [3]))` — Error! (list is not hashable)

---

### 📁 Notebook 06: `06_Dictionaries.ipynb`

Topics to cover:
- Dict creation: `{}`, `dict()`, `dict(a=1, b=2)`, `dict([(a,1),(b,2)])`, `dict.fromkeys()`
- Accessing: `d[key]` (KeyError) vs `d.get(key, default)` (safe)
- **Dict Methods** (all of them):
  - `.keys()`, `.values()`, `.items()` — returns view objects
  - `.get(key, default=None)`
  - `.setdefault(key, default)` — adds key if not present
  - `.update(other_dict)` — merges
  - `.pop(key, default)` — removes and returns
  - `.popitem()` — removes last inserted pair (Python 3.7+)
  - `.clear()` — removes all
  - `.copy()` — shallow copy
  - `dict.fromkeys(iterable, value)` — creates dict with same value
- **Dict Comprehension**: `{k: v for k, v in enumerate("abc")}`
- **Dict Ordering**: Python 3.7+ preserves insertion order
- **Nested Dictionaries**
- **Merging dicts**:
  - `{**d1, **d2}` (Python 3.5+)
  - `d1 | d2` (Python 3.9+)
  - `d1 |= d2` (in-place merge, Python 3.9+)
- **`in` operator** — checks keys, not values!
- **Iterating**: `for k in d`, `for k, v in d.items()`, `for v in d.values()`
- **collections module**:
  - `defaultdict` — doesn't raise KeyError, creates default value
  - `OrderedDict` — was important before 3.7, but still has some differences
  - `Counter` — counts elements, `.most_common(n)`, arithmetic operations
  - `ChainMap` — combines multiple dicts
- **Dict key requirements**: key must be hashable! List cannot be a key, tuple can
- **`del d[key]`** — deleting a key
- **Dict unpacking**: `**kwargs` in functions

**Quiz trap questions:**
- `d = {}; d[[1,2]] = "hello"` → Error (list is unhashable)
- `d = {True: 1, 1: 2, 1.0: 3}; print(d)` → `{True: 3}` (True == 1 == 1.0, all are the same key!)
- `dict.fromkeys([1,2,3], [])` trap — all share the same list reference!

---

### 📁 Notebook 07: `07_Sets.ipynb`

Topics to cover:
- Set creation: `{1, 2, 3}`, `set()`, `set([1, 2, 3])`
- Empty set: `set()` (❌ `{}` is an empty dict, not a set!)
- **Set Properties**: unordered, no duplicates, elements must be hashable
- **Set Methods**:
  - Add/Remove: `.add()`, `.remove()` (KeyError), `.discard()` (no error), `.pop()` (random), `.clear()`
  - Set operations: `.union()` / `|`, `.intersection()` / `&`, `.difference()` / `-`, `.symmetric_difference()` / `^`
  - `.issubset()` / `<=`, `.issuperset()` / `>=`, `.isdisjoint()`
  - Update operations: `.update()` / `|=`, `.intersection_update()` / `&=`, `.difference_update()` / `-=`, `.symmetric_difference_update()` / `^=`
- **frozenset** — immutable set, hashable, can be a dict key
- **Set Comprehension**: `{x for x in range(10) if x % 2 == 0}`
- Deduplication with set: `list(set([1,1,2,2,3]))` — but does not preserve order!
- Order-preserving deduplication: `list(dict.fromkeys([1,1,2,2,3]))`

---

### 📁 Notebook 08: `08_Control_Flow.ipynb`

Topics to cover:
- **if / elif / else** — full syntax
- **Ternary Expression**: `x = "yes" if condition else "no"`
  - Nested ternary: `a if c1 else b if c2 else c`
- **for loops**: `for item in iterable`
  - `range(start, stop, step)` — stop is not included!
  - Negative range: `range(10, 0, -1)`
  - `enumerate(iterable, start=0)` — index + value
  - `zip(iter1, iter2)` — parallel iteration
  - `zip_longest` (itertools) — fills shorter one with None
- **while loops**: `while condition:`
  - Infinite loop: `while True: ... break`
- **break, continue, pass**
  - `break` — stops the loop completely
  - `continue` — skips to next iteration
  - `pass` — does nothing (placeholder)
- **for...else and while...else** (VERY IMPORTANT — frequently appears on EPAM tests!):
  - `else` block executes only when the loop finishes **without break**
  - `else` does not execute when `break` is used
- **match-case** (Python 3.10+) — structural pattern matching
  - Basic matching, wildcard `_`, guards `if`, sequence patterns, mapping patterns
- **Nested loops** — `break` only stops the innermost loop
- **Loop performance tips**: list comprehension vs for loop speed

**Quiz trap questions:**
- When does for...else execute? (when loop finishes without break)
- `for i in range(5): pass; else: print("done")` — does "done" get printed? (Yes!)
- `range(0)` is empty — `for i in range(0): ... else: print("x")` → "x" gets printed
- `while False: ... else: print("x")` → "x" gets printed!

---

### 📁 Notebook 09: `09_Functions.ipynb`

Topics to cover:
- **Function definition**: `def func_name(params): ...`
- **return statement** — a function without return returns `None`
- **Multiple return values**: `return a, b` — actually returns a tuple
- **Parameters vs Arguments**
- **Argument types**:
  - Positional arguments
  - Keyword arguments
  - Default arguments — **MUTABLE DEFAULT TRAP**: `def f(lst=[])` (the most classic question!)
    - Correct way: `def f(lst=None): if lst is None: lst = []`
  - `*args` — variable positional (comes as a tuple)
  - `**kwargs` — variable keyword (comes as a dict)
  - Keyword-only arguments: `def f(a, *, b, c):` — b and c must be keyword arguments
  - Positional-only arguments (Python 3.8+): `def f(a, b, /, c, d):` — a and b must be positional
  - Full syntax: `def f(pos_only, /, normal, *, kw_only):`
  - Argument order: positional → *args → keyword → **kwargs
- **Scope — LEGB Rule** (most important!):
  - **L**ocal — inside the function
  - **E**nclosing — outer function of inner functions
  - **G**lobal — module level
  - **B**uilt-in — Python built-ins
  - Show each with examples
- **`global` keyword** — to modify a global variable inside a function
- **`nonlocal` keyword** — to modify a variable in the enclosing scope
- **First-class functions**: functions can be assigned to variables, passed as arguments, returned from functions
- **Lambda functions**: `lambda x, y: x + y`
  - Limitations: only one expression, no statements
  - `sorted(lst, key=lambda x: x[1])`
- **Higher-order functions**:
  - `map(func, iterable)` — applies func to each element
  - `filter(func, iterable)` — keeps elements that return True
  - `reduce(func, iterable)` — from functools, combines elements pairwise
- **Recursion**: base case + recursive case
  - `sys.getrecursionlimit()`, `sys.setrecursionlimit()`
  - Tail recursion — Python does not optimize it
- **Type Hints / Annotations**:
  - `def func(x: int, y: str = "hello") -> bool:`
  - `typing` module: `List[int]`, `Dict[str, int]`, `Optional[str]`, `Union[int, str]`, `Tuple[int, ...]`, `Callable[[int], str]`
  - Has no effect at runtime — only for documentation and IDE
- **Docstrings**: `"""This function does..."""`
- **`*` and `**` unpacking in function calls**: `func(*args, **kwargs)`

**Quiz trap questions:**
- Mutable default argument trap
- `def f(a, b=2, *args, **kwargs)` — which argument is which?
- LEGB scope example — which variable is used?
- `lambda x: x` vs `lambda x: (x)` vs `lambda x: x,` — differences

---

### 📁 Notebook 10: `10_Builtin_Functions.ipynb`

Topics to cover (each with examples):
- **Conversion**: `int()`, `float()`, `str()`, `bool()`, `list()`, `tuple()`, `set()`, `dict()`, `frozenset()`, `bytes()`, `bytearray()`, `complex()`, `chr()`, `ord()`, `hex()`, `oct()`, `bin()`, `ascii()`, `repr()`
- **Math**: `abs()`, `round()`, `min()`, `max()`, `sum()`, `pow()`, `divmod()`
  - `round()` banker's rounding: `round(0.5)` = 0, `round(1.5)` = 2 (trap!)
  - `round(2.675, 2)` = `2.67` (not 2.68 — float precision!)
- **Iteration**: `range()`, `enumerate()`, `zip()`, `reversed()`, `sorted()`, `iter()`, `next()`, `map()`, `filter()`
  - `zip()` — stops at the shortest iterable
  - `enumerate(iterable, start=0)`
  - `sorted(key=..., reverse=...)`
- **Logic**: `all()`, `any()`
  - `all([])` → `True` (empty iterable!)
  - `any([])` → `False`
- **Object**: `id()`, `type()`, `isinstance()`, `issubclass()`, `hash()`, `callable()`, `dir()`, `vars()`, `getattr()`, `setattr()`, `delattr()`, `hasattr()`, `property()`
- **I/O**: `print()` (`sep`, `end`, `file`, `flush` parameters), `input()`
- **Other**: `len()`, `open()`, `super()`, `staticmethod()`, `classmethod()`, `exec()`, `eval()`, `compile()`, `globals()`, `locals()`, `__import__()`
- **`zip()` advanced**: `dict(zip(keys, values))`, unzip: `list(zip(*zipped))`

**Quiz trap questions:**
- What is `round(2.5)`? (`2` — banker's rounding!)
- What is `all([])`? (`True`)
- What is `any([0, "", None, False, 0.0])`? (`False`)
- What does `sorted("hello")` return? (`['e', 'h', 'l', 'l', 'o']` — a list!)

---

### 📁 Notebook 11: `11_OOP.ipynb`

Topics to cover:
- **Class basics**: `class MyClass:`, `__init__`, `self`
- **Instance vs Class variables** — differences, trap examples
  - When class variable is mutable: does modifying via instance affect the class?
- **Instance methods** — `self` parameter
- **`@classmethod`** — `cls` parameter, belongs to class
- **`@staticmethod`** — takes neither self nor cls
- **`@property`** — getter/setter/deleter
- **Inheritance**:
  - Single inheritance
  - `super()` usage
  - Method overriding
  - `isinstance()`, `issubclass()`
- **Multiple Inheritance**:
  - **MRO (Method Resolution Order)** — C3 linearization (very important!)
  - `ClassName.__mro__` / `ClassName.mro()`
  - Diamond problem
- **Encapsulation**:
  - Public: `name`
  - Protected (convention): `_name`
  - Private (name mangling): `__name` → `_ClassName__name`
- **Polymorphism** — same interface, different behavior
- **Dunder/Magic Methods** (all with examples):
  - Construction: `__init__`, `__new__`, `__del__`
  - String: `__str__` (user-friendly), `__repr__` (developer-friendly)
  - Comparison: `__eq__`, `__ne__`, `__lt__`, `__le__`, `__gt__`, `__ge__`
  - Arithmetic: `__add__`, `__sub__`, `__mul__`, `__truediv__`, `__floordiv__`, `__mod__`, `__pow__`
  - Reflected: `__radd__`, `__rsub__`, etc.
  - Augmented: `__iadd__`, `__isub__`, etc.
  - Container: `__len__`, `__getitem__`, `__setitem__`, `__delitem__`, `__contains__`, `__iter__`, `__next__`
  - Callable: `__call__`
  - Context: `__enter__`, `__exit__`
  - Attribute: `__getattr__`, `__setattr__`, `__delattr__`, `__getattribute__`
  - Hash: `__hash__` (if `__eq__` is overridden, `__hash__` becomes None by default)
  - Boolean: `__bool__`, `__len__` (if `__bool__` is absent, `__len__` is used)
- **Abstract Base Classes (ABC)**:
  - `from abc import ABC, abstractmethod`
  - Cannot create an instance from an abstract class
- **`dataclasses`** (Python 3.7+):
  - `@dataclass`, `field()`, `__post_init__`
  - `frozen=True` — immutable
  - `order=True` — automatic comparison methods
- **`__slots__`** — memory optimization, no `__dict__`
- **Composition vs Inheritance**
- **Class decorators**
- **Metaclasses** — brief explanation (type is the metaclass)

**Quiz trap questions:**
- MRO questions — which class's method gets called?
- `__str__` vs `__repr__` — which does print() call?
- Name mangling: `obj.__x` → Error, `obj._ClassName__x` → works
- Class variable trap: mutable class variable

---

### 📁 Notebook 12: `12_Error_Handling.ipynb`

Topics to cover:
- **try / except / else / finally** — full flow
  - `else` — executes when there is no exception
  - `finally` — always executes (even when there is a return!)
- **Exception hierarchy**:
  - `BaseException` → `SystemExit`, `KeyboardInterrupt`, `GeneratorExit`, `Exception`
  - `Exception` → `ValueError`, `TypeError`, `KeyError`, `IndexError`, `AttributeError`, `NameError`, `RuntimeError`, `StopIteration`, `ArithmeticError` (→ `ZeroDivisionError`, `OverflowError`), `LookupError` (→ `KeyError`, `IndexError`), `OSError` (→ `FileNotFoundError`, `PermissionError`), `ImportError` (→ `ModuleNotFoundError`)
- **Multiple except**: `except (ValueError, TypeError) as e:`
- **`raise`** — raising exceptions, `raise` without argument (re-raise)
- **`raise ... from ...`** — exception chaining
- **Custom Exceptions**: 
  ```python
  class MyError(Exception):
      def __init__(self, message, code):
          super().__init__(message)
          self.code = code
  ```
- **`assert` statement**: for debugging, disabled with `-O` flag
- **Exception as control flow** — EAFP vs LBYL
  - EAFP: "Easier to Ask Forgiveness than Permission" — try/except
  - LBYL: "Look Before You Leap" — if checks
  - Python prefers the EAFP style
- **Context manager for error handling**: `with` statement
- **`except Exception` vs `except BaseException`** — difference
- **Bare `except:`** — why it's bad practice (also catches BaseException)
- **`sys.exc_info()`** — getting exception info
- **Traceback reading** — how to read tracebacks
- **Warning system**: `warnings.warn()`
- **`ExceptionGroup`** (Python 3.11+): `except*` syntax

**Quiz trap questions:**
- `try/except/else/finally` — which blocks execute and when?
- What happens when there is a return in the finally block?
- `except:` vs `except Exception:` difference
- Proper creation of custom exceptions

---

### 📁 Notebook 13: `13_Iterators_and_Generators.ipynb`

Topics to cover:
- **Iterator Protocol**: `__iter__()` and `__next__()` methods
- **Iterable vs Iterator** difference
  - Iterable: has `__iter__()` method — list, tuple, dict, set, str
  - Iterator: has both `__iter__()` and `__next__()` methods
  - `iter(iterable)` → returns an iterator
  - `next(iterator)` → next element, raises `StopIteration` at the end
- **Writing a custom Iterator class** — example
- **Generator Functions**: `yield` keyword
  - `yield` vs `return` difference
  - A generator function does not execute immediately when called — returns a generator object
  - Lazy evaluation — computes only when requested
  - `.send()`, `.throw()`, `.close()` methods
  - `yield from` — sub-generator delegation
- **Generator Expressions**: `(x for x in range(10))`
  - Generator expression vs List comprehension — memory difference
  - A generator can only be iterated once!
- **`itertools` module** (most important ones):
  - Infinite: `count()`, `cycle()`, `repeat()`
  - Terminating: `chain()`, `chain.from_iterable()`, `compress()`, `dropwhile()`, `takewhile()`, `groupby()`, `islice()`, `starmap()`, `tee()`, `zip_longest()`
  - Combinatoric: `product()`, `permutations()`, `combinations()`, `combinations_with_replacement()`
- **Generator memory advantage** — 1 million element example
- **`range()` is not an iterator** — it's a range object, it's lazy but not an iterator (can be iterated multiple times)
- **Unpacking generators**: `a, b, c = gen()` (element count must match)

**Quiz trap questions:**
- `g = (x for x in [1,2,3]); list(g); list(g)` — what does the second `list(g)` return? (`[]` — exhausted!)
- `def f(): return 1; yield 2` — is this a generator? (Yes! because of `yield`)
- `sum(x*x for x in range(10))` — no `()` needed here (generator expression)

---

### 📁 Notebook 14: `14_Decorators.ipynb`

Topics to cover:
- **What is a decorator** — a function that takes a function and returns a function
- **Basic decorator pattern**:
  ```python
  def my_decorator(func):
      @wraps(func)
      def wrapper(*args, **kwargs):
          # before
          result = func(*args, **kwargs)
          # after
          return result
      return wrapper
  ```
- **`@syntax`** — `@decorator` = `func = decorator(func)`
- **`functools.wraps`** — why it's important (preserves original function metadata: `__name__`, `__doc__`)
- **Decorator with arguments**:
  ```python
  def repeat(times):
      def decorator(func):
          @wraps(func)
          def wrapper(*args, **kwargs):
              for _ in range(times):
                  result = func(*args, **kwargs)
              return result
          return wrapper
      return decorator
  ```
- **Stacked decorators** — order matters!
  ```python
  @decorator1
  @decorator2
  def func(): ...
  # = decorator1(decorator2(func))
  ```
- **Class-based decorators**: `__init__` + `__call__`
- **Built-in decorators**: `@staticmethod`, `@classmethod`, `@property`, `@abstractmethod`, `@dataclass`, `@functools.lru_cache`, `@functools.total_ordering`, `@functools.singledispatch`
- **`functools.lru_cache`** — memoization, `maxsize` parameter
- **Practical decorator examples**: timing, logging, authentication, retry, validation

**Quiz trap questions:**
- Decorator ordering: `@a @b @c def f` → how is it applied?
- What happens without `@wraps`?
- Decorator with arguments vs without — structural difference

---

### 📁 Notebook 15: `15_File_Handling.ipynb`

Topics to cover:
- **`open()` function**: `open(file, mode, encoding)`
- **File Modes**: `r`, `w`, `a`, `x`, `r+`, `w+`, `a+`, `rb`, `wb`, `ab`
  - `r` — read (default), file must exist
  - `w` — write, deletes/creates file
  - `a` — append, writes to end of file
  - `x` — exclusive create, Error if file exists
  - `+` — read+write
  - `b` — binary mode
- **`with` statement** (context manager) — automatically closes the file
- **Reading**: `.read()`, `.readline()`, `.readlines()`, iteration (`for line in file`)
- **Writing**: `.write()`, `.writelines()`
- **File cursor**: `.seek()`, `.tell()`
- **`os` module**: `os.path.exists()`, `os.path.join()`, `os.listdir()`, `os.mkdir()`, `os.makedirs()`, `os.remove()`, `os.rename()`, `os.getcwd()`, `os.path.isfile()`, `os.path.isdir()`, `os.path.basename()`, `os.path.dirname()`, `os.path.splitext()`
- **`pathlib` module** (modern approach): `Path`, `/` operator, `.read_text()`, `.write_text()`, `.exists()`, `.glob()`, `.iterdir()`
- **JSON handling**: `json.dump()`, `json.dumps()`, `json.load()`, `json.loads()`
- **CSV handling**: `csv.reader()`, `csv.writer()`, `csv.DictReader()`, `csv.DictWriter()`

---

### 📁 Notebook 16: `16_Modules_and_Packages.ipynb`

Topics to cover:
- **Import types**: `import module`, `from module import name`, `from module import *`, `import module as alias`
- **`__name__ == "__main__"`** — what it means, why it's used
- **`__init__.py`** — package initializer
- **Module search path**: `sys.path`
- **Absolute vs Relative imports**: `from . import module`, `from .. import module`
- **Standard library highlights**: `os`, `sys`, `math`, `random`, `datetime`, `json`, `re`, `collections`, `functools`, `itertools`, `pathlib`, `typing`, `copy`, `string`, `textwrap`
- **`dir(module)`** — see what's inside a module
- **Circular imports** — the problem and its solution
- **`__all__`** — defines what gets exported with `from module import *`
- **`importlib`** — dynamic import

---

### 📁 Notebook 17: `17_Closures_and_Scope.ipynb`

Topics to cover:
- **LEGB Rule** — detailed examples
- **What is a Closure**: an inner function "remembers" the variables of its outer function
- **`nonlocal`** — modify a variable in the enclosing scope
- **`global`** — modify a global variable
- **Late Binding trap** (VERY IMPORTANT!):
  ```python
  funcs = [lambda: i for i in range(5)]
  [f() for f in funcs]  # [4, 4, 4, 4, 4] — all are 4!
  # Fix: funcs = [lambda i=i: i for i in range(5)]
  ```
- **Creating a counter with closures**
- **`__closure__`** attribute

---

### 📁 Notebook 18: `18_Context_Managers.ipynb`

Topics to cover:
- **`with` statement** — how it works
- **`__enter__` and `__exit__`** methods
- **Custom context manager class**
- **`contextlib.contextmanager`** — context manager with a decorator
- **Nested `with`**: `with open(a) as f1, open(b) as f2:`
- **Exception handling in `__exit__`** — if it returns True, exception is suppressed
- **`contextlib.suppress()`** — ignore specific exceptions
- **`contextlib.redirect_stdout()`**
- **Async context managers**: `__aenter__`, `__aexit__`

---

### 📁 Notebook 19: `19_Advanced_Topics.ipynb`

Topics to cover:
- **GIL (Global Interpreter Lock)** — what it is, why it exists, its effect on threading
- **Shallow vs Deep Copy** — full explanation, nested object example
- **`is` vs `==`** — identity vs equality
- **Mutable default argument** — why it's a problem, how to fix it
- **String interning** — which strings Python caches
- **Integer caching** — `-5` to `256`
- **`__slots__`** — instead of `__dict__`, saves memory
- **Descriptors** — `__get__`, `__set__`, `__delete__`
- **Metaclasses** — basic concept
- **`*args` and `**kwargs` advanced usage**
- **Unpacking**: `a, *b, c = [1,2,3,4,5]`
- **Chained comparison**: `1 < x < 10` = `1 < x and x < 10`
- **Walrus operator `:=`**
- **`Ellipsis` (`...`)** — in type hints, slicing, as a replacement for pass
- **`_` variable** — last result in interactive mode, "don't care" variable
- **Multiple assignment**: `a = b = []` — same object! trap!
- **Assignment expressions and augmented assignment**: `+=` vs `= ... +`
- **Truthy/Falsy** — all Falsy values: `0`, `0.0`, `0j`, `""`, `[]`, `()`, `{}`, `set()`, `None`, `False`, `range(0)`
- **`__all__`, `__name__`, `__doc__`, `__file__`, `__package__`**
- **Python memory management** — reference counting, garbage collection
- **`weakref`** module basics
- **`functools.partial`** — partial function application
- **`functools.reduce`** — reduce a list to a single value
- **`operator` module** — `operator.add`, `operator.itemgetter`, etc.

---

### 📁 Notebook 20: `20_EPAM_Mock_Test.ipynb`

This notebook should be a full EPAM simulation:
- **65 multiple choice questions**
- **19-minute timer** (with IPython widget if possible, or just an indication)
- Questions should cover all topics
- Questions should be difficult and tricky — like the real test
- Each question's answer and explanation should be in a separate cell
- Difficulty distribution: 30% Easy, 50% Medium, 20% Hard
- **Approximate topic distribution**: Data types (8), Operators (5), Strings (5), Lists (5), Tuples (3), Dicts (5), Sets (2), Control flow (5), Functions (8), Built-ins (3), OOP (8), Error handling (3), Iterators/Generators (3), Decorators (2), Closures (2)

### 📁 Notebook 21: `21_EPAM_Mock_Test_2.ipynb`

Second mock test — different questions, same format.

### 📁 Notebook 22: `22_Quick_Reference_Cheatsheet.ipynb`

A brief summary of all topics — for quick review on exam day.

---

## 🎯 ADDITIONAL INSTRUCTIONS

1. **At the beginning of each notebook, explain the topic's importance** in the context of the EPAM test (e.g., "Approximately 8 questions are expected from this topic")

2. **Every code cell should be runnable** — no syntax errors!

3. **Research EPAM's real questions** on the internet:
   - "EPAM Python assessment questions"
   - "EPAM Python Core test"
   - "Python MCQ tricky questions"
   - "Python certification exam questions"
   - "PCEP PCAP exam questions" (similar format)

4. **Focus on code output questions** — "What is the output of this code?" type questions appear most frequently

5. **Pay special attention to trap/gotcha questions**:
   - Mutable default arguments
   - Late binding in closures
   - `is` vs `==`
   - Integer caching
   - List multiplication trap `[[]] * 3`
   - `for...else`
   - `round()` banker's rounding
   - `sorted()` vs `.sort()` return value
   - Shallow vs deep copy
   - Dictionary key with True/1/1.0
   - Generator exhaustion

6. **At the end of each notebook, include a "Key Takeaways" section** — 5-10 most important points

7. **Difficulty rating** should be next to each question: 🟢 Easy | 🟡 Medium | 🔴 Hard

8. **Cross-references**: reference other notebooks from within a notebook (e.g., "For more details on this topic, see 09_Functions.ipynb")

---

## ⏱️ SUGGESTED STUDY PLAN

Add a study plan at the beginning of each notebook:

| Day | Notebook | Time |
|-----|----------|------|
| 1 | 01_Data_Types + 02_Operators | 3 hours |
| 2 | 03_Strings + 04_Lists | 3 hours |
| 3 | 05_Tuples + 06_Dicts + 07_Sets | 3 hours |
| 4 | 08_Control_Flow + 09_Functions | 3 hours |
| 5 | 10_Builtins + 11_OOP | 4 hours |
| 6 | 12_Errors + 13_Iterators + 14_Decorators | 3 hours |
| 7 | 15_Files + 16_Modules + 17_Closures + 18_Context | 3 hours |
| 8 | 19_Advanced + 22_Cheatsheet | 3 hours |
| 9 | 20_Mock_Test_1 | 1 hour |
| 10 | 21_Mock_Test_2 + Review | 2 hours |

---

**START NOW: Create each notebook as a separate `.ipynb` file. Start from 01 and continue sequentially. Each notebook should have at least 200-300 code cells. Be thorough, detailed, and professional. The quality should be suitable as preparation material for a real EPAM test.**
