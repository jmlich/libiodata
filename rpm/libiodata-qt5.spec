%define _name iodata-qt5
Name:     libiodata-qt5
Version:  0.19.8
Release:  1
Summary:  Library for input/ouput data
License:  LGPLv2
URL:      https://git.sailfishos.org/mer-core/libiodata
Source0:  %{name}-%{version}.tar.bz2

BuildRequires: pkgconfig(Qt5Core)
BuildRequires: bison
BuildRequires: flex

%description
This package provides a library for writing and reading structured data.

%package devel
Summary:  Development package for %{name}
Group:    Development/Libraries
Requires: pkgconfig(Qt5Core)
Requires: %{name} = %{version}-%{release}

%description devel
Provides header files for iodata library.

%package tests
Summary:  Testcases for iodata library
Group:    Development/System
Requires: testrunner-lite

%description tests
%{summary}.

%prep
%setup -q -n %{name}-%{version}

%build
export IODATA_VERSION=%version
%qmake5
make

%install
%qmake_install
install -d %{buildroot}/%{_datadir}/%{name}-tests/
mv %{buildroot}/%{_datadir}/%{_name}-tests/tests.xml %{buildroot}/%{_datadir}/%{name}-tests/tests.xml

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING debian/copyright
%{_libdir}/%{name}.so.*

%files devel
%defattr(-,root,root,-)
%{_bindir}/iodata-qt5-type-to-c++
%{_includedir}/iodata-qt5/*
%{_libdir}/%{name}.so
%{_datadir}/qt5/mkspecs/features/iodata-qt5.prf

%files tests
%defattr(-,root,root,-)
%{_bindir}/%{_name}-test
%{_datadir}/%{name}-tests/tests.xml
