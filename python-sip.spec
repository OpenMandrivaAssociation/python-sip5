%define snapshot -snapshot-20080424

Name: python-sip
Summary: Riverbanks's python sip
Version: 4.7.5
Release: %mkrel 0.20080424.1
Epoch: 1
Group: Development/Python 
URL: http://www.riverbankcomputing.co.uk/sip/index.php
Source0: http://www.riverbankcomputing.com/static/Downloads/sip4/sip-%{version}%{snapshot}.tar.gz
License: GPL
BuildRoot: %_tmppath/%name-%version-%release-root
BuildRequires: bzip2-devel
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
%setup -q -n sip-%{version}%{snapshot}

%build
%{__python} configure.py
%{make} CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC"

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}

%clean
%{__rm} -rf %{buildroot}
