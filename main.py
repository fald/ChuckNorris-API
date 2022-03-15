from ChuckNorris import ChuckNorris

if __name__ == "__main__":
    chuck = ChuckNorris()
    print(chuck.get_joke()['value'])
    while(True):
        if (input("Press Enter to get another joke (\'n\' to cancel): ") == 'n'):
            break
        print(chuck.get_joke()['value'])
    