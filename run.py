import os
import shutil
import argparse
import sys
import subprocess

def script_directory():
    return os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    # Configure.
    args = ["-S", script_directory(), "-B", os.path.join(script_directory(), "build"), "-G", "Ninja Multi-Config"]

    args.append("-DAF_BUILD_OPENCL=OFF")
    args.append("-DAF_BUILD_EXAMPLES=OFF")
    args.append("-DAF_BUILD_UNIFIED=OFF")
    args.append("-DAF_BUILD_DOCS=OFF")
    args.append("-DAF_BUILD_FORGE=OFF")
    args.append("-DAF_TEST_WITH_MTX_FILES=OFF")
    args.append("-DAF_USE_CCACHE=OFF")
    args.append("-DAF_WITH_CPUID=OFF")
    args.append("-DAF_WITH_EXTERNAL_PACKAGES_ONLY=OFF")
    args.append("-DAF_WITH_FMT_HEADER_ONLY=OFF")
    args.append("-DAF_WITH_NONFREE=OFF")
    args.append("-DAF_WITH_STATIC_FREEIMAGE=OFF")
    args.append("-DAF_WITH_IMAGEIO=OFF")
    args.append("-DAF_WITH_LOGGING=ON")
    args.append("-DAF_WITH_STACKTRACE=ON")
    args.append("-DAF_INTERNAL_DOWNLOAD_FLAG=ON")

    # Don't build any tests.
    args.append("-DBUILD_GMOCK=OFF")
    args.append("-DBUILD_TESTING=OFF")

    # Set all output paths manually as we copy from these during the package stage.
    args.append("-DAF_INSTALL_BIN_DIR=lib")
    args.append("-DAF_INSTALL_CMAKE_DIR=cmake")
    args.append("-DAF_INSTALL_DOC_DIR=doc")
    args.append("-DAF_INSTALL_EXAMPLE_DIR=examples")
    args.append("-DAF_INSTALL_INC_DIR=include")
    args.append("-DAF_INSTALL_LIB_DIR=lib")
    args.append("-DAF_INSTALL_MAN_DIR=share/ArrayFire/man")

    # On Linux this sets the RUNPATH to the install path of the AF libs.
    # This also installs/copies all the system binaries used by AF (CUDA/MKL).
    args.append("-DAF_INSTALL_STANDALONE=ON")

    # CPU settings.
    args.append("-DAF_BUILD_CPU=ON")
    args.append("-DAF_COMPUTE_LIBRARY=FFTW/LAPACK/BLAS")

    # CUDA settings. See options to customize architectures.
    args.append("-DAF_BUILD_CUDA=OFF") # WARNING !!!!!!!!!!!!!!!!!!!!!!!!!!!!!! OFF SHOULD BE ON
    args.append("-DCUDA_architecture_build_targets=7.2")
    args.append("-DAF_WITH_CUDNN=ON")
    args.append("-DAF_WITH_STATIC_CUDA_NUMERIC_LIBS=OFF")

    # Dependecies.
    # CUDA. Should be installed.
    # Lapacke, atlas.
    # sudo apt install liblapacke-dev libatlas-base-dev
    # Boost.
    # boost 1.72.0. Downloaded from https://boostorg.jfrog.io/artifactory/main/release/1.72.0/source/
    # Extracted to directory above arrayfire (../, /home/afaq.sabir/dev/).
    # cd /home/afaq.sabir/dev/
    # tar --bzip2 -xf ./boost_1_72_0.tar.bz2
    # ./bootstrap.sh --prefix=/home/afaq.sabir/dev/boost_1_72_0/install
    # ./b2 install
    args.append("-DBoost_DIR=/home/afaq.sabir/dev/boost_1_72_0/install/lib/cmake/Boost-1.72.0")
    #args.append("-DBoost_INCLUDE_DIR=/home/afaq.sabir/dev/boost_1_72_0/install/include")
    #args.append("-DBoost_PROGRAM_OPTIONS_LIBRARY_DEBUG:FILEPATH=Boost_PROGRAM_OPTIONS_LIBRARY_DEBUG-NOTFOUND")
    #args.append("-DBoost_PROGRAM_OPTIONS_LIBRARY_RELEASE:FILEPATH=Boost_PROGRAM_OPTIONS_LIBRARY_RELEASE-NOTFOUND")

    subprocess.run(["cmake", *args], check=True)

    # Build.
    args = ["--build", os.path.join(script_directory(), "build"), "--config", "Release"]
    subprocess.run(["cmake", *args], check=True)

