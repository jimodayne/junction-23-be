class Template:
    @classmethod
    def gen_ask_action_type(cls, msg: str):
        sentence = f'classify the following sentence into 2 categories predict, search into the form "": {msg}'

        return sentence

    @classmethod
    def gen_ask_what_predict(cls, msg: str):
        sentence = f'Classify the following setence into 2 categories price or trend into the form "": {msg}'

        return sentence

    @classmethod
    def gen_ask_what_content(cls, msg: str):
        sentence = f'Extract alloy type in this sentence into the form "": {msg.lower()}'

        return sentence

    @classmethod
    def gen_ask_time_period(cls, msg: str):
        sentence = f'How many days to the time period specified in this sentence into the form "": {msg.lower()}'

        return sentence

    @classmethod
    def gen_polish(cls, content, time, prediction):
        sentence = f"tell a short paragraph based on this: The price of '{content}' in {time} days is {prediction}"

        return sentence
