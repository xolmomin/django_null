from base64 import b64encode, b64decode

with open('python-logo.png', 'rb') as f:
    t = b64encode(f.read()).decode('utf-8')
