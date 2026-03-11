import os

# Configuration
directory_path = r"C:\Kriti 2026\bot\datasets\parcel_box\labelss"
new_first_number = "7" # Usually these are integers (0, 1, 2, etc.) for class IDs

# Iterate through every file in the directory
for filename in os.listdir(directory_path):
    # Only process .txt files
    if filename.endswith(".txt"):
        file_path = os.path.join(directory_path, filename)
        
        # 1. Read the current content
        with open(file_path, "r") as file:
            content = file.read()

        # 2. Split content, change first number, and rejoin
        data = content.split()
        if data:
            data[0] = str(new_first_number)
            new_content = " ".join(data)

            # 3. Save the modified content back to the file
            with open(file_path, "w") as file:
                file.write(new_content)
            
            print(f"Updated: {filename}")
        else:
            print(f"Skipped (empty): {filename}")

print("--- Processing Complete ---")