import openai
import codecs
from KEYS import OPENAI_KEY


def generate_text():
    openai.api_key = OPENAI_KEY

    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt="напиши 50 слов",
        max_tokens=50
        )

    response_text = response['choices'][0]['text']

    print(response_text)
    print(response)



if __name__ == "__main__":
    #generate_text()
    get_account_info()
