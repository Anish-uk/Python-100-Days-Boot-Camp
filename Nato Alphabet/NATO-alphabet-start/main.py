import pandas
student_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
nato = {row.letter:row.code for index,row in student_data_frame.iterrows()}


def generate_nato():
    word = input("Enter the name:").upper()
    try:
        nato_list = [nato[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet")
        generate_nato()
    else:
        print(nato_list)

generate_nato()
