# A program to say hello world in different languages.


def main():
    import sys

    lang = "English"

    if (len(sys.argv) < 2):
        sys.argv.append("english")

    for i in range(1, len(sys.argv)):
        lang = sys.argv[i]

        if (lang.lower() == "english"):
            print ("Hello, World!")

        elif (lang.lower() == "spanish"):
            print ("Hola, mundo!")

        elif (lang.lower() == "vietnamese"):
            print ("xim Chào thế giới!")

        elif (lang.lower() == "french"):
            print ("Bonjour, le monde!")

        elif(lang.lower() == "japanese"):
            print("こんにちは世界 - Kon'nichiwa sekai")

        else:
            print ("this shouldn't happen!")


main()
