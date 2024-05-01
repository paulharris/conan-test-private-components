#pragma once

#ifdef _WIN32
  #define PUBLIC_EXPORT __declspec(dllexport)
#else
  #define PUBLIC_EXPORT
#endif

PUBLIC_EXPORT void public_function();
