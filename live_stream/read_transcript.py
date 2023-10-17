from clean_text import main as clean_text

def main():
    # Open the .cha file for reading
    cha_file_path = '../callbank_transcripts/eng/4065.cha'

    try:
        with open(cha_file_path, 'r', encoding='utf-8') as cha_file:
            # Read the file content
            file_content = cha_file.read()

            # Extract the string 
            print(file_content)
            transcript = clean_text(file_content)
            print(transcript)
            # lines = file_content.split('\n')
            # transcript = ''''''
            # for line in lines:
            #     transcript = transcript + line
            # print(transcript)
    except FileNotFoundError:
        print(f"File not found: {cha_file_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()