#pragma once

#ifdef _WIN32
  #define PRIVATE_EXPORT __declspec(dllexport)
#else
  #define PRIVATE_EXPORT
#endif

PRIVATE_EXPORT void private_function();
