from setuptools import setup

setup(name='nephelae_master',
      version='0.1',
      description='Metapackage with all modules from LAAS dev for Nephelae project',
      url='ssh://git@redmine.laas.fr/laas/users/simon/nephelae/nephelae-devel/nephelae_master.git',
      author='Pierre Narvor',
      author_email='pnarvor@laas.fr',
      licence='bsd2',
      packages=['nephelae_base', 'nephelae_simulation', 'nephelae_paparazzi'],
      zip_safe=False)


