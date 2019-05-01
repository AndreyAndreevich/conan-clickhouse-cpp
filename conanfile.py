import os
from conans import ConanFile, CMake, tools

class ClickhouseclientConan(ConanFile):
    name = "clickhouse-cpp"
    version = "0.1"
    license = "http://www.apache.org/licenses/LICENSE-2.0"
    author = "Andrey l.a.r.p@yandex.ru"
    url = "https://github.com/artpaul/clickhouse-cpp.git"
    description = "Clickhouse C++ client"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        git = tools.Git(folder="clickhouse-cpp")
        git.clone("https://github.com/artpaul/clickhouse-cpp.git")

        os.rename(os.path.join(self.name, "CMakeLists.txt"),
                  os.path.join(self.name, "CMakeListsOriginal.txt"))
        fd = os.open(os.path.join(self.name, "CMakeLists.txt"), os.O_RDWR | os.O_CREAT)

        str = '''cmake_minimum_required(VERSION 3.0)
            project(cmake_wrapper)
            
            include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
            conan_basic_setup()
            '''
        if self.settings.os == "Windows":
            str += "add_compile_definitions(GTEST_LANG_CXX11=1)\n"
        str += '''include("CMakeListsOriginal.txt")'''

        os.write(fd, str.encode())
        os.close(fd)

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="clickhouse-cpp")
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="clickhouse-cpp")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        if self.settings.compiler == "Visual Studio":
            self.cpp_info.libs = tools.collect_libs(self)
        else:
            self.cpp_info.libs = ["clickhouse-cpp-lib"]