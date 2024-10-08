# course link https://www.youtube.com/watch?v=H2EJuAcrZYU
#<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Start From Time 4:56:30 To 5:17:25
# #<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

print("********* Arguments *********")

def hello(name, lang):
    greadings={
        "English": "Hello",
        "Spanish":"Hola",
        "German":"Hallo"
    }

    msg = f"{greadings[lang]} {name}"
    print(msg)

if __name__ == '__main__':
        

    import argparse

    parser = argparse.ArgumentParser(
        description = "provide a personal greading"
    )



    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True,help="The name of a person to great"
    )

    parser.add_argument(
        "-l","--lang",metavar="language",
        required=True,choices=["English","Spanish","German"],
        help="The language of the greading."
    )



    args = parser.parse_args()
    hello(args.name,args.lang)