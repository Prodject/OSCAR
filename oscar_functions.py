"""Module that contains code commonly used by actions, and core OSCAR components"""
import os, sys, subprocess, collections, re, json, getpass, importlib
import oscar_defaults
import actions
from actions import *
from tkinter import *
from tkinter import filedialog

#The responses, inputs, settings, and groups lists to be loaded or generated
responses = []
inputs = []
settings = []
groups = []

#Boolean that tells if it's the user's first time launching OSCAR
firstTime = True
#String that stores the command that the user last entered
command = None

def subprocess_cmd(bash_command):
    """Runs commands as a detached subprocess.

    Used in command scheduling, alongside with the /usr/bin/sleep command.
    Sample input: subprocess_cmd("sleep 60 && poweroff")
    """
    subprocess.Popen(bash_command,stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, preexec_fn=os.setpgrp)

def open_file_manager(location):
    """Opens a file manager window for the user to select a file from"""
    root = Tk()
    root.withdraw()
    root.filename = filedialog.askopenfilename(initialdir = location, title = "Select file")
    return root.filename

def get_yes_no(confirm, type = None):
    """Decides if a particular string is a positive or negative statement.

    In other words, it can read a string as yes/no.

    Arguments
    ---------
    confirm : string
        Variable that contains the string to be parsed
    type (optional) : any
        If this variable is defined, it checks if the string means no
        If the variable is left undefined, it checks if the string means yes

    Returns
    -------
    Boolean
        The boolean value indicating whether or not the string means yes or no.
        If passed with a type specified, the method will return True if the string
        means no, and False if the string means Yes.
        If passed without a type specified, the method will return True if the string
        means Yes, and False if the string means No.

    May be deprecated in the future, and replaced with a classification algorithm
    """
    global inputs
    contained_yes = ""
    if type == None:
        for i in range(0, len(inputs[9][0])):
            if contained_yes == "":
                if re.search(inputs[9][0][i],confirm):
                    contained_yes = inputs[9][0][i]
                if contained_yes != "" and len(inputs[9][1]):
                    for antiword in inputs[9][1]:
                        if re.search(antiword, confirm):
                            contained_yes = ""
            if contained_yes != "":
                return True
                break
        return False
    else:
        for i in range(0, len(inputs[8][0])):
            if contained_yes == "":
                if re.search(inputs[8][0][i], confirm):
                    contained_yes = inputs[8][0][i]
                if contained_yes != "" and len(inputs[8][1]):
                    for antiword in inputs[8][1]:
                        if re.search(antiword, confirm):
                            contained_yes = ""
            if contained_yes != "":
                return True
                break
        return False

def get_response(index, delimiter = None, replacement = None):
    """Randomly fetches an appropriate response from the responses array.

    Arguments
    ---------
    index : int
        An integer reflecting which response set to select from
    delimiter (optional) : string,
        A string to be replaced with replacement. For example, "<user>"
    replacement (optional) : string,
        A string that replaces the delimiter. For example, "foo"

    Returns
    -------
    String
        Returns a random string from the selected response set, with delimiters replaced if specified.
    """
    if delimiter == None or replacement == None:
        if responses:
            return responses[index][randint(0, len(responses[index]) - 1)]
        else:
            return oscar_defaults.responses_array[index][randint(0, len(oscar_defaults.responses_array[index]) - 1)]
    else:
        return get_response(index).replace(delimiter, replacement)

def open_in_browser(url):
    """Opens a given URL in the user's browser. If unsuccessful, prompts the user to open it his/herself."""
    if sys.platform == 'win32':
        print(get_response(23))
        os.startfile(url)
    elif sys.platform == 'darwin':
        print(get_response(23))
        subprocess.Popen(['open', url])
    else:
        try:
            print(get_response(23))
            subprocess.Popen(['xdg-open', url])
        except OSError:
            get_response(7, "<url>", url)

def schedule():
    """Returns the time in seconds until a scheduled event. Interprets text from the user in standard time units

    Returns
    -------
    float
        Returns the total time in seconds until a scheduled event
    """
    global command
    time_units = collections.OrderedDict([
        ("\\bsecs?\\b|\\bseconds?\\b", 1),
        ("\\bmins?\\b|\\bminutes?\\b", 60),
        ("\\bhours?\\b", 3600),
        ("\\bdays?\\b", 86400)
    ])
    total_time = 0.0
    for key in time_units:
        occurences = re.findall(key, command)
        if occurences:
            for item in occurences:
                index = command.find(item)
                index = command.rfind(' ', 0, index - 1) + 1
                #This bit's here to ignore false positives. For example: "I'll be heading to bed in a minute, so can you shut down my computer in 2 min?"
                try:
                    num = float(command[index:(command.find(' ', index))])
                    total_time += (num * time_units[key])
                except Exception:
                    continue
    if total_time != 0:
        time_string = convert_and_format_time(total_time)
        confirm = input(get_response(8, "<time_string>", time_string)).lower()
        while True:
            if get_yes_no(confirm):
                return total_time
            elif get_yes_no(confirm, 1):
                print(get_response(9))
                break
            else:
                confirm = input(get_response(10)).lower()
    else:
        print(get_response(11))


def close_oscar():
    """Closes the program.

    This function exists due to an error in jsonpickle, in which sys.exit() is mistakenly serialized as a dictionary
    """
    sys.exit()

def convert_and_format_time(total_time):
    """Takes time in seconds as an argument, and converts it to the lowest expressable value in days/hours/minutes/seconds

    Arguments
    ---------
    total_time : float
        The total time in seconds until an event

    Returns
    -------
    String
        A string that reflects the time until an event happens in days/hours/minutes/seconds
        Ex: "2 days 5 hours 3 minutes and 10 seconds"
        Ex: "5 minutes and 30 seconds"
    """
    time_string = ""
    orig_total_time = total_time
    days = int(total_time // 86400)
    if days > 0:
        total_time -= (days * 86400)
        if days > 1:
            time_string += str(days) + " days "
        else:
            time_string += str(days) + " day "

    hours = int(total_time // 3600)
    if hours > 0:
        total_time -= (hours * 3600)
        if hours > 1:
            time_string += str(hours) + " hours "
        else:
            time_string += str(hours) + " hour "

    minutes = int(total_time // 60)
    if minutes > 0:
        total_time -= (minutes * 60)
        if minutes > 1:
            time_string += str(minutes) + " minutes "
        else:
            time_string += str(minutes) + " minute "
    seconds = float(total_time)
    if seconds > 0:
        if time_string:
            time_string += "and"
        if seconds > 1 or seconds < 1:
            time_string += " %.3f seconds" % seconds
        else:
            time_string += " 1 second"
    else:
        time_string = time_string[:len(time_string) - 1]
    return time_string

def receive_command():
    """Receives the user's command and processes the input appropriately"""
    global responses, inputs, settings, groups, firstTime, command
    if firstTime:
        responses = oscar_defaults.responses_array
        inputs = oscar_defaults.inputs_array
        settings = oscar_defaults.settings_array
        groups = oscar_defaults.groups_array
        actions.greet()
        firstTime = False
    command = input("").lower()
    contained_keyword = ""
    found_keyword = False
    for input_type in range(0, len(inputs)):
        if contained_keyword == "" and inputs[input_type][2] != 0:
            for keyword in inputs[input_type][0]:
                if re.search(keyword, command):
                    contained_keyword = keyword
            if contained_keyword != "" and len(inputs[input_type][1]):
                for antiword in inputs[input_type][1]:
                    if re.search(antiword, command):
                        contained_keyword = ""
        if contained_keyword != "":
            found_keyword = True
            inputs[input_type][2]()
            break
    if not found_keyword:
        print(get_response(16))
