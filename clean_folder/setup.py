from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1',
    description='Сортує задану папку- перевіряє внутрішні вкладення/ Форматує утворюючи нові папки і розархивовує архіви, також переіменовує.',
    url='',
    author='Flying Circus',
    author_email='flyingcircus@example.com',
    license='MIT',
    packages=find_namespace_packages(),
    install_requires=['markdown'],
    entry_points={'console_scripts': ['helloworld = useful.some_code:hello_world']}
)