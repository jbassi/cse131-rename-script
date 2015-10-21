This script aims to make test cases usable with the YUNO testing framework (https://github.com/bulatb/yuno) for CSE 131. This script goes through each directory recursively (from your specified PATH) looking for incorect output of the form "Error, " and replaces this line with the corect path so yuno can correctly diff the files. 

An example of this would be the following:

Output from testrunner_client on ieng9 with a file named c00.rc:  
Error, "/tmp/cs131_testrunner_kWPqMF/file.rc":  
&nbsp;&nbsp;&nbsp;&nbsp;Initialization value of type float not assignable to constant/variable of type int.  
Error, "/tmp/cs131_testrunner_kWPqMF/file.rc":  
&nbsp;&nbsp;&nbsp;&nbsp;Initialization value of type float not assignable to constant/variable of type int.  
Compile: failure.

After running the script where the output is in phase2/check12/c00.rc:  
Error, "phase2/check12/c00.rc":  
&nbsp;&nbsp;&nbsp;&nbsp;Initialization value of type float not assignable to constant/variable of type int.  
Error, "phase2/check12/c00.rc":  
&nbsp;&nbsp;&nbsp;&nbsp;Initialization value of type float not assignable to constant/variable of type int.  
Compile: failure.

Modify the following to your liking:  
PHASE = '' # Leave blank to search all files and folders or only folders with phaseX/.  
CHECK = '' # Leave blank to search all files and folders or only folders with checkX/.  
PATH = '' # Set this to the root of your testcases. EX: /Users/jbassi/CSE131/testcases  
CLEAN_DIR = False # Set this to true if you want to remove any files not ending in .ans.out or .rc in your directories.

To run: `python rename.py` from the command line.
