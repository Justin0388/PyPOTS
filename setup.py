from setuptools import setup, find_packages

from pypots.__version__ import version

with open('./README.md', encoding='utf-8') as f:
    README = f.read()

setup(
    name='pypots',
    version=version,
    description='A Python Toolbox for Data Mining on Partially-Observed Time Series',
    long_description=README,
    long_description_content_type='text/markdown',
    license='GPL-3.0',
    author='Wenjie Du',
    author_email='wenjay.du@gmail.com',
    url='https://github.com/WenjieDu/PyPOTS',
    download_url='https://github.com/WenjieDu/PyPOTS/archive/master.zip',
    keywords=[
        'data mining', 'neural networks', 'machine learning', 'deep learning',
        'partially observed', 'time series', 'missing data', 'missing values',
    ],
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=[
        'matplotlib',
        'numpy',
        'scikit_learn',
        'scipy',
        'torch>=1.10',  # torch_sparse v0.6.13 needs torch>1.9
        'torch_sparse',
        'torch_scatter',
        'tensorboard',
        'pandas',
        'pycorruptor',
        'tsdb',
        'pyg'

    ],
    setup_requires=['setuptools>=38.6.0'],
)
