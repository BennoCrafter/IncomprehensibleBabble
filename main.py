import random
from tqdm import tqdm


class Generate:
    def __init__(self):
        self.validcharacters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                                "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", ",", ".",
                                "!"]

        self.filename_incomprehensible_text = 'OutputTxtFiles/IncomprehensibleBabble.txt'
        self.loop = 10000
        self.incomprehensibletext = ""
        self.max_characters_in_line = 100

    def GenerateIncomprehensibleText(self):
        # generate incomprehensible babble

        for _ in tqdm(range(round(self.loop/self.max_characters_in_line))):
            for i in range(self.max_characters_in_line):
                self.incomprehensibletext = self.incomprehensibletext + (random.choice(self.validcharacters))
            self.incomprehensibletext = self.incomprehensibletext + "\n"

        # write into write_into_file
        with open(self.filename_incomprehensible_text, "a+") as write_file:
            write_file.write(self.incomprehensibletext)
        write_file.close()


if __name__ == "__main__":
    generate_text = Generate()
    generate_text.GenerateIncomprehensibleText()