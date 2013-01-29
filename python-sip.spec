Name:		python-sip
Summary:	Riverbanks's python sip
Version:	4.14.3
Release:	1
Epoch:		1
Group:		Development/Python
URL:		http://www.riverbankcomputing.co.uk/software/sip/intro
Source0:	http://ignum.dl.sourceforge.net/project/pyqt/sip/sip-%version/sip-%version.tar.gz
License:	GPLv2+
BuildRequires:	bzip2-devel
BuildRequires:	python-devel
Obsoletes:	sip < %{version}
Obsoletes:	sip-devel < %{version}

%description
SIP is a tool that makes it very easy to create Python bindings
for C and C++ libraries. It was originally developed to create PyQt,
the Python bindings for the Qt toolkit, but can be used to
create bindings for any C or C++ library.

%files
%{_bindir}/sip
%{py_platsitedir}/s*
%{py_incdir}/sip.h

#------------------------------------------------------------

%prep
%setup -q -n sip-%{version}
#  Don't use X11R6 prefix for includes neither libraries by default.
for file in specs/linux-*; do
    %__perl -p -i -e "s@/X11R6/@/@g" $file
done

%build
%__python configure.py
%define _disable_ld_no_undefined 1
%make CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC" LIBS="%{?ldflags} -lpython%{py_ver}"

%install
%makeinstall_std

%changelog
* Wed Jun 20 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.13.3-1
- Update to 4.13.3

* Wed Jun 20 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.13.2-1
- Update to 4.13.2

* Mon May 23 2011 Funda Wang <fwang@mandriva.org> 1:4.12.3-1mdv2011.0
+ Revision: 677494
- new version 4.12.3

* Mon May 02 2011 Funda Wang <fwang@mandriva.org> 1:4.12.2-1
+ Revision: 662308
- update to new version 4.12.2

* Mon Jan 24 2011 Funda Wang <fwang@mandriva.org> 1:4.12.1-1
+ Revision: 632482
- update to new version 4.12.1

* Fri Dec 24 2010 Funda Wang <fwang@mandriva.org> 1:4.12-1mdv2011.0
+ Revision: 624578
- update to new version 4.12

* Fri Oct 29 2010 Funda Wang <fwang@mandriva.org> 1:4.11.2-2mdv2011.0
+ Revision: 589913
- rebuild

* Fri Oct 29 2010 Funda Wang <fwang@mandriva.org> 1:4.11.2-1mdv2011.0
+ Revision: 589883
- new version 4.11.2

* Wed Sep 01 2010 Funda Wang <fwang@mandriva.org> 1:4.11-1mdv2011.0
+ Revision: 574999
- new version 4.11 (api 7.1->8.0)

* Sat Jul 31 2010 Funda Wang <fwang@mandriva.org> 1:4.10.5-1mdv2011.0
+ Revision: 563975
- new version 4.10.5

* Tue Jul 13 2010 Funda Wang <fwang@mandriva.org> 1:4.10.3-1mdv2011.0
+ Revision: 552366
- update to new version 4.10.3

* Thu Mar 18 2010 Funda Wang <fwang@mandriva.org> 1:4.10.1-1mdv2010.1
+ Revision: 524761
- new version 4.10.1

* Thu Jan 21 2010 Funda Wang <fwang@mandriva.org> 1:4.10-1mdv2010.1
+ Revision: 494537
- new version 4.10 final

* Thu Jan 07 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.10-0.20100102.1mdv2010.1
+ Revision: 487355
- New snapshot

* Thu Nov 26 2009 Funda Wang <fwang@mandriva.org> 1:4.9.3-1mdv2010.1
+ Revision: 470265
- new version 4.9.3

* Mon Nov 23 2009 Funda Wang <fwang@mandriva.org> 1:4.9.2-1mdv2010.1
+ Revision: 469296
- new version 4.9.2

* Sat Oct 24 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.9.1-1mdv2010.0
+ Revision: 459148
- Update to version 4.9.1 - Bugfix version

* Mon Sep 28 2009 Funda Wang <fwang@mandriva.org> 1:4.9-1mdv2010.0
+ Revision: 450450
- New version 4.9

* Wed Jul 29 2009 Frederik Himpe <fhimpe@mandriva.org> 1:4.8.2-1mdv2010.0
+ Revision: 404082
- update to new version 4.8.2

* Thu Jun 18 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.8.1-1mdv2010.0
+ Revision: 387128
- Bugfix release 4.8.1

* Sat Jun 06 2009 Funda Wang <fwang@mandriva.org> 1:4.8-1mdv2010.0
+ Revision: 383191
- New version 4.8 final

* Sat May 30 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.8-0.20090528.2mdv2010.0
+ Revision: 381197
- Fix build
- New snapshot

* Fri May 29 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.8-0.20090528.1mdv2010.0
+ Revision: 381172
- New snapshot

* Sun May 03 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.8-0.20090430.1mdv2010.0
+ Revision: 370939
- Update to snapshot tarball

* Mon Jan 26 2009 Funda Wang <fwang@mandriva.org> 1:4.7.9-3mdv2009.1
+ Revision: 333675
- link against python

* Thu Dec 25 2008 Funda Wang <fwang@mandriva.org> 1:4.7.9-2mdv2009.1
+ Revision: 318558
- rebuild for new python

* Tue Nov 18 2008 Funda Wang <fwang@mandriva.org> 1:4.7.9-1mdv2009.1
+ Revision: 304175
- new version 4.7.9

* Sun Nov 09 2008 Funda Wang <fwang@mandriva.org> 1:4.7.8-1mdv2009.1
+ Revision: 301227
- New versio 4.7.8

* Sat Aug 09 2008 Funda Wang <fwang@mandriva.org> 1:4.7.7-1mdv2009.0
+ Revision: 270022
- New version 4.7.7

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1:4.7.6-3mdv2009.0
+ Revision: 265586
- rebuild early 2009.0 package (before pixel changes)

* Tue May 27 2008 Paulo Andrade <pcpa@mandriva.com.br> 1:4.7.6-2mdv2009.0
+ Revision: 211480
- Don't use X11R6 prefix for includes neither libraries by default.

  + Funda Wang <fwang@mandriva.org>
    - fix url

* Wed May 21 2008 Funda Wang <fwang@mandriva.org> 1:4.7.6-1mdv2009.0
+ Revision: 209886
- New version 4.7.6
- obsoletes old name

  + David Walluck <walluck@mandriva.org>
    - bump release
    - fix build on x86_64
    - 4.7.5-snapshot-20080424 (required for QT 4.4 support)

  + Thierry Vignaud <tv@mandriva.org>
    - fix description-line-too-long
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Dec 07 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1:4.7.3-1mdv2008.1
+ Revision: 116205
- update to new version 4.7.3

* Fri Nov 09 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1:4.7.1-1mdv2008.1
+ Revision: 107242
- update to new version 4.7.1

* Mon Aug 20 2007 Helio Chissini de Castro <helio@mandriva.com> 1:4.7-1mdv2008.0
+ Revision: 67983
- Restored external python-sip, to make it available for all python qt3 and python qt4 builds.
- import python-sip-4.7-1mdv2008.0


