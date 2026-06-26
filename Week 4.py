nums = [10, 20, 30, 40, 50]
print("Length:", len(nums))
print("Type:", type(nums))
ordered = True
print("Ordered:", ordered, "- Lists maintain the order in which elements are added.")
print("30 in nums:", 30 in nums)
print("First element:", nums[0])
print("Last element:", nums[-1])
nums.remove(40)
nums[1] = 200
print("Final list:", nums)
data = ("apple", "banana", "cherry", "date")
print("Length:", len(data))
print("Type:", type(data))
ordered = True
print("Ordered:", ordered, "- Tuples maintain the order of their elements.")
print("banana in data:", "banana" in data)
print("Element at index 3:", data[3])
try:
    data.remove("cherry")
except AttributeError as e:
    print("Error while removing:", e)
    try:
        data[0] = "apricot"
    except TypeError as e:
        print("Error while updating:", e)
        print("Tuple:", data)
        s = {1, 2, 3, 3, 4}
        print("Length:", len(s))
        print("Type:", type(s))
        ordered = False
print("Ordered:", ordered, "- Sets are unordered and do not support indexing.")
print("2 in s:", 2 in s)
try:
    print(s[0])
except TypeError as e:
    print("Error while accessing by index:", e)
s.remove(4)
s.add(10)
print("Final set:", s)
person = {"name": "Ali", "age": 20, "city": "Karachi"}
print("Length:", len(person))
print("Type:", type(person))
ordered = True
print("Ordered:", ordered, "- Dictionaries preserve the insertion order of keys in modern Python (Python 3.7+).")
print("'name' in person:", "name" in person)
print("Age:", person["age"])
person.pop("city")
person["age"] = 21
print("Final dictionary:", person)
words = ["red", "green", "blue", "yellow"]
print("Length:", len(words))
print("Type:", type(words))
ordered = True
print("Ordered:", ordered, "- Lists maintain the order of their elements.")
print("'purple' in words:", "purple" in words)
print("Element at index 2:", words[2])
print("Element at index 2:", words[2])
words.remove("green")
words.insert(1, "orange")
print("Final list:", words)
t = (5, 10, 15, 20)
print("Length:", len(t))
print("Type:", type(t))
ordered = True
print("Ordered:", ordered, "- Tuples maintain the order of their elements.")
print("15 in t:", 15 in t)
print("Element at index 2:", t[2])
try:
    t.remove(10)
except AttributeError as e:
    print("Error while removing:", e)
t = (5, 99, 15, 20)
print("New tuple:", t)
a = {1, 2, 3}
b = {3, 4, 5}
print("Length of a:", len(a))
print("Length of b:", len(b))
print("Type of a:", type(a))
print("Type of b:", type(b))
ordered = False
print("Ordered:", ordered, "- Sets are unordered and do not support indexing.")
print("4 in a:", 4 in a)
try:
    print(a[0])
except TypeError as e:
    print("Error while accessing by index:", e)
    a.remove(2)
a.update(b)
print("Final set a:", a)
student = {
    "id": 101,
    "name": "Sara",
    "scores": {
        "math": 80,
        "science": 90
    }
}
print("Length of student:", len(student))
print("Length of student['scores']:", len(student["scores"]))
print("Type of student:", type(student))
print("Type of student['scores']:", type(student["scores"]))
ordered = True
print("Ordered:", ordered, "- Dictionaries preserve the insertion order of keys in Python 3.7+.")
print("'math' in student['scores']:", "math" in student["scores"])