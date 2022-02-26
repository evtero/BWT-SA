
##################### BTW from BWM #####################

def get_rotations(t):
	'''
	Returns all rotations of text (list output)
	'''
	rotations = [t]
	for i in range(0,len(t)-1):
		last = t[len(t)-1]
		bigpref = t[:-1]
		r = last + bigpref 
		rotations.append(r)
		t = r
	return rotations

def get_bwm(t):
	'''
	Returns Burrows-Wheeler Matrix (list output)
	'''
	return sorted(get_rotations(t))

def bwm2btw(t):
	'''
	Returns Burrows-Wheeler Transform from BWM (string output)
	'''
	bwt = ''.join([x[len(x)-1] for x in get_bwm(t)])
	return bwt

##################### BTW from SA #####################

def get_sa_bf(t):
	'''
	Returns Suffix Array by brute force (list output)
	'''
	sa = {t:0}
	for i in range(len(t)-1,0,-1):
		sa[t[i:len(t)]] = i 
	sa = sorted(sa.items())
	return list(list(zip(*sa))[1])

def sa2btw(t,sa):
	'''
	Returns Burrows-Wheeler Transform from SA (string output)
	'''
	btw = ''
	for i in range(len(t)):
		if sa[i] > 0:
			btw += t[sa[i]-1]
		else:
			btw += '$'
	return btw


##################### Memory efficient SA  #####################

def get_first_buckets(t):
	'''
	Returns first level of buckets (list of tuples output)
	'''
	buckets = dict()
	for i in range(0,len(t)):
		buckets[t[i]] = buckets.get(t[i], []) + [i]
	return sorted(buckets.items())

def get_buckets(bucket,t):
	'''
	Returns next level of buckets from one bucket (list of tuples output)
	e.g. bucket ('A', [0, 8, 12]) 
	'''
	l = len(bucket[0])*2
	d = dict()
	for i in bucket[1]:
		if (i+l) > len(t):
			prefix = t[i:len(t)] # special case last chars
		else:
			prefix = t[i:i+l]
		d[prefix] = d.get(prefix,[]) + [i]
	return sorted(d.items())

def get_sa(buckets_group,t,sa):
	'''
	Recursive function to generate Suffix Array from each buckets group (list output)
	'''
	for bucket in buckets_group:
		if len(bucket[1]) != 1:
			next_buckets = get_buckets(bucket,t)
			get_sa(next_buckets,t,sa)
		else:
			sa.append(bucket[1][0])
	return sa

def sa_prefix_doubling(t):
	'''
	Main function
	Returns Suffix Array that is generated recursively (list output)
	'''
	buckets_group = get_first_buckets(t)
	sa = []
	sa = get_sa(buckets_group,t,sa)
	return sa



