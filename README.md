# DiscourseMarker


Python script to detect Discourse Markers.

*A very very naive way to detect the presence of Discourse Markers/Connectives using a rule-based regex matching.*


### How to run

The script requires input in the form of a parse tree(s) from Stanford parser.

* Put the parse tree in the input file - "rules" from the Stanford parser.
* Delimit using "<<".
* Run the script
 
```sh
$ python reader.py
```

* Output is in the form of a list of DMs.


### Extra

* reader.py is the cleaned version with the output in the clean and correct manner.
* reader.py.bak is the dirty version with all the uneccessary print commands and comments. Run at your own risk. :P
