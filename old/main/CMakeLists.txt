cmake_minimum_required(VERSION 2.6)
set(CMAKE_LEGACY_CYGWIN_WIN32 0)
set(CMAKE_VERSION_STRING ${CMAKE_MAJOR_VERSION}.${CMAKE_MINOR_VERSION}.${CMAKE_PATCH_VERSION})
IF (${CMAKE_VERSION_STRING} GREATER 2.8.4)
  cmake_policy(SET CMP0017 NEW) 
  MESSAGE ("CMake version is greater than 2.8.4")
ELSE (${CMAKE_VERSION_STRING} GREATER 2.8.4)
  MESSAGE ("CMake version is not greater than 2.8.4")
ENDIF (${CMAKE_VERSION_STRING} GREATER 2.8.4)
# Nombre del proyecto.
PROJECT(PPL)
SET(build_setup_dir $ENV{HOME}/.xc_build)

#XCBasica
SET(basica_setup_file ${build_setup_dir}/basica_dirs.cmake)
INCLUDE(${basica_setup_file})
SET(bibXCBasica_DIR ${basica_src_dir}/..)
message(STATUS "basica project dir: "${bibXCBasica_DIR})
SET(bibXCBasica_INC ${basica_inc_dir})
message(STATUS "basica include dir: "${bibXCBasica_INC})
INCLUDE_DIRECTORIES(${bibXCBasica_INC})
SET(bibXCBasica_LIB ${basica_lib_dir})
message(STATUS "basica lib dir: "${bibXCBasica_LIB})
LINK_DIRECTORIES(${bibXCBasica_LIB})

#XCLcmd
SET(lcmd_setup_file ${build_setup_dir}/lcmd_dirs.cmake)
INCLUDE(${lcmd_setup_file})
SET(bibXCLcmd_DIR ${lcmd_src_dir}/..)
message(STATUS "lcmd project dir: "${bibXCLcmd_DIR})
SET(bibXCLcmd_INC ${lcmd_inc_dir})
message(STATUS "lcmd include dir: "${bibXCLcmd_INC})
INCLUDE_DIRECTORIES(${bibXCLcmd_INC})
SET(bibXCLcmd_LIB ${lcmd_lib_dir})
message(STATUS "lcmd lib dir: "${bibXCLcmd_LIB})
LINK_DIRECTORIES(${bibXCLcmd_LIB})

#PPL
SET(ppl_setup_file ${build_setup_dir}/ppl_dirs.cmake)
INCLUDE(${ppl_setup_file})
SET(DIR_FUENTES_PPL ${ppl_src_dir})
message(STATUS "ppl project dir: "${DIR_FUENTES_PPL})
SET(libPPL_INC ${ppl_inc_dir})
message(STATUS "ppl include dir: "${libPPL_INC})
INCLUDE_DIRECTORIES(${libPPL_INC})
SET(libPPL_LIB ${ppl_lib_dir})
message(STATUS "ppl lib dir: "${libPPL_LIB})
LINK_DIRECTORIES(${libPPL_LIB})

SET(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${bibPPLBasica_DIR}/CMake")
SET(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${bibPPLLcmd_DIR}/CMake")
SET(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${DIR_FUENTES_PPL}/CMake")

INCLUDE(${CMAKE_ROOT}/Modules/CheckIncludeFile.cmake)

INCLUDE(${DIR_FUENTES_PPL}CMake/find_packages.cmake)

include_directories(${PYTHON_INCLUDE_DIRS})

# Make sure the linker can find the lcmd library once it is built.
LINK_DIRECTORIES(${LIBRARY_OUTPUT_PATH})
LINK_DIRECTORIES(${VTK_LIBRARY_DIRS})


# Archivos fuente.
SET(SOURCES ppl)

ADD_DEFINITIONS(-Wall -O3 -frounding-math)


message(STATUS "CMAKE_MODULE_PATH=" ${CMAKE_MODULE_PATH})
message(STATUS "Boost_VERSION=" ${Boost_VERSION})
message(STATUS "Boost_LIBRARIES=" ${Boost_LIBRARIES})
message(STATUS "Boost_LIBRARY_DIRS=" ${Boost_LIBRARY_DIRS})
message(STATUS "Boost_INCLUDE_DIRS=" ${Boost_INCLUDE_DIRS})

# Creamos ejecutables
FOREACH(source ${SOURCES})
  ADD_EXECUTABLE(${source} ${source})
  TARGET_LINK_LIBRARIES(${source} Ppl XCLcmd XCBasica vtkRendering vtkIO vtkHybrid CGAL CGAL_Core plotter mpfr gmp mysqlpp sqlite3 ${Boost_LIBRARIES} ${PYTHON_LIBRARIES} ${GNUGTS_LIBRARIES})
ENDFOREACH(source)




