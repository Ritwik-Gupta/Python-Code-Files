Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def mystery(l):
	if l == []:
		return(l)
	else:
		return(l[-1:] + mystery(l[:-1]))
