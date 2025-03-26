from renderer import render_pages, CONFIG

if __name__ == '__main__':
    
    power = '$Engine'
    _input = input(power + ':')
    
    if _input == 'start':
        render_pages()
        print("Successfully Completed")
    
    else: print('Invalid Input')
