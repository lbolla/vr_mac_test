import setuptools

setup_params = dict(
    name='vr_mac_test',
    version='0.1',
    author="Lorenzo Bolla",
    author_email="lbolla@gmail.com",
    py_modules=['main']
)

if __name__ == '__main__':
    setuptools.setup(**setup_params)
