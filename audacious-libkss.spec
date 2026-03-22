Name:           audacious-libkss
Version:        0.1.0
Release:        1%{?dist}
Summary:        KSS input plugin for Audacious using libkss
License:        MIT AND ISC
URL:            https://github.com/ramonsmits/audacious-libkss

# COPR SCM source type generates this tarball from git clone --recursive
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake >= 3.22
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  audacious-devel >= 4.2
Requires:       audacious

%description
An Audacious input plugin that uses libkss to play KSS music files
(MSX, SMS, Game Gear). Supports PSG, SCC, OPLL/FMPAC, MSX-Audio/OPL
with per-channel stereo panning and NEZplug m3u playlist parsing.

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_libdir}/audacious/Input/kss-libkss.so
