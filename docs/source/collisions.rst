Collision algorithms
--------------------


First also in the implementation there are the object to the
same object collision which are described here:

Sphere2Sphere
^^^^^^^^^^^^^

The collision of 2 spheres is the most simple algorithms. Important
is the distance between the two center points. If this distance is
larger than the sum of the two radii then there is no collision. If
the distance is equal as the radii sum both spheres has one contact
point. If there is are real overlapping one can define a contact circle
(not implemented yet!).


Box2Box
^^^^^^^

The collision of two boxes is based on a simple algorithm approach.
One has a collision of at least one corner of one box is touching
or is inside the other box. For a complete test one has to check
for all corners of all boxes! Before describing the test of a corner
is touching or inside a box it is necessary to describe a helper
algorithm, the calculation of the box volume. Generally the volume of
a box even if the box is not rectangular is calculated by multiplying
the base of a box with the height. For our purpose we need another
slightly complicated algorithm. We cut the box into 6 pyramids where
all pyramids have the same top point, which is naturally the center
point of the box. However, if one move this center point around inside
the box the calculated volume will not change (in the computational
world the volume will be the same within accuracy value!). So coming
back to the corner test. Assume that the test point is outside the box
if we now use the same volume algorithm and exchange the center point
with the test point the volume is now larger than the original volume
of the box. If the new calculated volume is equal to the original
volume then the corner is touching is laying inside the box which
indicated a collision. Please keep always in mind to check every corner
of both boxes since there is one test case in which one corner of
one box is inside the other box. The corner of this box are far away
from the other box, so checking only this box is not sufficient!
