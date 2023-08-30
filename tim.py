#!/usr/bin/env python
# coding: utf-8

# In[1]:


inventory={
    'purchase':500,
    'bag':['apple','bread','milk'],
    'pack':['canvas','paper', 'rope', 'loaf']
}
x=inventory.items()
print(x)


# In[16]:


inventory={
    'purchase':500,
    'bag':['apple','bread','milk'],
    'pack':['canvas','paper', 'rope', 'loaf']
}
x=inventory.items()
print(x)
inventory['pocket']=['shell', 'berry','mint']
print(x)


# In[14]:


inventory['pack'].remove('paper')


# In[15]:


inventory={
    'purchase':500,
    'bag':['apple','bread','milk'],
    'pack':['canvas','paper', 'rope', 'loaf']
}
x=inventory.items()
print(x)
inventory['pack'].remove('paper')
print(x)


# In[20]:


inventory['purchase']+=50


# In[19]:


inventory={
    'purchase':500,
    'bag':['apple','bread','milk'],
    'pack':['canvas','paper', 'rope', 'loaf']
}
x=inventory.items()
print(x)
inventory['purchase']+=50
print(x)


# In[25]:
prices = {
    'banana': 4,
    'apple': 2,
    'orange': 1.5,
    'pear': 3
}
stock = {
    'banana': 6,
    'apple': 0,
    'orange': 32,
    'pear': 15
}
total = 0

for x in prices:
    if x in stock:
        y = prices[x] * stock[x]  # Use square brackets to access dictionary values
        print(f"The value of {x}: {y}")  # Use f-string for proper string formatting
        total += y
    else:
        print(f"The value of {x} not found")
        
print("Total value:", total)


# In[ ]:


def main():
    outfile = open('student.csv', 'r')
    fcontent=outfile.read()
    print(fcontent)
    outfile.close()



main()


# In[42]:


def main():
    student = {}

    try:
        # Open the CSV file for reading
        outfile = open('student.csv', 'r')

        lines = outfile.readlines()  # Read all lines in the file

        # Iterate through each line (excluding the header)
        for line in lines[1:]:
            columns = line.strip().split(',')  # Split the line into columns

            if len(columns) >= 2:
                student_name = columns[0]  # Extract student name from the first column
                page_views = columns[1]  # Extract page views from the second column
                student[student_name] = page_views  # Add to the dictionary

        print(student)

    except:
        print("An error occurred while reading the file.")

        # Make sure to close the file even if an exception occurs
        outfile.close()

main()


# In[63]:


def main():
    student = {}

    try:
        # Open the CSV file for reading
        outfile = open('student.csv', 'r')

        lines = outfile.readlines()  # Read all lines in the file

        # Iterate through each line (excluding the header)
        for line in lines[1:]:
            columns = line.strip().split(',')  # Split the line into columns

            if len(columns) >= 2:
                student_name = columns[0]  # Extract student name from the first column
                page_views = columns[1]  # Extract page views from the second column
                student[student_name] = page_views  # Add to the dictionary
                sorted_student = dict(sorted(student.items()))
        
        for student_name, page_views in sorted_student.items():
            print(f"Student Name: {student_name}, Page Views: {page_views}")

    except:
        print("An error occurred while reading the file.")

        # Make sure to close the file even if an exception occurs
        outfile.close()

main()


# In[67]:

def main():
    student = {}

    try:
        # Open the CSV file for reading
        with open('student.csv', 'r') as infile:
            lines = infile.readlines()  # Read all lines in the file

            # Iterate through each line (excluding the header)
            for line in lines[1:]:
                columns = line.strip().split(',')  # Split the line into columns

                if len(columns) >= 2:
                    student_name = columns[0]  # Extract student name from the first column
                    page_views = columns[1].strip('"')  # Remove surrounding double quotes from page views
                    
                    # Handle the case where page_views contains non-numeric characters
                    if not page_views.isdigit():
                        print(f"Invalid page views value for {student_name}: {page_views}")
                        continue
                    
                    student[student_name] = page_views  # Add to the dictionary
            
            # Use dictionary comprehension to filter students with page views less than 100
            filtered_students = {student_name: page_views for student_name, page_views in student.items() if int(page_views) < 100}

            # Print the filtered students
            for student_name, page_views in filtered_students.items():
                print(f"Student Name: {student_name}, Page Views: {page_views}")

    except Exception as e:
        print("An error occurred while reading the file:", str(e))

main()





# In[80]:


def main():
    students_data = {}  # Dictionary to store student data {student_name: page_views}
    
    # Read the student.csv file from the same directory
    with open('student.csv', 'r') as infile:
        header = infile.readline()  # Read and ignore the header line
        for line in infile:
            parts = line.strip().split(',')  # Assuming the CSV is comma-separated
            
            student_name = parts[0]  # Student name is the first part
            try:
                page_views = int(parts[1])  # Page views is the second part
            except ValueError:
                # Handle cases where page views are not a valid integer
                continue
            
            students_data[student_name] = page_views
    
    # Sort the student data based on page views
    sorted_students = sorted(students_data.items(), key=lambda x: x[1])
    
    # Create a list of students with page views less than 100
    students_less_than_100_views = [student for student, views in sorted_students if views < 100]
    
    # Print the list of students with page views less than 100
    for student in students_less_than_100_views:
        first_name, last_name = student.split()  # Assuming first name and last name are separated by a space
        print("First Name:", first_name, "Last Name:", last_name)
        
main()



# %%
