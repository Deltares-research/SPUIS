.. |br| raw:: html

   <br />

.. _theory:

Theory
===========

SPUIS can calculate water levels and flow velocities in discharge sluices and other hydraulic structures with a free surface or with submerged pipes or culverts. The hydraulic structure may contain control structures such as gates, spillways or valves. Constructions up- and downstream of the hydraulic structure, such as a gradually varying discharge channel with sheet pile walls at the sides for guiding the flow, or an energy dissipator at the downstream end, can also be taken into account. 

To run calculations with SPUIS, the hydraulic structure must be schematized into (minimum 2, maximum 50) sections. Each section requires a specified bed level and location along the waterway. If two consecutive sections have a different bed level, the bed level in-between the sections will increase or decrease linearly to create a sloping bed. Sections should be chosen such that all changes in the width and height of hydraulic structure and surrounding waterway are captured. Each section is defined by a profile (minimum 2, maximum 20) with specified wet perimeters (varying with height) and Nikuradze roughness length. A single profile may be used to describe multiple sections that have the same geometry, but if the roughness differs, a new profile definition is required for that section. Profiles describing parallel culverts must describe these culverts as a single, larger culvert: separation into individual parallel culverts is not possible in SPUIS. To ensure that wall friction is implemented correctly in this case, the wet perimeter of this single, larger culvert needs to be equal to the sum of the wet perimeters of each individual culvert.

.. image:: ../images/definitions.png

SPUIS has two built-in computation methods: the user can pick from using either backwater curves (only for structures with a free surface) or Bernoulli and momentum equations. A SPUIS calculation always starts at the first cross-section on the downstream side. SPUIS assumes that the flow is steady and initially subcritical. Calculations are then made at each cross-section while moving in the upstream direction. On a transition to the supercritial flow regime, indicated by finding a critical cross-section, the direction of the computations automatically switches to the downstream direction. SPUIS will then continue in the downstream direction until it finds the transition back to the subcritical regime, indicated by a (submerged) hydraulic jump. After finding the hydraulic jump, SPUIS will resume its calculation, again in the upstream direction, from the location it originally had found the critical cross-section. This process of switching the direction of the calculations is shown below. 

.. image:: ../images/rekenschema.png
