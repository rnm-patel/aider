from distutils.core import setup

# reading requirements.txt file for install_requires field
packages = []
with open('requirements.txt') as fp:
    for line in fp:
        line = line.replace(',', '').strip()
        if line.startswith('#'): continue
        if line != '': packages.append(line)

setup(
    name = 'aider',         
    packages = ['aider'],
    version = '0.2.1',      
    license='MIT',        
    description = 'general utilities',     
    long_description = open('README.rst').read(),
    author = 'Rajat Movaliya',              
    author_email = 'rajatmovaliya@gmail.com',     
    url = 'https://github.com/rnm-patel/aider',  
    download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',
    keywords = ['utility', 'generic', 'log', 'config', 'calendar'],
    include_package_data=True,
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