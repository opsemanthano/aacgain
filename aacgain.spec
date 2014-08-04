Summary: Lossless MP4/M4A (AAC) and MP3 volume adjustment tool 
Name: aacgain
Version: 1.8
Release: 1
License: GPL
Group: Productivity/Multimedia/Sound/Editors 
URL: http://altosdesign.com/aacgain/
Packager: Miguel Angel <maacruz at gmail dot com>
Source: aacgain-%{version}.tar.bz2
Buildroot: /var/tmp/%{name}-root

%description
AACGain is a modification to Glen Sawyer's excellent  mp3gain program. It supports AAC (mp4/m4a/QuickTime) audio files in addtion to mp3 files. If you are not familiar with mp3gain, stop reading this, and go to http://mp3gain.sourceforge.net. 
AACGain normalizes the volume of digital music files using the  ReplayGain algorithm. It works by modifying the global_gain fields in the mp4 samples. Free-form metadata tags are added to the file to save undo information, making the normalization process reversable.
AACGain uses the same command-line user interface as mp3gain.

BACK UP YOUR MUSIC FILES BEFORE USING AACGAIN! THIS IS EXPERIMENTAL SOFTWARE.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
make

%install
rm -rf $RPM_BUILD_ROOT
make install-strip DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{_bindir}/aacgain

%changelog
* Sat Nov 08 2008 Miguel Angel <maacruz at gmail dot com>
- Uptdate to 1.8
* Tue May 08 2007 Miguel Angel <maacruz at gmail dot com>
- Update to 1.7
* Wed Apr 11 2007 Miguel Angel <maacruz at gmail dot com>
- Update to 1.6
* Sat Nov 5 2005 Miguel Angel <maacruz at gmail dot com>
- first build
