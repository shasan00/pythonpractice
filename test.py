def studentGrades(name, grade):
    gradebook = dict(zip(name, grade))
    query = input("Enter a student name: ").strip()

    if query in gradebook:
        return gradebook[query]
    else:
        return "Student not found."

studentGrades(["syed", "santosh", "angela"], [90, 20, 30])