# ================================
# MY LIBRARY BOOK ORGANISER
# ================================

# PART 1 - DATA STRUCTURES AND LISTS

books = ["Harry Potter", "Matilda", "The Jungle Book", "Charlotte's Web", "Wonder"]

print("Library Book List:", books)


# PART 2 - LIST OPERATIONS

print("
Total Books:", len(books))
print("First Book:", books[0])
print("Last Book:", books[-1])
print("First Three Books:", books[:3])

books.append("Diary of a Wimpy Kid")
print("
After Adding a Book:", books)

books.remove("The Jungle Book")
print("After Removing a Book:", books)

books.sort()
print("Books Sorted Alphabetically:", books)

books.reverse()
print("Books in Reverse Order:", books)


# PART 3 - DICTIONARIES

librarian = {
    "name": "Ms. Priya",
    "section": "Children's Books",
    "experience": 5
}

print("
Librarian Profile:", librarian)


# PART 4 - DICTIONARY OPERATIONS

print("Librarian Name:", librarian["name"])
print("Library Section:", librarian["section"])
print("Experience:", librarian.get("experience"))

librarian["experience"] = 6
print("Updated Experience:", librarian)

librarian["email"] = "priya@schoollibrary.com"
print("After Adding Email:", librarian)

librarian.pop("section")
print("After Removing Section:", librarian)


# PART 5 - CONVERTING A LIST INTO A DICTIONARY

book_ids = [101, 102, 103, 104, 105]
book_names = ["Matilda", "Wonder", "Harry Potter", "Charlotte's Web", "Diary of a Wimpy Kid"]

book_directory = dict(zip(book_ids, book_names))

print("
Book Directory:", book_directory)


# FINAL SUMMARY

print("
================================")
print("LIBRARY ORGANISER SUMMARY")
print("================================")
print("Available Books:", books)
print("Librarian Details:", librarian)
print("Book ID Directory:", book_directory)
print("================================")

