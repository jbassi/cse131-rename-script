import os
import shutil

PHASE     = ''          # Leave blank to search all files and folders or only folders with phaseX/.
CHECK     = ''          # Leave blank to search all files and folders or only folders with checkX/.
PATH      = ''          # Set this to the root of your testcases. EX: /Users/jbassi/CSE131/testcases
OUTPUT    = '/output'   # Do not modify this.
CLEAN_DIR = False       # Set this to true if you want to remove any files not ending in .ans.out or .rc.

def main():
  global PATH
  if PATH == '':
    print 'Please specify the path to your testcases/ folder.'
    return
  if not PATH.endswith('/'):
    PATH += '/'

  for subdir, dirs, files in os.walk(PATH):
    if (PHASE == '' and CHECK == '') or PHASE + '/' + CHECK in subdir:
      print 'Looking for files in: ', subdir
      # Create temporary directory to store modified output files in.
      if not os.path.exists(subdir + OUTPUT):
        os.makedirs(subdir + OUTPUT)

      for filename in files:
        if '.out' in filename:
          with open (subdir + '/' + filename, 'r') as file:
            # Get the part of the filename before the first dot.
            filenamePrefix = filename[0:filename.find('.')]
            # Create a new file ending in .ans.out.
            with open(os.path.join(subdir + OUTPUT, filenamePrefix + '.ans.out'), 'w') as target:
              for line in file:
                # If the original output file has 'Error, ' in it, replace the file path.
                if 'Error,' in line.strip():
                  pathName = subdir + '/' + filenamePrefix + '.rc'
                  target.write('Error, "' + pathName.replace(PATH, '') + '": \n')
                else:
                  target.write(line)

        if CLEAN_DIR and (not filename.endswith('.ans.out')) and (not filename.endswith('.rc')):
          # Remove any files from the directory that do not end in .ans.out and .out.
          os.remove(subdir + '/' + filename)

      # Copy all files in tempory directory back out to original path.
      for filename in os.listdir(subdir + OUTPUT):
        shutil.copy(subdir + '/' + OUTPUT + '/' + filename, subdir)

      # Remove temporary directory.
      shutil.rmtree(subdir + '/' + OUTPUT, ignore_errors=True)

if __name__ == '__main__':
  main()
