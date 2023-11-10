from setuptools import setup, find_packages

setup(
    name='acmd',
    packages=find_packages(),
    version='0.1.0',
    description='This package automatically generates and run aws-cli commands using AWS Bedrock models. Example usage: "# acmd list all by s3 buckets"',
    author='Junxiang Ji',
    author_email='junxiang.ji@qq.com',
    url='https://github.com/DEV3L/python-package-archetype',
    download_url='https://github.com/DEV3L/python-package-archetype/tarball/0.4',
    keywords=['aws-cli', 'Bedrock'],  # arbitrary keywords
    install_requires=[
        'pytest==2.9.2',
        'requests',
		'boto3==1.16.59'
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
            'acmd = aws_cli_bedrock.cli_creactor:invoke'
        ]},
)
