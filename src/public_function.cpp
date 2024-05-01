#include <iostream>
#include "public_function.h"

#include "private_function.h"

void public_function(){
    std::cout << "the public function\n";

    // requires private component for linking!
    private_function();
}
