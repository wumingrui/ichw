Python 3.6.3 (v3.6.3:2c5fed86e0, Oct  3 2017, 00:32:08) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> """wcount.py: count words from an Internet file.

__author__ = "Wu Mingrui"
__pkuid__  = "1700011806"
__email__  = "1919460265@qq.com"
"""
'wcount.py: count words from an Internet file.\n\n__author__ = "Wu Mingrui"\n__pkuid__  = "1700011806"\n__email__  = "1919460265@qq.com"\n'
>>> import sys
>>> from urllib.request import urlopen
>>> def wcount(lines, topn=10):
	"""count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
	lines.lower()
	lines.replace(","," ")
	lines.replace("."," ")
	whole={}
	lst=lines.split()
	for i in lst:
		num=0
		for j in lst:
			if i==j:
				num=num+1
		whole[i]=num
	answer=sorted(whole.items(),key=lambda kv:kv[1],reverse=True)
	for i in range(0,topn):
		print(answer[i][0],"\t",answer[i][1])
	pass

>>> if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines   = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)

        
Usage:  url [topn]
  url: URL of the txt file to analyze 
  topn: how many (words count) to output. If not given, will output top 10 words
>>> 
