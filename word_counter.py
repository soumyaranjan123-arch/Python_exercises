def main():
    input_text = input('''Input your text: ''')
    counter(input_text)

def counter(text):
    print(f'The total characters in the above text is {len(text)}.')
    print(f'The total words in the above text is {len(text.split())}.')
    print(f'The total lines in the above text is {len(text.splitlines())}.')
    
    with open('text.txt','r') as text:
        print(f'The total lines in the text.txt file is {len(text.readlines())}.')
    

main()