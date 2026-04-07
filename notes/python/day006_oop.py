def student_info(name, age, *args, **kwargs):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Subjects: {', '.join(args)}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
#student_info("Alice", 20, "Math", "Science", DOB="1990-01-01", Phone=1234567890)


from collections import Counter

words = ["apple", "banana", "apple", 
         "cherry", "banana", "apple"]

words_count = Counter(words)
print(words_count)
print(words_count.most_common(1))
print(words_count.most_common(2))

