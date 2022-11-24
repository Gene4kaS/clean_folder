from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1',
    description='Сортує задану папку- перевіряє внутрішні вкладення/ Форматує утворюючи нові папкиcd і розархивовує архіви, також переіменовує.',
    url='https://github.com/Gene4kaS/clean_folder',
    author='Gene4kaS',
    author_email='',
    license='MIT',
    packages=find_namespace_packages(),    
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']}
)