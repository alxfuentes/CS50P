def main():
    tweet = input("Input: ").strip()

    print( "Output: ", shorten( tweet ) )

def shorten( tweet ):
    vowels =["a","e","i","o","u","A","E","I","O","U"]
    ret = ""
    for c in tweet:
        if c not in vowels:
            ret += c
    return ret

main()