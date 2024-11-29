SPUIS
===================================

This is the documentation for **SPUIS**, a 1D `Deltares <https://www.deltares.nl/>`_ tool for calculating water levels and flow velocities in discharge sluices. SPUIS can be applied to both open channel flow and culverts. SPUIS was originally developed by Delft Hydraulics in 1986 [1] and updated in 1989 [3] and 1995 [4]. The latter version was converted from the original Fortran code to the currently available Python code in 2024 (SPUIS 4.02) and contains the same functionality as version SPUIS 4.01 from 1995. 

.. note::

   SPUIS is based on the Dutch word "spuisluis", meaning "discharge sluice" or "sluice gate" in English.

The implementation of SPUIS was tested by comparison with measurements from physical scale model tests of discharge sluices Dintelsas and Crèvecoeur in the Netherlands [1]. In the past, SPUIS has been applied to support the design of hydraulic structures, such as the discharge sluice in Nieuwe Statenzijl (1987) [2], Oosterhout (1995) [4], and the Brouwersdam (2018) [5] in the Netherlands.

.. toctree::
   :maxdepth: 1
   :caption: Contents

   theory 
   getting-started
   tutorial   
   examples
   code
   support

Literature
-----------
* [1] WL | Delft Hydraulics (1986). ‘Berekening van de afvoer van spuisluizen met behulp van een rekenmodel.’ Report R2125.
* [2] WL | Delft Hydraulics (1987). ‘Sluiscomplex Nieuwe Statenzijl - Hydraulische aspecten van de schut- en spuisluis.’ Report Q0485.
* [3] WL | Delft Hydraulics (1989). ‘Berekening van de afvoer van spuisluizen bij schietend water situaties.’ Report Q0331.
* [4] WL | Delft Hydraulics (1995). ‘Aflaatwerk en gemaal te Oosterhout.’ Report Q1952.
* [5] Deltares (2018). ‘Bepaling afvoercoëfficiënt doorlaatmiddel Brouwersdam.’ Report 11202901-002-ZKS-0002.
