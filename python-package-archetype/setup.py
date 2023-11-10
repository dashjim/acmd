from setuptools import setup, find_packages

setup(
    name='acbr',
    packages=find_packages(),
    version='0.5',
    description='This acbr package (named after AwsCliBedRock) automatically generates and run aws-cli commands using AWS Bedrock models.',
    author='Junxiang Ji',
    author_email='junxiang.ji@qq.com',
    url='https://github.com/DEV3L/python-package-archetype',
    download_url='https://github.com/DEV3L/python-package-archetype/tarball/0.4',
    keywords=['aws-cli', 'Bedrock'],  # arbitrary keywords
    install_requires=[
        'pytest>=2.9.2',
        'requests',
		'boto3>=1.16.59'
    ],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'],
    entry_points={
        'console_scripts': [
            'acbr = acbr.cli-reactor:invoke'
        ]},
)
