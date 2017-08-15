from datetime import date,datetime
import urllib.request
import json
import re
import socket
import ssl

def sort_list(l):
    """Takes a list and returns a sorted version"""
    l.sort()
    return l


def rgb_to_hex(red, green, blue):
    """
    Convert red, green, blue values into a HTML hex representation
    The short syntax should (#fff) be used where possible.
    """
    hex_long = '#%02x%02x%02x' % (red, green, blue)
    reg_exp = re.compile(r'#([0-9a-f])\1([0-9a-f])\2([0-9a-f])\3')
    if reg_exp.match(hex_long):
        h1, h2, h3 = hex_long[1], hex_long[3], hex_long[5]
        hex_short = '#{0}{1}{2}'.format(h1, h2, h3)
        return hex_short
    else:
        return hex_long

def get_github_members(org_name):
    """
    Get the number of (public) members belonging to the specified Github
    organisation
    """
    u = urllib.request.urlopen('https://api.github.com/orgs/{0}/public_members'.format(org_name))
    #counts the number of json objects
    num_public_members = (len(json.load(u)))
    return num_public_members


def get_ssl_expiry(domain):
    """
    Takes a domain and returns a date that represents when the SSL certificate
    will expire.
    """
    date_list = []
    ssl_date_fmt = r'%Y, %m, %d'
    ssl_datetime_fmt = r'%b %d %H:%M:%S %Y %Z'

    context = ssl.create_default_context()
    conn = context.wrap_socket(
        socket.socket(socket.AF_INET),
        server_hostname = domain,
    )
    # 3 second timeout because Lambda has runtime limitations
    conn.settimeout(3.0)

    conn.connect((domain, 443))
    ssl_info = conn.getpeercert()
    # parse the string from the certificate into a Python datetime object
    datetime_object = datetime.strptime(ssl_info['notAfter'], ssl_datetime_fmt)
    #print(datetime.date.strftime(datetime_object, ssl_date_fmt))
    s = date.strftime(datetime_object, ssl_date_fmt)
    conn.close()

    #converting the date string to int and storing it in a list
    for i in s.split(','):
        date_list.append(int(i))

    return date(date_list[0],date_list[1],date_list[2])
