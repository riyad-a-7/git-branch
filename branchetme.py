# git branch
# git switch
# git merge
# git branch -d
# git reset commit_code
# git reset --hard commit_code
# git stash
# git clone
# git branch -U main
# git push origin main
# git set-url origin <link>
# git remote -v
# git pull

# git branch
def Sums(user_input1, user_input2):
    from time import sleep
    print("iki ededin toplenmasi:")
    print("calcutation...")
    sleep(1)
    return f"{user_input1} + {user_input2} = {user_input1 + user_input2}"

def Subs(user_input1, user_input2):
    from time import sleep
    print("iki ededin cixilmasi:")
    print("calcutation...")
    sleep(1)
    return f"{user_input1} - {user_input2} = {user_input1 - user_input2}"

user_input1 = int(input("Birinci ededi daxil edin: "))
user_input2 = int(input("Ikinci ededi daxil edin: "))
print(Sums(user_input1, user_input2))


