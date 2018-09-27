from termcolor import cprint

def print_ok(text):
  cprint("\n"+text+"\n", "green")


def print_green(text):
  cprint(text, "green")


def print_red(text):
  cprint(text, "red")


def print_blue(text):
  cprint(text, "blue", "on_white")

def print_error(text):
  cprint("\nERROR: "+text+"\n", "red")

def printlarge(input):  #function to print large headings easily.
    print("########### " + input + " ###########")

def printnl():  #function to print new line
    print("\n")