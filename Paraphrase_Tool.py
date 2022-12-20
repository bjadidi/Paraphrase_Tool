import openai

def gpt3 (stext):
    openai.api_key = "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"
    response = openai.Completion.create(
        engine= "text-davinci-002", 
        prompt= stext,
        temperature= 0.1,
        max_tokens= 1000,
        top_p= 1
        #frequancy_penalty= 0
        #presence_penalty= 0
    )

    content = response.choices[0].text.split('.')
    #print(content)

    return response.choices[0].text

#query = 'what is global warming?'
input_user = input("Please write the text that you want to paraphrase: ")
query = "Please paraphrase this: " + input_user
response = gpt3(query)
print(response)