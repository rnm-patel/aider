from distutils.core import setup

name = 'utils'

# reading readme flie for assigning it as long description
text = ''
with open('README.md') as fp:
    text = fp.read()

# reading requirements.txt file for install_requires field
packages = []
with open(name + '/requirements.txt') as fp:
    for line in fp:
        line = line.strip()
        if line.startswith('#'): continue
        packages.append(line)

setup(
    name = name,         
    packages = ['utils'],
    version = '0.1',      
    license='MIT',        
    description = 'general utilities',     
    long_description = text,
    author = 'Rajat Movaliya',              
    author_email = 'rajatmovaliya@gmail.com',     
    url = 'https://github.com/user/reponame',  
    download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',
    keywords = ['utility', 'generic', 'log', 'config', 'calendar'],
    install_requires=packages,
    classifiers=[
        'Development Status :: 3 - Alpha',   
        'Intended Audience :: Developers',      
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License', 
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)