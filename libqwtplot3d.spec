%define fakename qwtplot3d

%define major 0
%define libname %mklibname %{fakename} %{major}
%define libnamedev %mklibname %{fakename}  -d

Name:		libqwtplot3d
Version:	0.2.7
Release:	%mkrel 7
Summary:	3D plotting widget extension to the Qt GUI
License:	zlib
Group:		System/Libraries
Url:		http://qwtplot3d.sourceforge.net/
Source:		http://puzzle.dl.sourceforge.net/sourceforge/qwtplot3d/qwtplot3d-%{version}.tar.bz2
Patch0:		qwtplot3d-0.2.7-headers.patch
Patch1:		qwtplot3d-0.2.7-linkage.patch
BuildRequires:	qt4-devel
BuildRequires:	zlib-devel
BuildRequires:	mesaglu-devel

%description
QwtPlot3D is a feature-rich Qt/OpenGL-based C++ programming library.
It provides essentially a bunch of 3D-widgets for programmers.

%package -n %{libname}
Summary:	3D plotting widget extension to the Qt GUI
Group:		System/Libraries

%description -n %{libname}
QwtPlot3D is a feature-rich Qt/OpenGL-based C++ programming library.
It provides essentially a bunch of 3D-widgets for programmers.

%package -n %{libnamedev}
Summary:	Development tools for programs which uses QwtPlot3D Widget set
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{libname}-devel

%description -n %{libnamedev}
QwtPlot3D is a feature-rich Qt/OpenGL-based C++ programming library.
It provides essentially a bunch of 3D-widgets for programmers.

%prep
%setup -q -n qwtplot3d
%patch0 -p1
%patch1 -p1

%build
%qmake_qt4
%make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_libdir}

for n in include/*.h ; do
    install -m 644 $n %{buildroot}%{_includedir}
done

# install, preserving links
chmod 644 lib/libqwtplot3d.so*
for n in lib/libqwtplot3d.so* ; do
    cp -d $n %{buildroot}%{_libdir}
done

%clean
rm -rf %{buildroot}

%files -n %{libname}
%{_libdir}/libqwtplot3d.so.%{major}*

%files -n %{libnamedev}
%{_includedir}/*
%{_libdir}/*.so



%changelog
* Sat Apr 28 2012 Andrey Bondrov <abondrov@mandriva.org> 0.2.7-7mdv2012.0
+ Revision: 794319
- Update patches and cleanup spec

* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.7-6mdv2011.0
+ Revision: 620219
- the mass rebuild of 2010.0 packages

* Tue Aug 25 2009 Emmanuel Andry <eandry@mandriva.org> 0.2.7-5mdv2010.0
+ Revision: 421198
- add P1 to fix gcc44 build
- check major

* Tue Aug 05 2008 Funda Wang <fwang@mandriva.org> 0.2.7-4mdv2009.0
+ Revision: 263927
- fix license
- drop unneeded BR

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.2.7-3mdv2009.0
+ Revision: 240988
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sat Jul 21 2007 Funda Wang <fwang@mandriva.org> 0.2.7-1mdv2008.0
+ Revision: 54262
- fix file list
- New version

* Tue Apr 24 2007 Lenny Cartier <lenny@mandriva.org> 0.2.6-2mdv2008.0
+ Revision: 17950
- Rebuild

* Mon Apr 23 2007 Lenny Cartier <lenny@mandriva.org> 0.2.6-1mdv2008.0
+ Revision: 17656
- Update to 0.2.6


* Fri Jul 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.2.5-1mdk
- 0.2.5
- Fix qt path
- Fix BuildRequires

* Wed Mar 09 2005 Lenny Cartier <lenny@mandrakesoft.com> 0.2.4-0.beta.1mdk
- from Olivier Lahaye <olivier.lahaye1@free.Fr> : 
	- port spec to Mandrake 10.1

* Fri Feb 11 2005 Vitaly Lipatov <lav@altlinux.ru> 0.2.4-alt0.2beta
- move libraries to /usr/lib64, fix .so placement

* Mon Dec 27 2004 Vitaly Lipatov <lav@altlinux.ru> 0.2.4-alt0.1beta
- first build for ALT Linux Sisyphus

