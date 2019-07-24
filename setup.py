from setuptools import setup, find_packages

setup(name='nephelae_master',
      version='0.1',
      description='Metapackage with all modules from LAAS dev for Nephelae project',
      url='ssh://git@redmine.laas.fr/laas/users/simon/nephelae/nephelae-devel/nephelae_master.git',
      author='Pierre Narvor',
      author_email='pnarvor@laas.fr',
      licence='bsd2',
      packages=find_packages(include=['nephelae_base*', 'nephelae_simulation*', 'nephelae_paparazzi*','nephelae_mapping']),
      install_requires=[
        'numpy',
        'scipy',
        'netCDF4',
        'utm',
        'ivy-python',
        'matplotlib',
        'scikit-learn',
        'sh'
      ],
      zip_safe=False)


