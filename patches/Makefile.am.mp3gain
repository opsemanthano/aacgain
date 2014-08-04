noinst_LTLIBRARIES = libmp3gain.la

INCLUDES = -I$(top_srcdir)/aacgain

libmp3gain_la_SOURCES = gain_analysis.c apetag.c rg_error.c mp3gain.c

SUBDIRS = mpglibDBL
AM_CFLAGS = -DHAVE_MEMCPY -DAACGAIN
AM_CXXFLAGS = -DHAVE_MEMCPY -DAACGAIN
libmp3gain_la_LIBADD = $(top_builddir)/mp3gain/mpglibDBL/libmpglib.la
