from termcolor import colored


class FindInp:
    def __init__(self):
        self.filename_incomprehensible_text = 'OutputTxtFiles/IncomprehensibleBabble.txt'
        self.print_color = "blue"

    def read_file(self):
        with open(self.filename_incomprehensible_text) as f:
            self.text = f.read()

    def get_inp_in_data(self, user_inp):
        index = self.text.find(user_inp)
        print("Es ist an der Position " + str(index) + " bis " + str(index + len(user_inp)))
        substring = self.text[index-10:index + len(user_inp) + 10]
        for_user_inp = substring[0:10]
        after_user_inp = substring[len(user_inp):10]
        print(for_user_inp + colored(substring[10:10+len(user_inp)], self.print_color) + after_user_inp)
        if index == -1:
            print("Es tut mir leid! Dies exestiert bei uns noch nicht!")

    def output(self, user_inp):
        self.get_inp_in_data(user_inp=user_inp)


if __name__ == "__main__":
    find_input = FindInp()
    find_input.read_file()
    find_input.output(user_inp=input("Input:"))
