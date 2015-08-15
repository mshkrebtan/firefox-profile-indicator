# Firefox Profile Indicator

As a way of indicating which Firefox profile is currently in use I wrote some [userChrome.css](https://developer.mozilla.org/en-US/docs/Mozilla/Tech/XUL/Tutorial/Modifying_the_Default_Skin) rules which altered the background colour of the tab bar and add some text to any profile.

![Screenshot](http://i.imgur.com/fvpAgRo.png)

## Usage
If you clone/download this repository you can run the <code>indicate.py</code> script and it will walk you through specifying a profile, text and colour to use before copying the rules into your profile automatically.

Alternatively you can add the CSS rules manually by copying userChrome.css into the [<code>chrome</code> folder](http://kb.mozillazine.org/Chrome_folder) inside a Firefox profile. If the file already exists then just copy the rules from my file to the bottom of yours. Change the the <code>content: "";</code> property to add text to the far right of the tab bar and the <code>background: ;</code> property to specify a background colour to be used.

Lighter colours seems to work best but you could tweak the text colour and other elements to make a darker colour blend in better. Also the 'padding-right: ;' property stops the tabs from overlapping the text when you open too many so if you want a long text string you may need to increase this value.

## Known Issues
Currently the script is hardcoded to look for Firefox profiles inside the <code>~/.mozilla/firefox</code> and so will probably only work for Linux systems. You can easily change this string to point to your profiles' location.
