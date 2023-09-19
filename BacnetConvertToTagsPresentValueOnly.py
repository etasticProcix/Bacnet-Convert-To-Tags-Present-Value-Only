import json

def process_tags(tag_list, new_tags, parent_name=None):
    for tag in tag_list:
        current_name = tag.get('name', '')
        if tag.get('tagType') == 'Folder' and current_name == 'Object_List':
            process_tags(tag.get('tags', []), new_tags, current_name)
        elif tag.get('tagType') == 'Folder':
            process_tags(tag.get('tags', []), new_tags, current_name)
        elif tag.get('tagType') == 'AtomicTag' and tag.get('name') == 'Present_Value':
            if parent_name:
                tag['name'] = parent_name
            new_tags.append(tag)

# Ask for the name of the input file
input_file = input("Enter the name of the input file: ")

# Read the JSON data from the file
with open(input_file, 'r') as file:
    data = json.load(file)

# Initialize new_tags list
new_tags = []

# Start processing tags
process_tags(data.get('tags', []), new_tags)

# Create a new JSON object with modified tags
new_data = {
    'tags': new_tags
}

# Ask for the name of the output file
output_file = input("Enter the name of the output file: ")

# Write the modified JSON data to the output file
with open(output_file, 'w') as file:
    json.dump(new_data, file, indent=4)

print("File successfully processed!")
