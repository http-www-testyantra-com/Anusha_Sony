def get_input():
    try:
      a=int(input("enter the value of a"))
      b=int(input(("Enter the value of b")))

    except ValueError as e:
        print(e)
        return get_input()
    finally:
        print("Im finally of get_input")


def div(a,b):
    try:
     c=a/b
     return c
    except ZeroDivisionError as e:
        print(e)
        return get_input()
    finally:
        print("Im finally of div method")
def main():
    try:
        a,b=get_input()
        c=div(a,b)
        print(c)
    except ZeroDivisionError as e:
        print(e)
        main()
    except Exception as e: # Parent Exception
        print(e)
        main()
    except:
        print("Exception arised due to sudden key entrered")
        main()
    finally:
        print("Process Completedd")

if __name__ == '__main__':
    main()



