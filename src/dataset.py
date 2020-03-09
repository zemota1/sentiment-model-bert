import transformers
from nltk.tokenize import RegexpTokenizer


class IMDBDataset:

    def __init__(self, review, label):
        self.__review = review.values
        self.__label = label.values
        self.__tokenizer = transformers.BertTokenizer.from_pretrained(
            "../input/",
            do_lower_case=True
        )
        self.__max_length = 512

    def get_max_len(self):
        return self.__max_length

    def get_tokenizer(self):
        return self.__tokenizer

    def get_review(self):
        return self.__review

    def get_label(self):
        return self.__label

    def __len__(self):
        return len(self.get_review())

    def __getitem__(self, item):
        text = str(self.get_review()[item])

        tokenizer = RegexpTokenizer(r'\w+')
        text_clean = tokenizer.tokenize(text)
        print(text_clean)

