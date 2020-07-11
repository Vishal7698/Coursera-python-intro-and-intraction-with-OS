def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'",<>.?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my","we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its","they", "them","their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being","have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when","where", "how","all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very","can", "will", "just"]

    # LEARNER CODE START HERE
    list_op=[]
    no=0;
    for word in file_contents:
        for letter in word:
            if letter in punctuations:
                word1 = word.replace(letter,'')
                file_contents[no]=word1


        if word in uninteresting_words:
            file_contents.remove(word)

        no=no+1
    return file_contents


def generate_from_frequencies(file_contents):
    text = {}

    for al in file_contents:
        if al not in text:
            text[al] = set()
            text[al]=0
        if al in text:
            text[al]=text[al]+1
    return text

sd=["asc","!bas","is","#pardfdft","the","how","&lucky" , "bas","bas","asc"]
ay=calculate_frequencies(sd)
print(ay)
print(generate_from_frequencies(ay))

for word in file_contents:
    for letter in word:
        if letter in punctuations:
            word1 = word.replace(letter, '')
            file_contents[no] = word1
    if word in uninteresting_words:
        file_contents.remove(word)

text = {}

for al in file_contents:
    if al not in text:
        text[al] = set()
        text[al] = 0
    if al in file_contents:
        text[al] = text[al] + 1
return text
