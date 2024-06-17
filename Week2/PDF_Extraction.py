import PyPDF2
import pandas as pd

# Path to the PDF file
pdf_path = 'ga2.9.pdf'
subject_a = 'Physics'
subject_b = 'Economics'
subject_a_marks = 69
group_start = 21
group_end = 50
# Read the PDF file
pdf_reader = PyPDF2.PdfReader(pdf_path)

# Function to extract text from specified pages
def extract_text_from_pages(start_page, end_page):
    text = ""
    for page_num in range(start_page, end_page + 1):
        text += pdf_reader.pages[page_num].extract_text()
        text += '\n'
    return text

# Extract text from pages corresponding to groups 21-50
# Assuming each group corresponds to one page, and groups 21-50 are pages 20-49 (0-indexed)
start_page = group_start -1
end_page = group_end - 1
extracted_text = extract_text_from_pages(start_page, end_page)

# Display extracted text for verification (optional)
#print(extracted_text[:2000])

# Now, parse the extracted text and filter data
# Here we assume that the data is structured in a tabular format in the text
lines = extracted_text.split('\n')
data = []
for line in lines:
    if line.strip():
        if line[0] == 'S' or line[0] == 'M':
            continue
        data.append(line.split())

# Convert the list of lists into a pandas DataFrame
df = pd.DataFrame(data, columns=['Math', 'Physics', 'English', 'Economics', 'Biology'])

# Convert relevant columns to numeric types
df[subject_a] = pd.to_numeric(df[subject_a])
df[subject_b] = pd.to_numeric(df[subject_b])

# Filter the data
filtered_df = df[(df[subject_a] >= subject_a_marks)]

# Calculate the total marks
total_marks = filtered_df[subject_b].sum()

print(f'{total_marks}')