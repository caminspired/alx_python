def multiple_returns(sentence):
    if len(sentence) == 0:
        return (0, None)
    else:
        return (len(sentence), sentence[0])
        print ("Length: {} - First character: {}".format(len(sentence), (sentence[0])))
