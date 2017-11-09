from subprocess import Popen, PIPE
import shutil
#import base64
url = raw_input('Enter URL: ')
#name = raw_input('What is this?:')
fromfile = open('/users/matthewschwartz/livestream/livestream')
indata = fromfile.read()
tofile = open('/users/matthewschwartz/livestream/newstream', 'a')
tofile.write(indata)
tofile.write( url)
tofile.write(' best')
fromfile.close()
#name = base64.urlsafe_b64encode(name)
def subprocess_cmd(dr, cmd1, cmd2):
    p1 = Popen(cmd1.split(),stdout=PIPE,cwd=dr)
    p2 = Popen(cmd2.split(),stdin=p1.stdout,stdout=PIPE,cwd=dr)
    p1.stdout.close()
    return p2.communicate()[0]
subprocess_cmd('/Users/matthewschwartz/livestream','open -a Terminal', 'chmod 700 newstream')
#shutil.copyfile('/Users/matthewschwartz/livestream/newstream','/Users/matthewschwartz/livestream/changethisname ')
