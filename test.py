import random
import pandas as pd
import google.generativeai as palm
import os
import sys
sys.path.append('/Users/liushiwen/Desktop/github')
from config import get_config 

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
    # print(test_list)
    test_df = vocab(test_list, df)
    score = 0
    ans = []
    ans_list = []
    print(test_df)
    input('enter anything to continue the exam...')
    print('\n'*50)
    for ii in range(test_df.shape[0]):
        print(f"\n[ {test_df['vocabulary'][ii]} ]")
        without_list = list(range(1,test_list[ii])) + list(range(test_list[ii]+1,df.shape[0]))
        random_list = pick_random(without_list,3)
        random_list.append(test_list[ii])
        random.shuffle(random_list)
        ans_list.append(random_list.index(test_list[ii]))
        for jj in range(4):

            word = df['chinese'][random_list[jj]]
            print(f"{jj}.{word}")
        ans.append(input("輸入選項："))
        if int(ans[ii]) == ans_list[ii]:
            score += 1
            print("Correct!")
        else:
            print("WRONGGG:")
            english_word = test_df['vocabulary'][ii]
            chinese_ans = df['chinese'][random_list[ans_list[ii]]]
            print(f"The answer of [ {english_word} ] is {chinese_ans}.")

    print(f"YOUR SCORE: [ {score}/{test_df.shape[0]} ]")
def test_bard(vocab):
    """
    At the command line, only need to run once to install the package via pip:
    $ pip install google-generativeai
    """

    config = get_config()
    palm.configure(api_key=config["PALM_API_KEY"])

    defaults = {
    'model': 'models/chat-bison-001',
    'temperature': 0.25,
    'candidate_count': 1,
    'top_k': 40,
    'top_p': 0.95,
    }
    context = ""
    examples = []
    messages = []
    messages.append(f"I am preparing for GRE. I currently learning about vocabularies. Write a sentence contains the word \"{vocab}\".")
    response = palm.chat(
    **defaults,
    context=context,
    examples=examples,
    messages=messages
    )
    print(response.last) # Response of the AI to your most recent request
    
if __name__ == "__main__":
    df = pd.read_excel('mason2000.xlsx')
    # print(df.head())
    number_list = list(range(1,df.shape[0]))
    selection_test(df,number_list)
    # test_bard("exactitude")


    

    