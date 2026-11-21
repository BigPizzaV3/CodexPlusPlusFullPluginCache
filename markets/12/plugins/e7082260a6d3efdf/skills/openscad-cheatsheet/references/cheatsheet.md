# OpenSCAD official cheatsheet

Downloaded October 25, 2026 from [openscad.org/cheatsheet](https://openscad.org/cheatsheet/). The source labels this sheet v2021.01. Markdown conversion retains the source wording and link targets. The [HTML snapshot](cheatsheet.html) retains its original layout references. By Peter Uithoven at [Fablab Amersfoort](https://www.fablabamersfoort.nl/), [CC-BY](https://freedomdefined.org/Licenses/CC-BY).

# OpenSCAD

## v2021.01

## Syntax

- [var](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/General#Variables) = [value](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/General#Values_and_Data_Types);

- [var](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/General#Variables) = cond [?](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Conditional_and_Iterator_Functions#Conditional_?_:) value_if_true [:](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Conditional_and_Iterator_Functions#Conditional_?_:) value_if_false;

- [var](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/General#Variables) = [function](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/User-Defined_Functions_and_Modules#Function_Literals) (x) x + x;

- [module](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/User-Defined_Functions_and_Modules#Modules) name(…) { … }
name();

- [function](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/User-Defined_Functions_and_Modules#Functions) name(…) = …
name();

- [include](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Include_Statement) <….scad>

- [use](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Include_Statement) <….scad>

## Constants

- [undef](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/General#The_Undefined_Value)

undefined value

- [PI](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/General#Numbers)

mathematical constant [π](https://en.wikipedia.org/wiki/Pi) (~3.14159)

## Operators

- [n + m](https://en.wikibooks.org/w/index.php?title=OpenSCAD_User_Manual/Mathematical_Operators#Scalar_Arithmetical_Operators)

Addition

- [n - m](https://en.wikibooks.org/w/index.php?title=OpenSCAD_User_Manual/Mathematical_Operators#Scalar_Arithmetical_Operators)

Subtraction

- [n * m](https://en.wikibooks.org/w/index.php?title=OpenSCAD_User_Manual/Mathematical_Operators#Scalar_Arithmetical_Operators)

Multiplication

- [n / m](https://en.wikibooks.org/w/index.php?title=OpenSCAD_User_Manual/Mathematical_Operators#Scalar_Arithmetical_Operators)

Division

- [n % m](https://en.wikibooks.org/w/index.php?title=OpenSCAD_User_Manual/Mathematical_Operators#Scalar_Arithmetical_Operators)

Modulo

- [n ^ m](https://en.wikibooks.org/w/index.php?title=OpenSCAD_User_Manual/Mathematical_Operators#Scalar_Arithmetical_Operators)

Exponentiation

- [n < m](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Mathematical_Operators#Relational_operators)

Less Than

- [n <= m](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Mathematical_Operators#Relational_operators)

Less or Equal

- [b == c](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Mathematical_Operators#Relational_Operators)

Equal

- [b != c](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Mathematical_Operators#Relational_Operators)

Not Equal

- [n >= m](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Mathematical_Operators#Relational_Operators)

Greater or Equal

- [n > m](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Mathematical_Operators#Relational_Operators)

Greater Than

- [b && c](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Mathematical_Operators#Logical_Operators)

Logical And

- [b || c](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Mathematical_Operators#Logical_Operators)

Logical Or

- [!b](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Mathematical_Operators#Logical_Operators)

Negation

## Special variables

- [$fa](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Other_Language_Features#$fa)

minimum angle

- [$fs](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Other_Language_Features#$fs)

minimum size

- [$fn](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Other_Language_Features#$fn)

number of segments

- [$t](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Other_Language_Features#$t)

animation step

- [$vpr](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Other_Language_Features#$vpr)

viewport rotation angles in degrees

- [$vpt](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Other_Language_Features#$vpt)

viewport translation

- [$vpd](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Other_Language_Features#$vpd)

viewport camera distance

- [$vpf](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Other_Language_Features#$vpf)

viewport camera field of view

- [$children](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/User-Defined_Functions_and_Modules#Children)

number of module children

- [$preview](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Other_Language_Features#$preview)

true in F5 preview, false for F6

## Modifier Characters

- [*](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Modifier_Characters#Disable_Modifier)

disable

- [!](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Modifier_Characters#Root_Modifier)

show only

- [#](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Modifier_Characters#Debug_Modifier)

highlight / debug

- [%](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Modifier_Characters#Background_Modifier)

transparent / background

## 2D

- [circle](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Using_the_2D_Subsystem#circle)(radius | d=diameter)

- [square](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Using_the_2D_Subsystem#square)(size,center)

- [square](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Using_the_2D_Subsystem#square)([width,height],center)

- [polygon](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Using_the_2D_Subsystem#polygon)([points])

- [polygon](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Using_the_2D_Subsystem#polygon)([points],[paths])

-  [text](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Text)(text,size,font,direction,language,script,
halign,valign,spacing)

- [import](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Importing_Geometry#import)("….extformats: DXF|SVG", convexity)

- [projection](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Using_the_2D_Subsystem#3D_to_2D_Projection)(cut)

## 3D

- [sphere](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Primitive_Solids#sphere)(radius | d=diameter)

- [cube](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Primitive_Solids#cube)(size, center)

- [cube](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Primitive_Solids#cube)([width,depth,height], center)

- [cylinder](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Primitive_Solids#cylinder)(h,r|d,center)

- [cylinder](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Primitive_Solids#cylinder)(h,r1|d1,r2|d2,center)

- [polyhedron](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Primitive_Solids#polyhedron)(points, faces, convexity)

- [import](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Importing_Geometry#import)("….extformats: STL|OFF|AMF|3MF", convexity)

- [linear_extrude](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Using_the_2D_Subsystem#linear_extrude)(height,center,convexity,twist,slices)

- [rotate_extrude](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Using_the_2D_Subsystem#rotate_extrude)(angle,convexity)

- [surface](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Other_Language_Features#surface)(file = "….extformats: DAT|PNG",center,convexity)

## Transformations

- [translate](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Transformations#translate)([x,y,z])

- [rotate](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Transformations#rotate)([x,y,z])

- [rotate](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Transformations#rotate)(a, [x,y,z])

- [scale](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Transformations#scale)([x,y,z])

- [resize](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Transformations#resize)([x,y,z],auto,convexity)

- [mirror](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Transformations#mirror)([x,y,z])

- [multmatrix](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Transformations#multmatrix)(m)

- [color](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Transformations#color)("colorname",alpha)

- [color](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Transformations#color)("#hexvalue#rgb|#rgba|#rrggbb|#rrggbbaa")

- [color](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Transformations#color)([r,g,b,a])

- [offset](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Transformations#offset)(r|delta,chamfer)

- [hull](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Transformations#hull)()

- [minkowski](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Transformations#minkowski)(convexity)

## Lists

- [list = […, …, …];](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/General#Vectors)

create a list

- [var = list[2];](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/General#Indexing_elements_within_vectors)

index a list (from 0)

- [var = list.z;](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/General#Dot_notation_indexing)

dot notation indexing (x/y/z)

## Boolean operations

- [union](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/CSG_Modelling#union)()

- [difference](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/CSG_Modelling#difference)()

- [intersection](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/CSG_Modelling#intersection)()

## List Comprehensions

- [Generate](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/List_Comprehensions#for) [ for (i = range|list) i ]

- [Generate](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/List_Comprehensions#for) [ for (init;condition;next) i ]

- [Flatten](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/List_Comprehensions#each) [ each i ]

- [Conditions](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/List_Comprehensions#if) [ for (i = …) if (condition(i)) i ]

- [Conditions](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/List_Comprehensions#if/else) [ for (i = …) if (condition(i)) x else y ]

- [Assignments](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/List_Comprehensions#let) [ for (i = …) let (assignments) a ]

## Flow Control

- [for](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Conditional_and_Iterator_Functions#For_loop) (i = [start:end]) { … }

- [for](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Conditional_and_Iterator_Functions#For_loop) (i = [start:step:end]) { … }

- [for](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Conditional_and_Iterator_Functions#For_loop) (i = […,…,…]) { … }

- [for](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Conditional_and_Iterator_Functions#For_loop) (i = …, j = …, …) { … }

- [intersection_for](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Conditional_and_Iterator_Functions#Intersection_For_Loop)(i = [start:end]) { … }

- [intersection_for](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Conditional_and_Iterator_Functions#Intersection_For_Loop)(i = [start:step:end]) { … }

- [intersection_for](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Conditional_and_Iterator_Functions#Intersection_For_Loop)(i = […,…,…]) { … }

- [if](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Conditional_and_Iterator_Functions#If_Statement) (…) { … }

- [let](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Conditional_and_Iterator_Functions#Let_Statement) (…) { … }

## Type test functions

- [is_undef](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Type_Test_Functions#is_undef)

- [is_bool](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Type_Test_Functions#is_bool)

- [is_num](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Type_Test_Functions#is_num)

- [is_string](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Type_Test_Functions#is_string)

- [is_list](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Type_Test_Functions#is_list)

- [is_function](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Type_Test_Functions#is_function)

## Other

- [echo](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Other_Language_Features#echo)(…)

- [render](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Other_Language_Features#render)(convexity)

- [children](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/User-Defined_Functions_and_Modules#Children)([idx])

- [assert](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Other_Language_Features#assert)(condition, message)

- [assign](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Conditional_and_Iterator_Functions#Assign_Statement) (…) { … }

## Functions

- [concat](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Mathematical_Functions#concat)

- [lookup](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Mathematical_Functions#lookup)

- [str](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/String_Functions#str)

- [chr](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/String_Functions#chr)

- [ord](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/String_Functions#ord)

- [search](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Other_Language_Features#search)

- [version](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Other_Language_Features#OpenSCAD_Version)

- [version_num](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Other_Language_Features#OpenSCAD_Version)

- [parent_module](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Other_Language_Features#parent_module.28n.29_and_.24parent_modules)(idx)

## Mathematical

- [abs](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Mathematical_Functions#abs)

- [sign](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Mathematical_Functions#sign)

- [sin](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Mathematical_Functions#sin)

- [cos](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Mathematical_Functions#cos)

- [tan](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Mathematical_Functions#tan)

- [acos](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Mathematical_Functions#acos)

- [asin](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Mathematical_Functions#asin)

- [atan](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Mathematical_Functions#atan)

- [atan2](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Mathematical_Functions#atan2)

- [floor](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Mathematical_Functions#floor)

- [round](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Mathematical_Functions#round)

- [ceil](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Mathematical_Functions#ceil)

- [ln](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Mathematical_Functions#ln)

- [len](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Mathematical_Functions#len)

- [let](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Mathematical_Functions#let)

- [log](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Mathematical_Functions#log)

- [pow](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Mathematical_Functions#pow)

- [sqrt](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Mathematical_Functions#sqrt)

- [exp](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Mathematical_Functions#exp)

- [rands](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Mathematical_Functions#rands)

- [min](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Mathematical_Functions#min)

- [max](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Mathematical_Functions#max)

- [norm](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Mathematical_Functions#norm)

- [cross](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Mathematical_Functions#cross)

Links: [Official website](https://openscad.org/) | [Code](https://github.com/openscad/openscad) | [Issues](https://github.com/openscad/openscad/issues) | [Manual](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual) | [MCAD library](https://github.com/openscad/MCAD) | [Mailing list](https://openscad.org/community.html#forum) | [Other links](https://fablabamersfoort.nl/book/openscad)

[Edit me on GitHub!](https://github.com/openscad/openscad.github.com/tree/main/cheatsheet)
By Peter Uithoven @ [Fablab Amersfoort](https://www.fablabamersfoort.nl/) ([CC-BY](https://freedomdefined.org/Licenses/CC-BY))
