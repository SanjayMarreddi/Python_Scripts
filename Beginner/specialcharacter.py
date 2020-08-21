import re
def fun(s):
    # return True if s is a valid email, else return False
    for i in emails:
        print i
        break

        if "." in i:
            username,website=i.split("@",-1)
            websitename,extension=website.split(".")
            if len(extension)<=3:
                a1=True
            if len(extension)>3:
                a1=False
            for i in username:
                regex = re.compile('[@!#$%^&*()<>?/\|}{~:]')       
            if(regex.search(i) == None): 
                a2=True
            else:
                a2=False
            for j in websitename:
                regex = re.compile('-[@_!#$%^&*()<>?/\|}{~:]')       
            if(regex.search(j) == None): 
                a3=True
            else:
                a3=False
            if a1 and a2 and a3 == True:
                return True
            else:
                return False

def filter_mail(emails):
    return filter(fun, emails)

if __name__ == '__main__':
    n = int(raw_input())
    emails = []
    for _ in range(n):
        emails.append(raw_input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print filtered_emails
