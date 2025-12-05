"""
Python’s mutable objects, such as lists and dictionaries, allow you to change their value or data directly without affecting their identity. In contrast, immutable objects, like tuples and strings, don’t allow in-place modifications. Instead, you’ll need to create new objects of the same type with different values.
"""

"""MUTABLE DATA TYPES
1. Lists
2. Dictionaries
3. Sets
"""

"""
IMMUTABLE DATA TYPES
1. Strings
2. Tuples
"""

"NB:"
"DIFFFERENCE BETWEEN A VARIABLE NAME & THE OBJECT"
"""
1. A Python variable name is a label that refers to a memory location where objects live
2. A Python object is a concrete piece of information that lives in a specific memory location on your computer
"""

"""
Every object has three core characteristics
1. Value
2. Identity 
3. Type
"""

"""
IMPACT OF MUTABLE VS IMMUTABLE OBJECTS ON CODE
1. Immutable objects may require more MEMORY
2. Mutable objects make working with threads challenging i.e require syncronisation
PS: Excessive synchronization weakens concurrency!
"""

"""
IMMUTABLE DATA TYPES
1. Numeric: int, float, complex PS: Boolean datatype is a subclass of int
2. Collection: str, bytes, tuple
"""
"PS: You can use a bytearray object to emulate an existing string!"
"e.g"
def mutate_string(str_ng: str):
    mutable_greeting = bytearray(str_ng.encode("utf-8"))
    print(id(mutable_greeting))
    mutable_greeting[1] = ord("E")

    print("MUTABLE_GREETING>>>>", mutable_greeting)

mutate_string("Hello!")
