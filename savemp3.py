#enter youtube URL and creates exe to create mp3

from subprocess import Popen, PIPE
url = raw_input('Enter URL: ')

fromfile = open('/users/matthewschwartz/SaveMp3/SaveMP3')
indata = fromfile.read()
tofile = open('/users/matthewschwartz/SaveMp3/newmp3', 'w')
tofile.write(indata)
tofile.write(url)
fromfile.close()

def subprocess_cmd(dr, cmd1, cmd2):
    p1 = Popen(cmd1.split(),stdout=PIPE,cwd=dr)
    p2 = Popen(cmd2.split(),stdin=p1.stdout,stdout=PIPE,cwd=dr)
    p1.stdout.close()
    return p2.communicate()[0]
subprocess_cmd('/Users/matthewschwartz/SaveMp3','open -a Terminal', 'chmod 700 newmp3')
