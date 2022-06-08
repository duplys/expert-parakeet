## Relevant Definitions
**Abstract Type.** In programming languages, an _abstract type_ is a type that cannot be instantiated directly (a type that is not abstract &ndash; which can be instantiated &ndash; is called a _concrete type_). 

An abstract type may provide no implementation, or an incomplete implementation. In some languages, abstract types with no implementation (rather than an incomplete implementation) are known as _interfaces_. (Source: [Wikipedia contributors, "Abstract type," _Wikipedia, The Free Encyclopedia_ (accessed June 8, 2022)][1])

**Abstract Class.** In class-based object-oriented programming, abstract types are implemented as _abstract classes_ (also known as abstract base classes), and concrete types as concrete classes. (Source: [Wikipedia contributors, "Abstract type," _Wikipedia, The Free Encyclopedia_ (accessed June 8, 2022)][1])

**Abstract Base Class.** In language that support inheritance, an _abstract class_, or _abstract base class_ (ABC), is a class that cannot be instantiated because it is either labeled as abstract or it simply specifies _abstract methods_.

An abstract class may provide implementations of some methods, and may also specify virtual methods via signatures that are to be implemented by direct or indirect descendants of the abstract class.

Most object-oriented programming languages allow the programmer to specify which classes are considered abstract and will not allow these to be instantiated. For example, in Java, C# and PHP, the keyword _abstract_ is used. In C++, an abstract class is a class having at least one abstract method given by the appropriate syntax in that language (a pure virtual function in C++ parlance).

A class consisting of only virtual methods is called a Pure Abstract Base Class (or Pure ABC) in C++ and is also known as an interface by users of the language. Other languages, notably Java and C#, support a variant of abstract classes called an interface via a keyword in the language. In these languages, multiple inheritance is not allowed, but a class can implement multiple interfaces. Such a class can only contain abstract publicly accessible methods. (Source: [Wikipedia contributors, "Class (computer programming)," _Wikipedia, The Free Encyclopedia_ (accessed June 8, 2022)][3])

**Interface.** In some object-oriented languages, especially those without full multiple inheritance, the term _interface_ is used to define an _abstract type_ that contains no data and only provides method signatures (i.e., that contains no implementation).

A class having code and data for all the methods corresponding to that interface and declaring so is said to _implement_ that interface. A class can implement multiple interfaces, and hence can be of different types at the same time. (Source: [Wikipedia contributors, "Interface (computing)," _Wikipedia, The Free Encyclopedia_ (accessed June 8, 2022)][2])

## Interesting References
* https://refactoring.guru/design-patterns/abstract-factory

[1]: https://en.wikipedia.org/w/index.php?title=Abstract_type&oldid=1068234135
[2]: https://en.wikipedia.org/w/index.php?title=Interface_(computing)&oldid=1088659384
[3]: https://en.wikipedia.org/w/index.php?title=Class_(computer_programming)&oldid=1087887547





