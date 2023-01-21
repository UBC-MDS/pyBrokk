from pymine.bow import bow
import pandas as pd

def test_bow():
    """Tests for bow functions.
    this function tests four issues:
    1. Checks whether the last column of input data frame is string.
    2. As the bow function should not add any rows, checks whether the number of rows in both data frames are the same.
    3. As the bow function only applys on the last column of the input data frame, checks whether the first m-1 columns in both data frames are the same.
    4. Compares 
     
    """
    input = pd.DataFrame({
            "url_address": ["first url","second url","third url"],
            "url id": [1,2,3],
            "text": ["this is first url",
                    "this is the second url",
                    "this is not this first url"]
            })
    expected = pd.DataFrame({
            "url_address": ["first url","second url","third url"],
            "url id": [1,2,3],
            "text": ["this is first url",
                    "this is the second url",
                    "this is not this first url"],
            "first" : [1,0,1],
            "is" : [1,1,1],
            "not" : [0,0,1],
            "second" : [0,1,0],
            "the" : [0,1,0],
            "this": [1,1,2],
            "url" : [1,1,1]
            })
    output = bow(input)
    assert (input.applymap(type) == str).all(0)[-1], "last column of the input data frame should be string"
    assert input.shape[0] == output.shape[0] , "the row number of both output and input data frames should be the same"
    assert input.iloc[:,0:-1].equals(output.iloc[:,0:input.shape[1]-1]), "the first m-1 columns of input and output data frames should be the same" 
    assert output.equals(expected) , "The output is not as expected!"
    
