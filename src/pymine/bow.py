def bow(text):
    """
    Converts a raw text to a list of target words as strings
    
    Parameters
    ----------
    text : str
           
    Returns
    ----------
    words : list
        list of all intended words 
        
    Examples
    ----------
    >>> text = \"""ChatGPT (Generative Pre-trained Transformer)[1] is a chatbot launched by OpenAI in November 2022. 
                  ChatGPT was fine-tuned on top of GPT-3.5 using supervised learning as well as reinforcement learning.[5]\""" 
    >>> bow(text)
            [{'2022': 1,
            'chatbot': 1,
            'chatgpt': 2,
            'fine': 1,
            'generative': 1,
            'gpt': 1,
            'launched': 1,
            'learning': 2,
            'november': 1,
            'openai': 1,
            'pre': 1,
            'reinforcement': 1,
            'supervised': 1,
            'trained': 1,
            'transformer': 1,
            'tuned': 1,
            'using': 1}]
    """
    words = CountVectorizer(stop_words='english')
    words_matrix = words.fit_transform([text])
    words_array = words_matrix.toarray()
    df = pd.DataFrame(data=words_array, columns = words.get_feature_names()).to_dict('records')
    return df
