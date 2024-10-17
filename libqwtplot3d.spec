%define fakename qwtplot3d

%define major 0
%define libname %mklibname %{fakename} %{major}
%define devname %mklibname %{fakename}  -d

Summary:	3D plotting widget extension to the Qt GUI
Name:		libqwtplot3d
Version:	0.2.7
Release:	9
License:	zlib
Group:		System/Libraries
Url:		https://qwtplot3d.sourceforge.net/
Source0:	http://puzzle.dl.sourceforge.net/sourceforge/qwtplot3d/qwtplot3d-%{version}.tar.bz2
Patch0:		qwtplot3d-0.2.7-headers.patch
Patch1:		qwtplot3d-0.2.7-linkage.patch
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(zlib)

%description
QwtPlot3D is a feature-rich Qt/OpenGL-based C++ programming library.
It provides essentially a bunch of 3D-widgets for programmers.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	3D plotting widget extension to the Qt GUI
Group:		System/Libraries

%description -n %{libname}
QwtPlot3D is a feature-rich Qt/OpenGL-based C++ programming library.
It provides essentially a bunch of 3D-widgets for programmers.

%files -n %{libname}
%{_libdir}/libqwtplot3d.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development tools for programs which uses QwtPlot3D Widget set
Group:		Development/Other
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
QwtPlot3D is a feature-rich Qt/OpenGL-based C++ programming library.
It provides essentially a bunch of 3D-widgets for programmers.

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so

#----------------------------------------------------------------------------

%prep
%setup -q -n qwtplot3d
%patch0 -p1
%patch1 -p1

%build
%qmake_qt4
%make

%install
mkdir -p %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_libdir}

for n in include/*.h ; do
    install -m 0644 $n %{buildroot}%{_includedir}
done

# install, preserving links
chmod 0755 lib/libqwtplot3d.so*
for n in lib/libqwtplot3d.so* ; do
    cp -d $n %{buildroot}%{_libdir}
done

