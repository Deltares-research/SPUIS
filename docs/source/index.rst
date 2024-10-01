SPUIS documentation
===================================

This is the documentation for **SPUIS**, a 1D `Deltares <https://www.deltares.nl/>`_ tool for calculating water levels and flow velocities in discharge sluices. SPUIS can be applied to both open channel flow and closed-off culverts. SPUIS was originally developed by Delft Hydraulics in 1986 [1]_ and updated in 1989 [3]_ and 1995 [4]_. The latter version was converted from the original Fortran code to the currently available Python code in 2024 and contains the same functionality as version SPUIS 4.01 from 1995. 

The implementation of SPUIS was tested by comparison with measurements from physical scale model tests of discharge sluices Dintelsas and Crèvecoeur in the Netherlands [1]_. In the past, SPUIS has been applied to support the design of hydraulic structures, such as pumping station Oosterhout (1995) [4]_, discharge sluice Nieuwe Statenzijl [2]_, and discharge sluice Brouwersdam (2018) [4]_ in the Netherlands.

The SPUIS documentation covers the following topics:
    - The theory on which SPUIS is based,
    - An example calculation,
    - A tutorial for setting up a SPUIS schematization,
    - Instructions for running SPUIS on your computer,
    - An overview of the Python code and the functionality of each subroutine.

.. note::

   SPUIS is based on the Dutch word "spuisluis", meaning "discharge sluice" or "sluice gate" in English.

.. [1] WL | Delft Hydraulics (1986). ‘Berekening van de afvoer van spuisluizen met behulp van een rekenmodel.’ Report R2125.
.. [2] WL | Delft Hydraulics (1987). ‘Sluiscomplex Nieuwe Statenzijl - Hydraulische aspecten van de schut- en spuisluis.’ Report Q0485.
.. [3] WL | Delft Hydraulics (1989). ‘Berekening van de afvoer van spuisluizen bij schietend water situaties.’ Report Q0331.
.. [4] WL | Delft Hydraulics (1995). ‘Aflaatwerk en gemaal te Oosterhout.’ Report Q1952.
.. [5] Deltares (2018). ‘Bepaling afvoercoëfficiënt doorlaatmiddel Brouwersdam.’ Report 11202901-002-ZKS-0002.
