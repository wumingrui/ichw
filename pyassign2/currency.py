Python 3.6.3 (v3.6.3:2c5fed86e0, Oct  3 2017, 00:32:08) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> from urllib.request import urlopen
>>> def exchange(currency_from, currency_to, amount_from):
    """Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in 
    currency currency_from to the currency currency_to. The value 
    returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""
    amount_from=str(amount_from)
    l=len(amount_from)
    web="http://cs1110.cs.cornell.edu/2016fa/a1server.php?from="+currency_from+"&to="+currency_to+"&amt="+amount_from
    doc = urlopen(web)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    k=len(jstr)
    no1=""
    no=["1","2","3","4","5","6","7","8","9","0","."]
    for i in range(k):
        if jstr[i] in no:
            no1=no1+jstr[i]
    result=float(no1[l:])
    return result

>>> def test():
    """Used to test if the exchange function works.Considering that the currency exchange
    rate varies in different time periods, we have to import the exchange function twice，
    cutting off the test errors caused by rate changes.
    In the test function, we first calculate exchange("USD","EUR",1), then exchange("EUR,
    "USD",1). If the two return values can get a product equals to 1，then we can saythat
    the exchange function is very likely to work well."""
    a=exchange("USD","EUR",1)
    b=exchange("EUR","USD",1)
    if (a*b-1)<0.00001:
        print("Function exchange passed the text program.")
    else:
        print("Function exchange failed to pass the text program.")

>>> test()
Function exchange passed the text program.
>>> 
