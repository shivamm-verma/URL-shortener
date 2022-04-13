
shortyy,longyy = 0,0       # initializing
def main_init():           # program to return a random short link
    import random
    list_alpha = ['a','b','c','d','e','f','g','h','i','j','k','l',\
        'm','n','o','p','q','r','s','t','u','v','w','x','y','z'] 
    lst_shortlink_code = []
    i = 1
    while i <= 6:                 # password unique-code length = 6
        lst_elem = random.choice(list_alpha)
        str_case = random.randint(0,1)
        if str_case == 1:
            lst_elem = lst_elem.upper()
        lst_shortlink_code.append(lst_elem)
        i += 1
    shortlink_code = "".join(lst_shortlink_code)
    shortlink = []           # main shortened link(right now,type = list())
    shortlink.append("https://www.dwarflink.com/")       # server name(OUR)
    shortlink.append(shortlink_code)
    shortlink = "".join(shortlink)            #now it's type = string(str)
    #print(shortlink)
    return shortlink          # return values at last to avoid """STOPPED INTERPRETING"""


if __name__ == "__main__":
        var = main_init()
        print(var)

