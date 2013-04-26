import requests
import json

username = 'kixeye'
password = 'kixeye'

""" A test of the game support system.

If this were going into production, I would use an actual test-runner (nose, eg)
and the 'print' statements would be using the logging module.
"""

def test_auth():
    print 'GET http://localhost:8000/users'
    print '(should fail without login)'
    r = requests.get('http://localhost:8000/users')
    print 'Response: %s' % (r.text,)
    print '=' * 60

def test_list_users():
    print 'GET http://localhost:8000/users user=kixeye, pass=kixeye'
    r = requests.get('http://localhost:8000/users', auth=(username, password))
    print 'Response: %s' % (r.text,)
    print '=' * 60

def test_create_user():
    print 'POST http://localhost:8000/users'
    payload = {'first_name': 'Will', 'last_name':'Harbin', 'nickname':'da_boss'}
    url = 'http://localhost:8000/users/'
    headers = {'content-type': 'application/json'}
    r = requests.post(
        url,
        data=json.dumps(payload),
        auth=(username, password),
        headers=headers
    )
    print 'Response: %s' % (r.text,)
    print '=' * 60

def test_create_battle():
    print 'POST http://localhost:8000/battles/'
    payload = {
        'attacker': 1,
        'defender': 2,
        'winner': 2,
    }
    url = 'http://localhost:8000/battles/'
    headers = {'content-type': 'application/json'}
    r = requests.post(
        url,
        data=json.dumps(payload),
        auth=(username, password),
        headers=headers
    )
    print 'Response: %s' % (r.text,) 
    print '=' * 60

if __name__ == '__main__':
    test_auth()
    test_list_users()
    test_create_user()
    test_create_battle()
