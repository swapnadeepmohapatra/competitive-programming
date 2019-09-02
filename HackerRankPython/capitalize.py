if __name__ == '__main__':
    string = input()
    full_name = string.split(' ')
    capitalized_string = ' '.join((word.capitalize() for word in full_name))
    print(capitalized_string)