#include "compa_function.h"


#if __has_include("compb_function_failure.h")
#  warning "BAD - I can see compb_function_failure.h"
// This should NOT be possible!
#  include "compb_function_failure.h"
#endif



int main() {
    compa_function();
}
