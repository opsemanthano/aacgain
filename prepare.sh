#!/bin/bash
# Thx to "Hardloaf" for improvements in this...
# Changed for a better source tree with all needed files included (maacruz@gmail.com)

echo Patching...
patch -b -p0 -N <patches/faad2.patch
patch -b -p0 -N <patches/mpeg4ip.patch
patch -b -p0 -N <patches/mp3gain.patch

rm -f mp3gain/mpglibDBL/config.h
cp patches/Makefile.am.mpglibDBL mp3gain/mpglibDBL/Makefile.am
cp patches/Makefile.am.mp3gain mp3gain/Makefile.am

echo
echo Running automake and friends...
aclocal
# on macos we need glibtoolize
libtoolize -c -f 2>/dev/null || glibtoolize -f
autoheader
autoconf
automake -c -a

