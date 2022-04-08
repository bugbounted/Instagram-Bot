import random
hashtags = []
with open("hashtags.txt") as file:
    for hashtag in file: 
        hashtag = hashtag.strip() 
        hashtags.append(hashtag) 


comments = []
with open("comments.txt") as file:
    for comm in file: 
        comm = comm.strip() 
        comments.append(comm) 

c = random.randint(0, len(comments))
print(comments[c])