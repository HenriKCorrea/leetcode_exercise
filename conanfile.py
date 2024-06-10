from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps

class Recipe(ConanFile):
    def __init__(self, display_name):
        super().__init__(display_name)
        
    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"  
    
    def requirements(self):
        self.requires("gtest/1.14.0")

    def layout(self):
        cmake_layout(self)

    def generate(self):
        # Import dependencies 
        deps = CMakeDeps(self)
        deps.generate()

        # Generate the CMake
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()