import sys

def read_input_file(input_filename):
    """Reads the input file and returns its contents."""
    try:
        with open(input_filename, 'r') as infile:
            contents = infile.readlines()
        print(f"File '{input_filename}' successfully read.")
        return contents
    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
        sys.exit(1)

def write_output_file(output_filename, contents):
    """Writes the contents to the output file."""
    try:
        with open(output_filename, 'w') as outfile:
            outfile.writelines(contents)
        print(f"Output successfully written to '{output_filename}'")
    except Exception as e:
        print(f"Error writing to file '{output_filename}': {e}")
        sys.exit(1)

if __name__ == "__main__":
    print("Script is running...")

    if len(sys.argv) < 2:
        print("Usage: python testing.py <input_filename>")
        sys.exit(1)

    input_filename = sys.argv[1]

    print(f"Input file provided: {input_filename}")

    # Replace .in with .out in the output file name
    if not input_filename.endswith(".in"):
        print(f"Error: Input file should have a '.in' extension.")
        sys.exit(1)

    output_filename = input_filename.replace(".in", ".out")

    print(f"Output file will be: {output_filename}")

    # Read from input file
    input_contents = read_input_file(input_filename)

    # Write the same content to output file
    write_output_file(output_filename, input_contents)

    print("Script execution finished.")
