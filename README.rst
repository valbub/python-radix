# python-radix

Python-radix library
====================

The library contains tools for conversion numbers to a new base. Current version works with radixes from 2 to 36.

Python-radix usage examples
---------------------------
Python-radix has both procedural and object-oriented solutions.

**Procedural way example**

    # to convert number 4 from base 10 to base 2

    cast(4, 10, 2)

    >>'100'

You can use both str and int types for the number you convert.

**Object oriented way example**

    # create an object to convert numbers from one base to another (here it converts from base 10 to base 2)

    new = Converter(10, 2)

    new.convert(4)

    >>'100'

This will work too:

    new = Converter(10, 2)

    new.convert('4')

    >>'100'