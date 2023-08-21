import random
import pandas as pd
import google.generativeai as palm
import os
def pick_random(number_list: list=[], num: int=5)->list:
    # Check if the list has at least 5 unique elements
    if len(number_list) >= num:
        # Pick 5 random non-repeating numbers from the list
        return random.sample(number_list, num)
    else:
        print("The list doesn't have enough unique elements.")
        return []

def vocab(number_list, df):
    return df.iloc[number_list].reset_index(drop=1)

def spelling_test(number_list):
    test_list = pick_random(number_list)
    # print(test_list)
    test_df = vocab(test_list, df)
    score = 0
    wrong_ans = []
    for ii in range(test_df.shape[0]):
        print(test_df['chinese'][ii])
        ans = input('input:')
        if ans == test_df['vocabulary'][ii]:
            score+=1
        else:
            wrong_ans.append(ii)
        # print(test_df.iloc[ii])
    print(f"{score}/{test_df.shape[0]}")
    print(df.iloc[wrong_ans])

def selection_test(df,number_list):
    test_list = pick_random(number_list)
    print(test_list)
    test_df = vocab(test_list, df)
    score = 0
    ans = []
    ans_list = []
    print(test_df)
    for ii in range(test_df.shape[0]):
        print(f"\n[ {test_df['vocabulary'][ii]} ]")
        without_list = list(range(1,test_list[ii])) + list(range(test_list[ii]+1,df.shape[0]))
        random_list = pick_random(without_list,3)
        random_list.append(test_list[ii])
        random.shuffle(random_list)
        ans_list.append(random_list.index(test_list[ii]))
        # print(random_list)
        for jj in range(4):

            word = df['chinese'][random_list[jj]]
            print(f"{jj}.{word}")
        ans.append(input("輸入選項："))
        if int(ans[ii]) == ans_list[ii]:
            score += 1
            print("Correct!")
        else:
            print("NO NO.")
        # print(ans[ii], ans_list[ii])

    print(f"YOUR SCORE: [ {score}/{test_df.shape[0]} ]")
def test_bard():
    """
    At the command line, only need to run once to install the package via pip:
    $ pip install google-generativeai
    """

# import os
# palm.configure(api_key=os.environ["PALM_API_KEY"])
    print(os.environ["PALM_API_KEY"])
    # palm.configure(api_key="YOUR API KEY")

    # defaults = {
    # 'model': 'models/chat-bison-001',
    # 'temperature': 0.25,
    # 'candidate_count': 1,
    # 'top_k': 40,
    # 'top_p': 0.95,
    # }
    # context = ""
    # examples = []
    # messages = [
    # "what is earth",
    # "Earth is the third planet from the Sun and the only astronomical object known to harbor life. According to radiometric dating and other evidence, Earth formed about 4.54 billion years ago, not long after the Sun. Earth is the densest planet in the Solar System and the largest of the four terrestrial planets. It is also the only planet known to have an atmosphere composed primarily of oxygen. The atmosphere protects life on Earth by absorbing ultraviolet solar radiation, warming the surface through greenhouse effect, and reducing temperature extremes between day and night.\n\nThe surface of Earth is mostly covered by water, which is why it is often called the \"blue planet\". The continents and other landmasses are located on the Earth's crust, which is divided into several tectonic plates that move slowly over time. The Earth's interior is composed of a solid inner core, a liquid outer core, and a mantle. The inner core is made of solid iron and nickel, while the outer core is made of liquid iron and nickel. The mantle is made of silicate rocks.\n\nEarth's climate is affected by the Sun, the atmosphere, and the oceans. The Sun provides Earth with energy, which drives the Earth's climate system. The atmosphere traps heat from the Sun, which warms the Earth's surface. The oceans absorb and release heat, which helps to regulate the Earth's climate.\n\nEarth is home to a wide variety of life, including plants, animals, and microorganisms. Life on Earth is thought to have originated about 3.8 billion years ago. The evolution of life on Earth has led to the development of complex organisms, such as humans.\n\nEarth is a beautiful and complex planet. It is the only home we have, and it is important to take care of it."
    # ]
    # messages.append("NEXT REQUEST")
    # response = palm.chat(
    # **defaults,
    # context=context,
    # examples=examples,
    # messages=messages
    # )
    # print(response.last) # Response of the AI to your most recent request
if __name__ == "__main__":
    # df = pd.read_excel('mason2000.xlsx')
    # print(df.head())
    # number_list = list(range(1,df.shape[0]))
    # selection_test(df,number_list)
    test_bard()


    

    