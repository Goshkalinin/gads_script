import openai
from KEYS import OPENAI_KEY


def set_role():
    openai.api_key = OPENAI_KEY

    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": "Next time you should give back synonym to a word, ok?"}])

    print(completion.choices[0].message.content)



def generate_text(prompt):
    openai.api_key = OPENAI_KEY

    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=[{"role": "user", "content": "Butter"}])

    print(completion.choices[0].message.content)



if __name__ == "__main__":
    set_role()
    generate_text('asd')





