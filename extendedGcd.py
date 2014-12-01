def exgcd(m,n):
	x=x1=y0=0  #x0=1,x1=0
	y=x0=y1=1   #t0=0,t1=1, these four variable to update x,y,which mx+ny=1
                        
	r = m % n   # r is the mod
	q = (m-r)/n  #q is the quotient
	 
	while(r!=0):  #termination condition

                #x(i+1) = x(i-1)-q*x(i)
                #y(i+1) = y(i-1)-q*y(i)
		x = x0-q*x1
		y = y0-q*y1
		x0=x1
		y0=y1
		x1=x
		y1=y

                #normal gcd, gcd(m,n) = gcd(n,m%n)
		m=n
		n=r
		r=m%n
		q=(m-r)/n
	return n,x,y

if __name__=="__main__":
	print exgcd(35,25)
