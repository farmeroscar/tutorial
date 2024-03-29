# This is example code 
#for use with the Wing tutorial, which
# is accessible from the Help menu of the IDE

# NOTE: This code is incomplete and contains deliberate errors 
# to illustrate features when working through the tutorial

import os
import sys
import stat
import time
if sys.hexversion >= 0x03000000:
  from urllib import request
else:
  import urllib

# NOTE:  This import will not work unless you follow the directions
# in the tutorial to set your PYTHONPATH
from path_example import ParseRDFNews, kCannedData

  

#----------------------------------------------------------------------
def PromptToContinue(msg="Press Enter to Continue: "):
  """Prompt to continue and wait for the user to press Enter"""
  if sys.hexversion >= 0x03000000:
    x = input(msg)
  else:
    x = raw_input(msg)
  
#-----------------------------------------------------------------------
def GetItemCount():
  """This gets the number of items to use in this example"""
  return 5

#-----------------------------------------------------------------------
def ReadPythonNews(count, force=0):
  """Read news from planet.python.org news channel"""

  newscache = 'newscache.rdf'


  txt = None
  if not force and os.path.exists(newscache):    
      mtime = os.stat(newscache).st_mtime
      duration = time.time() - mtime
      if duration < 60 * 60 * 24:
        f = open(newscache, 'rb')
        txt = f.read()
        f.close()
      
  if txt is None:
    try:
      if sys.hexversion >= 0x03000000:
        svc = request.urlopen("http://planet.python.org/rss20.xml")
      else:
        svc = urllib.urlopen("http://planet.python.org/rss20.xml")
      txt = svc.read()
      svc.close()
    except:
      return kCannedData
    f = open(newscache, 'wb')
    f.write(txt)
    f.close()
      
  if len(txt) == 0:
    return []

  news = ParseRDFNews(txt)
  
  return news[:count]
  
#-----------------------------------------------------------------------
def PrintAsText(news):
  """Print Python news in plain text format"""
  
  for data, event, url in news:
    print("%s -- %s (%s)" % (data, event, url))
    #testvar
   
#-----------------------------------------------------------------------
def PrintAsHTML(news):
  """Print Python news in simple HTML format"""
  
  for date, event, url in news:
    # NOTE: The line below contains a deliberate typo
    print('<p><i>%s</i> <a href="%s">%s</a></p>' % (date, url, event))
    

##########################################################################
# Enter code according to the tutorial here:

news = ReadPythonNews(GetItemCount())
PrintAsText(news)
#PromptToContinue()
PrintAsHTML(news)

