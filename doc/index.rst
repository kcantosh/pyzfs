.. pyzfs documentation master file, created by
   sphinx-quickstart on Mon Feb 10 15:14:35 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to PyZFS's documentation!
=================================

**PyZFS** is an MPI-parallelized Python code for the first-principles calculation of the spin-spin zero-field-splitting (ZFS) tensor based on wavefunctions obtained from density functional theory (DFT) calculations.

**PyZFS** can work with wavefunctions generated by various plane-wave pseudopotential DFT codes including **Quantum Espresso** (https://www.quantum-espresso.org/) and **Qbox** (http://qboxcode.org/). **PyZFS** also supports the standard cube file format. **PyZFS** computes the spin-spin ZFS tensor from normalized pseudo-wavefunctions without projected-augmented-wave type corrections and is designed to be scalable to large calculations. For instance, **PyZFS** has been applied to study spin-defects in semiconductors using supercells containing thousands of valence electrons.

--------

.. toctree::
   :hidden:
   :maxdepth: 2

   installation
   tutorial
   documentation

.. glossary::

   :ref:`installation`
      Instructions on how to install the **PyZFS** package.
   
   :ref:`tutorial`
      Demonstration of usage of **PyZFS** with wavefunctions from various DFT codes.
   
   :ref:`documentation`
      Detailed documentation of the **PyZFS** package.

