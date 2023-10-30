import re
from read_transcript import read_transcript

def main(input_text):
    return clean_text(input_text)


def clean_text(text):
    # Step 1: Remove beginning text data
    cleaned_text = re.sub(r'(?m)^\@.*\n?', '', text)

    # Step 2: Remove text markers and timestamps
    cleaned_text = re.sub(r'&=[^ ]*', '', cleaned_text)
    cleaned_text = re.sub(r'\*.:|\d+_\d+', '', cleaned_text)

    # Step 3: Replace newline characters with spaces
    cleaned_text = cleaned_text.replace('\n', ' ')

    # Step 4: Strip multiple spaces into single spaces
    cleaned_text = re.sub(r'    ', ' ', cleaned_text)
    cleaned_text = re.sub(r'   ', ' ', cleaned_text)
    cleaned_text = re.sub(r'  ', ' ', cleaned_text)

    # Step 5: Remove unwanted characters using regex
    cleaned_text = re.sub(r'&-um|\.', '', cleaned_text)

    cleaned_text = re.sub(r'    ', ' ', cleaned_text)
    cleaned_text = re.sub(r'   ', ' ', cleaned_text)
    cleaned_text = re.sub(r'  ', ' ', cleaned_text)

    cleaned_text = re.sub(r'xxx', ' ', cleaned_text)

    # Step 6: Remove unnecessary spaces and punctuation
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s.?]', '', cleaned_text)

    # cleaned_text=cleaned_text.replace(",","")
    # cleaned_text=cleaned_text.replace(".","")
    # cleaned_text=cleaned_text.replace("'","")

    return cleaned_text.strip()  # Removes leading and trailing spaces


# Input text
input_text = '''
*B:    But &-um . 238070_238670
*A:    uh, uh, the the the main reason for that is I had not really
    anticipated a few expenses that recently came up . 239130_246640
*B:    ah . 246990_247620
*A:    uh, related to a couple of burglaries that I had . 247010_250770
*B:    oh, harsh .
*B:    Harsh . 251130_252630
*A:    yeah .
*A:    yeah, but, and . 252280_255060
*A:    Not a whole lot I can do about that now . 255770_257400
*B:    Indeed .
*B:    Indeed . 257859_259010
*A:    have to deal with the situation .
*A:    And . 258709_260380
*A:    So that's what I'm doing . 261200_262160
*B:    Sounds good . 262750_263560
*A:    But &-um . 262980_263610
'''

# # Transcript text
# filepath = '../callbank_transcripts/eng/4065.cha'
# transcript_text = read_transcript(filepath)
# print(f"Before: {transcript_text}")

# # Getting cleaned text
# cleaned_text = clean_text(transcript_text)
# print(f"After: {cleaned_text}")

# print(cleaned_text)