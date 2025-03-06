def count_lines_in_file(filename):
    try:
        with open(filename, 'r', encoding="utf-8") as file:
            line_count = sum(1 for _ in file)
        print(f"Total number of lines: {line_count}")
    except FileNotFoundError:
        print("Error: File not found.")

count_lines_in_file("example.txt")  
