#include <iostream>
#include "compa_function.h"

#include "compb_function.h"

void compa_function(){
    std::cout << "the compa function\n";

    // requires compb component for linking!
    compb_function();
}
