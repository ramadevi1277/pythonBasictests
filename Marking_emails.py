EmailList = ['testsample@gmail.com',"test.sample12@gmail.com","sample.test@yahoo.co.in",
            'abc@rediffmail.com','abc@programmingisfun.com',"ProgrammingIsfun@youtube.com"]

for index in EmailList:
    #print(index)
    les = len(index.split('@')[0]) - 2
    import pdb;pdb.set_trace()
    s = index.split('@')[1].rsplit('.')
    ls = len(s[0])-1
    st = index.split('@')[0][0] + str(les * '*') + index.split('@')[0][-1] + '@' + s[0][0] + str(ls * '*') + '.' + s[-1]
    print(st)