#!/home/ec2-user/anaconda3/bin/python

import praw
import traceback



def commentExtractor(postId):
    reddit = praw.Reddit('bot1')

    submission = reddit.submission(id=postId)
    submission.comments.replace_more(limit=0)


    # Write our updated list back to the file
    with open("comments.txt", "w") as f:
        f.write(submission.title + "\n")
        f.write(submission.author.name)
        for comment in submission.comments.list():
            f.write(comment.body + "\n")

def main():
    try:
        commentExtractor('6oxkpo')
    except:
        traceback.print_exc(file=sys.stdout)

if __name__ == "__main__":
    main() 
