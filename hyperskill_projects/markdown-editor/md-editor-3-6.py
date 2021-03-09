def input_text():
    return input("- Text: ")

def plain():
    return input_text()
    
def bold():
    return '**' + input_text() + '**' 
    
def italic():
    return '*' + input_text() + '*'
    
def inline_code():
    return '`' + input_text() + '`'
    
def link():
    label = input("- Label: ")
    url = input("- URL: ")
    return f"[{label}]({url})"

def header():
    level = int(input("- Level: "))
    text = input_text()
    if 1 <= level <= 6:
        return "#" * level + " " + text + "\n"
    else:
        print("The level should be within the range of 1 to 6")

def line_break():
    return '\n'
    
def main():
    formatters = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'line-break']
    special = ['!help', '!done']
    lines = []
    while True:
        user = input("- Choose a formatter: ")
        text = ""
        if user not in formatters:
            if user == "!help":
                print("Available formatters:", ' '.join(formatters))
                print("Special commands:", ' '.join(special))
            elif user == "!done":
                break
            else:
                print("Unknown formatting type or command. Please try again")
                continue
        else:
            if user == 'plain':
                text = plain()
            elif user == 'bold':
                text = bold()
            elif user == 'italic':
                text = italic()
            elif user == 'inline-code':
                text = inline_code()
            elif user == 'line-break':
                text = line_break()
            elif user == 'link':
                text = link()
            elif user == 'header':
                text = header()
        if text:
            lines.append(text)
        print(*lines, sep="")
                

if __name__ == '__main__':
    main()
