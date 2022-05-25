#include "point.h"
#include <stdio.h>

int main(int argc, char** argv) {
    struct Point* p1 = makepoint(2.1, 3.2);
    struct Point* p2 = makepoint(2.5, 3.6);

    double d = distance(p1, p2);
    printf("[*] Distance between p1 and p2: %f\n", d);

    // This declaration won't work because point.h doesn't define the size
    // of struct Point. It also doesn't define the members of Point, so 
    // direct access to x,y is impossible.  
    // struct Point p3;
    // p1->x = 3;

    return 0;
}