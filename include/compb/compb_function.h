#pragma once

#ifdef _WIN32
  #define COMPB_EXPORT __declspec(dllexport)
#else
  #define COMPB_EXPORT
#endif

COMPB_EXPORT void compb_function();
