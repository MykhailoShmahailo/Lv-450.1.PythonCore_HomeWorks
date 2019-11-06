philosophy = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

better_amount = philosophy.count("better")
never_amount = philosophy.count("never")
is_amount = philosophy.count("is")

print(" ")
print("Count the words")
print(" ")

print("Better  ", better_amount)
print("Never  ", never_amount)
print("Is  ", is_amount)

print(" ")
print("Text transform to uppercase")
print(" ")
print(philosophy.upper())

print(" ")
print("Replace i to &")
print(" ")

print(philosophy.replace("i", "&"))
print(" ")