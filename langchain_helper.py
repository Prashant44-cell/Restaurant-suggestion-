from  langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from secret_key import OPENAI_API_KEY

import os 
 
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
llm = ChatOpenAI(temperature=0.8) #Here temperature means how the response creative and don't want to incorrect response

def generator_name_and_items(menu):
    # chain1: Generate restaurant name
    prompt_template_name = PromptTemplate(
        input_variables=["menu"],
        template="I want to open a restaurant for {menu} food. Suggest a fancy name for this."
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    # chain2: Generate menu items
    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest me some menu items for {restaurant_name}."
    )
    
    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")
        
    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['menu'],
        output_variables=['restaurant_name', 'menu_items']
    )
    response = chain({'menu': menu})

    return response




if __name__ == "__main__":
    print(generator_name_and_items("Indian"))
 
