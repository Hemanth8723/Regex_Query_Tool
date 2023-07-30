import re

def main():
    print("=== Regex Query Tool ===")
    while True:
        text = input("\nEnter the text string (or 'q' to quit): ")
        if text.lower() == 'q':
            break

        regex_pattern = input("Enter the regex pattern: ")
        try:
            matches = re.findall(regex_pattern, text)
            if matches:
                print("Matches found:")
                for match in matches:
                    print(f"  - {match}")
            else:
                print("No matches found.")
        except re.error as e:
            print(f"Error in regex pattern: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
