#include "public_function.h"


#if __has_include("private_function_failure.h")
#  warning "BAD - I can see private_function_failure.h"
// This should NOT be possible!
#  include "private_function_failure.h"
#endif



int main() {
    public_function();
}
