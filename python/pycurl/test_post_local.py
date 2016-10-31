import pycurl
import datetime
# --------- upload_file.py ----------------
# upload binary file with pycurl by http post
for index in xrange(10):
    break
    c = pycurl.Curl()
    c.setopt(c.POST, 1)
    c.setopt(c.URL, "http://0.0.0.0:5001/api/receive")
    # c.setopt(c.URL, "http://0.0.0.0:5001/importfile/")
    # c.setopt(c.HTTPPOST, [("uploadfile", (c.FORM_FILE, "./data.txt"))])
    c.setopt(c.HTTPPOST, [('uploadfile', (pycurl.FORM_CONTENTS, 'data.txt'))])
    c.setopt(c.VERBOSE, 1)
    c.perform()
    c.close()
    print "that's it ;)"
    break
    
"""
pf = [('field1', 'this is a test using httppost & stuff'),
      ('field2', (pycurl.FORM_FILE, 'test_post.py', pycurl.FORM_FILE, './data.txt')),
      ('uploadfile', (pycurl.FORM_CONTENTS, 'this is wei\000rd, but null-bytes are okay'))
     ]
pf = [('field1', 'this is a test using httppost & stuff'),
      ('field2', (pycurl.FORM_FILE, './nohup.out', pycurl.FORM_FILE, './data.txt'))
     ]
"""
content = open("./data.txt","r").read()
pf = [('filename','data.txt'),('uploadfile', (pycurl.FORM_CONTENTS, content)) ]
  
c = pycurl.Curl()
c.setopt(c.POST, 1)
c.setopt(c.URL, "http://0.0.0.0:5001/api/receive")
c.setopt(c.HTTPPOST, pf)
c.setopt(c.VERBOSE, 1)
c.perform()
c.close()
print 'all over'
        


