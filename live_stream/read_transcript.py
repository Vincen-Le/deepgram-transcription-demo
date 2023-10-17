def main():
    # Step 1: Open the .cha file for reading
    cha_file_path = '../callbank_transcripts/eng/4065.cha'

    try:
        with open(cha_file_path, 'r', encoding='utf-8') as cha_file:
            # Step 2: Read the file content
            file_content = cha_file.read()

            # Step 3: Extract the string (for example, extracting a line)
            # Let's say you want to extract the first line from the file:
            lines = file_content.split('\n')
            if lines:
                first_line = lines[0]
                print("Extracted string:", first_line)
    except FileNotFoundError:
        print(f"File not found: {cha_file_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()