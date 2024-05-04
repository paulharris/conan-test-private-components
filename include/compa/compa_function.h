#pragma once

#ifdef _WIN32
  #define COMPA_EXPORT __declspec(dllexport)
#else
  #define COMPA_EXPORT
#endif

COMPA_EXPORT void compa_function();
