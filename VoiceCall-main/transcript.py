import json

# Sample text data (you would read this from your source)
text_data = """This is the first paragraph. It contains some information about a topic.This is the second paragraph. It provides more details on the same topic.And here's the third paragraph. It concludes the discussion.
"""

# Split the text into paragraphs
paragraphs = text_data.strip().split('\n\n')

# Initialize an empty list to store the JSON data
json_data = []

# Iterate over each paragraph and create a dictionary
for i, paragraph in enumerate(paragraphs):
    # Split each paragraph into lines
    lines = paragraph.strip().split('\n')
    
    # Create a list to store the lines of the paragraph
    paragraph_lines = []
    for line in lines:
        paragraph_lines.append(line.strip())
    
    paragraph_dict = {
        "paragraph_number": i + 1,
        "lines": paragraph_lines
    }
    json_data.append(paragraph_dict)

# Convert the data to JSON format
json_string = json.dumps(json_data, indent=2)

# Print or save the JSON string
print(json_string)