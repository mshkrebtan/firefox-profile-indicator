#!/usr/bin/python

import sys
import os
from os import listdir
from os.path import isdir, join, expanduser
import re

def main():
    try:
        input = raw_input
    except NameError:
        pass

    firefox_dir = expanduser("~") + "/.mozilla/firefox"

    profiles = get_profiles(firefox_dir);

    for i, name in enumerate(profiles):
        print "(" + str(i + 1) + ") " + name

    profile = int(input("Select profile: "))
    if profile > 0 and profile < len(profiles) + 1:
        profile = profiles[profile - 1]
    else:
        print "Error"
        sys.exit(1)

    profile_name = extract_profile_name(profile)

    text = input("Indicator text (" + profile_name + "): ")
    if text == "":
        text = profile_name

    color = input("Indicator color: ")
    if color == "":
        print "Error"
        sys.exit(1)

    indicate(firefox_dir, profile, text, color)

def indicate(firefox_dir, profile_name, text, color):
    css_filepath = os.path.dirname(os.path.realpath(sys.argv[0])) + "/userChrome.css"
    with open (css_filepath, "r") as myfile:
        css = myfile.read().replace("\n", "")

    css = css.replace("\"Text\"", "\"" + text + "\"")
    css = css.replace("skyblue", color)

    user_chrome_filepath = firefox_dir + "/" + profile_name + "/chrome/userChrome.css"

    write_method = "a"
    if not os.path.isfile(user_chrome_filepath):
        write_method = "w"

    with open(user_chrome_filepath, write_method) as user_chrome:
        user_chrome.write(css)

    print "CSS rules written to:", user_chrome_filepath

def extract_profile_name(profile):
    profile_pattern = re.compile("^\w*\.(\w*)$")
    return profile_pattern.search(profile).group(1)

def get_profiles(firefox_dir):
    profile_pattern = re.compile("^\w*\.(\w*)$")
    profile_dirs = [ d for d in listdir(firefox_dir) if isdir(join(firefox_dir, d)) and profile_pattern.match(d) ]
    return profile_dirs

if __name__ == "__main__":
    main()
