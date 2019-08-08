from setuptools import setup, find_packages
import os
import sh

path = os.path.dirname(os.path.abspath(__file__))
command = sh.Command("cd  " + path + "&& git submodule init && git submodule update")
process = command()
process.wait()

# setup(name='nephelae_master',
#       version='0.2.1',
#       description='Metapackage with all modules from LAAS dev for Nephelae project',
#       url='ssh://git@redmine.laas.fr/laas/users/simon/nephelae/nephelae-devel/nephelae_master.git',
#       author='Pierre Narvor',
#       author_email='pnarvor@laas.fr',
#       licence='bsd2',
#       packages=find_packages(include=['nephelae_base*', 'nephelae_simulation*', 'nephelae_paparazzi*','nephelae_mapping*']),
#       install_requires=[
#         'numpy',
#         'scipy',
#         'netCDF4',
#         'utm',
#         'ivy-python',
#         'matplotlib',
#         'scikit-learn',
#         'sh'
#       ],
#       zip_safe=False)


