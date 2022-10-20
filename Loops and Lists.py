def main():


    List = [1,2,3,7]
    print(str(seven(List)))


def seven(l):

    for i in range(len(l)):
        if l[i] == 7:
            if i+1 >= len(l):
                return False
            elif l[i+1] == 7:
                return True
    return False



if __name__ == "__main__":
    main()


