import os

# Input and output file names
INPUT_FILE = "sample_env.env"
OUTPUT_FILE = ".env"

# Check if the input file exists
if not os.path.exists(INPUT_FILE):
    print(f"Error: Input file '{INPUT_FILE}' does not exist.")
    exit(1)

# Read the input file and process each line
with open(INPUT_FILE, 'r') as infile, open(OUTPUT_FILE, 'w') as outfile:
    for line in infile:
        # Write comments and empty lines directly to the output file
        if line.strip().startswith("#") or not line.strip():
            outfile.write(line)
            continue

        # Process lines with "VAR=VALUE" format
        if "=" in line:
            var, value = line.strip().split("=", 1)
            print(f"Current value of {var} is '{value}'")
            new_value = input(f"Enter new value for {var} (leave blank to keep current value): ").strip()

            # Use the default value if no new value is provided
            if not new_value:
                new_value = value

            # Write the variable and its value to the output file
            outfile.write(f"{var}={new_value}\n")
        else:
            # Handle malformed lines
            print(f"Warning: Skipping malformed line: {line.strip()}")
            outfile.write(line)

print(f"Updated environment variables saved to '{OUTPUT_FILE}'.")
