cmake_minimum_required(VERSION 3.22)
set(CMAKE_POLICY_DEFAULT_CMP0077 NEW)

project(audacious-libkss
	VERSION 0.1.0
	LANGUAGES C CXX
)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

if(CMAKE_CXX_COMPILER_ID MATCHES "GNU" OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
	add_compile_options(-ffunction-sections -Wall)
	add_link_options(-Wl,--gc-sections -Wl,-O1)
endif()

find_package(PkgConfig REQUIRED)
pkg_search_module(AUDACIOUS REQUIRED audacious>=4.2)
pkg_get_variable(AUDACIOUS_PLUGIN_DIR audacious plugin_dir)

# libkss sources (compiled as a static library)
set(LIBKSS_SOURCES
	libkss/src/filters/dc_filter.c
	libkss/src/filters/filter.c
	libkss/src/filters/rc_filter.c
	libkss/src/kss/bgm2kss.c
	libkss/src/kss/kss.c
	libkss/src/kss/kss2kss.c
	libkss/src/kss/kssload.c
	libkss/src/kss/mbm2kss.c
	libkss/src/kss/mgs2kss.c
	libkss/src/kss/mpk2kss.c
	libkss/src/kss/opx2kss.c
	libkss/src/kss2vgm.c
	libkss/src/kssplay.c
	libkss/src/rconv/psg_rconv.c
	libkss/src/vm/detect.c
	libkss/src/vm/mmap.c
	libkss/src/vm/vm.c
	libkss/modules/emu2149/emu2149.c
	libkss/modules/emu2212/emu2212.c
	libkss/modules/emu2413/emu2413.c
	libkss/modules/emu76489/emu76489.c
	libkss/modules/emu8950/emu8950.c
	libkss/modules/emu8950/emuadpcm.c
	libkss/modules/kmz80/kmdmg.c
	libkss/modules/kmz80/kmevent.c
	libkss/modules/kmz80/kmr800.c
	libkss/modules/kmz80/kmz80.c
	libkss/modules/kmz80/kmz80c.c
	libkss/modules/kmz80/kmz80t.c
)

add_library(kss-static STATIC ${LIBKSS_SOURCES})
set_target_properties(kss-static PROPERTIES POSITION_INDEPENDENT_CODE ON)
target_include_directories(kss-static PRIVATE libkss/src libkss/modules)
target_compile_options(kss-static PRIVATE
	$<$<C_COMPILER_ID:GNU,Clang>:-Wno-incompatible-pointer-types -Wno-int-conversion>
)

# Plugin module
add_library(audacious-libkss MODULE kss-plugin.cc)
set_target_properties(audacious-libkss PROPERTIES PREFIX "" OUTPUT_NAME "kss-libkss")
target_compile_features(audacious-libkss PUBLIC cxx_std_17)
target_include_directories(audacious-libkss PRIVATE ${AUDACIOUS_INCLUDE_DIRS} libkss/src libkss/modules)
target_link_libraries(audacious-libkss PUBLIC ${AUDACIOUS_LINK_LIBRARIES} kss-static)

install(TARGETS audacious-libkss DESTINATION ${AUDACIOUS_PLUGIN_DIR}/Input)
