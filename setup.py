from setuptools import setup

setup(
    name='IPSearchApp',
    version='1.0',
    packages=[''],
    url='https://github.com/cadeatkins/search',
    license='MIT',
    author='Your Name',
    author_email='your-email@example.com',
    description='IP Search App',
    install_requires=[
        'pandas',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    entry_points={
        'console_scripts': [
            'ipsearchapp = search:main',
        ],
    },
)
