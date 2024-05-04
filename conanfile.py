from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps


# NOTE that "require_compb" is ONLY an option for helping to run the tests,
# and to switch and demonstrate the behaviour that I'm testing.

class ThelibRecipe(ConanFile):
    name = "test_separate_component_lib"
    version = "1.0"
    package_type = "library"

    # Optional metadata
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of thelib package here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False], "require_compb": [True,False]}
    default_options = {"shared": False, "fPIC": True, "require_compb": True}

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*", "include/*"

    def config_options(self):
        if self.settings.os == "Windows":
            self.options.rm_safe("fPIC")

    def configure(self):
        if self.options.shared:
            self.options.rm_safe("fPIC")

    def layout(self):
        cmake_layout(self)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.components["compb_function"].libs = ["compb_function"]
        self.cpp_info.components["compb_function"].includedirs = ["include/compb"]

        self.cpp_info.components["compa_function"].libs = ["compa_function"]
        self.cpp_info.components["compa_function"].includedirs = ["include/compa"]

        if self.options.require_compb:
            self.cpp_info.components["compa_function"].requires = ["compb_function"]
