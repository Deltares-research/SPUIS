.. |br| raw:: html

   <br />

.. _background:

Background
===========

Application
-----------
The **SPUIS** program was originally developed by the Waterloopkundig Laboratorium in 1986 [1]_ and updated in 1989 [2]_ and 1995 [3]_. The current Python module of SPUIS contains the functionality of the SPUIS 4.01 version of 1995 [3]_ after conversion from Fortran to Python. 

SPUIS calculates water levels and cross-sectional average flow velocities in sluices or hydraulic structures with a free water surface. Different components can be schematized in a chain of elements, for example with an upstream supply channel with a flow contraction, followed by a downstream part with a diffuser. Calculations can also be made for pipes, culverts, etc., without a free water surface. Control structures (e.g., submerged or non-submerged gates, spillways, doors, and flaps) may be present in the watercourse. The user must specify the flow-carrying cross-sections. The calculations assume steady flow. The flow can be subcritical or supercritical. In situations with a free water surface, transitions from subcritical to supercritical flow (with the transition being the critical, discharge-determining cross-section) and from supercritical to subcritical flow (transition via a hydraulic jump, whether or not submerged) can be computed.

The watercourse is divided into sections by a series of sequential cross-sections. Between the cross-sections, water surface profiles are calculated using the step method or backwater curves in the case of a free water surface. The roughness of the bed and walls is the key variable here. Changes in the flow-carrying profile are calculated using Bernoulli's, momentum and continuity equations. Only series of components can be considered. Splitting a section into multiple non-identical parallel sections is not possible. 

Subcritical flow situations are calculated in the upstream direction (backwater curves), while supercritical flow situations are calculated in the downstream direction. In situations with a free water surface where both subcritical and supercritical flows are present, the calculation direction is adjusted to the flow condition and can reverse during the calculation. Essentially, this switches between SPUIS4 and SPUIS4a or vice versa. In version 4.01 of SPUIS [3]_, an automatic switch is included. This program assumes that the flow is initially subcritical. Therefore, the calculation starts in the upstream direction. Once a critical cross-section is found during the calculation, the calculation direction is reversed, and the supercritical water trajectory is calculated until the transition to subcritical flow (the hydraulic jump) is found.

Literature
-----------

The background, formulas and set-up of the original Fortran program is given in [1]_ and [2]_. The program has been tested for a limited number of sluices. In all test cases, model results were compared with available measurements from physical model tests. Furthermore, the sensitivity of model results to parameter variations was investigated. Hardly any validation reports are available. The program SPUIS has been applied in the past to support in the design of hydraulic structures in the Netherlands, for example in Oosterhout [3]_ and the Brouwersdam [4]_

.. [1] Waterloopkundig Laboratorium, E.A. van Kleef. ‘Berekening van de afvoer van spuisluizen met behulp van een rekenmodel.’ Rapport R2125/Q331, november 1986.
.. [2] Waterloopkundig Laboratorium, E.A. van Kleef. ‘Berekening van de afvoer van spuisluizen bij schietend water situaties.’ Rapport Q331-II, juli 1989.
.. [3] Waterloopkundig Laboratorium, A. Vrijburcht. ‘Aflaatwerk en gemaal te Oosterhout.’ Rapport Q1952, maart 1995.
.. [4] Deltares, A. de Loor. ‘Bepaling afvoercoëfficiënt doorlaatmiddel Brouwersdam.’ Rapport 11202901-002-ZKS-0002, september 2018.