from clean_text import main as clean_text

def main(filepath):
    # Open the .cha file for reading
    cha_file_path = filepath

    try:
        with open(cha_file_path, 'r', encoding='utf-8') as cha_file:
            # Read the file content
            file_content = cha_file.read()

            return file_content
    except FileNotFoundError:
        print(f"File not found: {cha_file_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()