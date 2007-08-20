Name: python-sip
Summary: Riverbanks's python sip
Version: 4.7
Release: %mkrel 1
Epoch: 1
Group: Development 
URL: http://www.riverbankcomputing.co.uk/sip/index.php
Source0: http://www.riverbankcomputing.com/Downloads/sip4/sip-%{version}.tar.gz
License: GPL
BuildRoot: %_tmppath/%name-%version-%release-root
BuildRequires: bzip2-devel
BuildRequires: openssl-devel
%py_requires -d

%description
SIP is a tool that makes it very easy to create Python bindings for C and C++ libraries. It was
originally developed to create PyQt, the Python bindings for the Qt toolkit, but can be used to
create bindings for any C or C++ library.

%files 
%defattr(-,root,root)
%_bindir/sip
%py_platsitedir/s*
%py_incdir/sip.h

#------------------------------------------------------------

%prep
%setup -q -n sip-%version

%build
python configure.py

%make

%install
rm -rf %buildroot
make DESTDIR=%buildroot install

%clean
rm -rf %buildroot

