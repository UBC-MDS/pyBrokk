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
    >>> text = "ChatGPT was launched as a prototype on November 30, 2022, and quickly garnered \n
                attention for its detailed responses and articulate answers across many domains \n
                of knowledge." 
    >>> bow(text)
   [a, across, and, answers, articles, as, attention, domains, its, chatgpt, detailed, for, garnered,
   lnowledge,launched, many, november, on, prototype, quickly, responses, was, 2022, 30  ]
    """
    # count_words code goes here...