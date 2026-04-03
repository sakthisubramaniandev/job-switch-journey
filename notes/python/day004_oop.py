#Error Handling
def safe_divide(a,b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("You cannot divide a number by zero!")
        return None
    except TypeError:
        print("All the inputs must be numbers!")
        return None
    finally:
        print("Division attempted.")
        
#File Handling        
try:
    with open("my_progress.txt", "w") as f:
        f.write("Day: 004\n")
        f.write("LeetCode solved: 2\n")
        f.write("Topics: Error Handling, File Handling\n")
        
    with open("my_progress.txt", "r") as f:
        for line in f:
            print(line.strip())
except IOError:
    print("Unable to write to the file.")
    
        
        