%define name libqwtplot3d
%define version 0.2.7
%define release %mkrel 6

%define fakename  qwtplot3d

%define major 0
%define libname %mklibname %{fakename} %major
%define libnamedev %mklibname %{fakename}  -d

Name: %name
Version: %version
Release: %release
Summary: 3D plotting widget extension to the Qt GUI
License: zlib
Group: System/Libraries
Url: http://qwtplot3d.sourceforge.net/
Source: http://puzzle.dl.sourceforge.net/sourceforge/qwtplot3d/qwtplot3d-%version.tar.bz2
Patch0: qwtplot3d-gcc44.patch
BuildRequires: qt4-devel
BuildRequires: zlib-devel
BuildRequires: mesaglu-devel
BuildRoot: %{_tmppath}/%{name}-root

%description
QwtPlot3D is a feature-rich Qt/OpenGL-based C++ programming library.
It provides essentially a bunch of 3D-widgets for programmers.

%package -n %libname
Summary: 3D plotting widget extension to the Qt GUI
Group: System/Libraries

%description -n %libname
QwtPlot3D is a feature-rich Qt/OpenGL-based C++ programming library.
It provides essentially a bunch of 3D-widgets for programmers.

%package -n %libnamedev
Summary: Development tools for programs which uses QwtPlot3D Widget set
Group: Development/Other
Requires: %libname = %version-%release
Provides: %{name}-devel = %version-%release
Obsoletes: %{libname}-devel

%description -n %libnamedev
QwtPlot3D is a feature-rich Qt/OpenGL-based C++ programming library.
It provides essentially a bunch of 3D-widgets for programmers.

%prep
%setup -q -n qwtplot3d
%patch0 -p1

%build
%qmake_qt4
%make

%install
mkdir -p %buildroot%{_includedir}
mkdir -p %buildroot%_libdir

for n in include/*.h ; do
    install -m 644 $n %buildroot%{_includedir}
done

# install, preserving links
chmod 644 lib/libqwtplot3d.so*
for n in lib/libqwtplot3d.so* ; do
    cp -d $n %buildroot%_libdir
done

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files -n %libname
%defattr (-,root,root)
%{_libdir}/libqwtplot3d.so.%{major}*

%files -n %libnamedev
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
