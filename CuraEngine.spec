#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : CuraEngine
Version  : 4.11.0
Release  : 21
URL      : https://github.com/Ultimaker/CuraEngine/archive/4.11.0/CuraEngine-4.11.0.tar.gz
Source0  : https://github.com/Ultimaker/CuraEngine/archive/4.11.0/CuraEngine-4.11.0.tar.gz
Source1  : https://github.com/nothings/stb/archive/e6afb9cbae4064da8c3e69af3ff5c4629579c1d2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : AGPL-3.0 BSD-3-Clause BSL-1.0 JSON MIT
Requires: CuraEngine-bin = %{version}-%{release}
Requires: CuraEngine-license = %{version}-%{release}
Requires: libArcus-lib
BuildRequires : buildreq-cmake
BuildRequires : libArcus-dev
BuildRequires : pkg-config
BuildRequires : protobuf-dev

%description
=====================================================================
Clipper Change Log
=====================================================================
v6.4.2 (27 February 2017) Rev 512
* Several minor bugfixes: #152 #160 #161 #162

%package bin
Summary: bin components for the CuraEngine package.
Group: Binaries
Requires: CuraEngine-license = %{version}-%{release}

%description bin
bin components for the CuraEngine package.


%package license
Summary: license components for the CuraEngine package.
Group: Default

%description license
license components for the CuraEngine package.


%prep
%setup -q -n CuraEngine-4.11.0
cd %{_builddir}
tar xf %{_sourcedir}/e6afb9cbae4064da8c3e69af3ff5c4629579c1d2.tar.gz
cd %{_builddir}/CuraEngine-4.11.0
mkdir -p stb
cp -r %{_builddir}/stb-e6afb9cbae4064da8c3e69af3ff5c4629579c1d2/* %{_builddir}/CuraEngine-4.11.0/stb

%build
## build_prepend content
sed -i -e s,"DEV","%{version}", src/settings/Settings.h
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1631719967
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake .. -DCURA_ENGINE_VERSION:STRING=%{version} \
-DStb_INCLUDE_DIRS=../
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1631719967
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/CuraEngine
cp %{_builddir}/CuraEngine-4.11.0/LICENSE %{buildroot}/usr/share/package-licenses/CuraEngine/78e50e186b04c8fe1defaa098f1c192181b3d837
cp %{_builddir}/CuraEngine-4.11.0/libs/clipper/License.txt %{buildroot}/usr/share/package-licenses/CuraEngine/061a7c3bb0f292d1578ffdc1960b7b34643241da
cp %{_builddir}/CuraEngine-4.11.0/libs/rapidjson/license.txt %{buildroot}/usr/share/package-licenses/CuraEngine/491e6b20160e05471d747164c4900e5fa5c6520e
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/CuraEngine

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/CuraEngine/061a7c3bb0f292d1578ffdc1960b7b34643241da
/usr/share/package-licenses/CuraEngine/491e6b20160e05471d747164c4900e5fa5c6520e
/usr/share/package-licenses/CuraEngine/78e50e186b04c8fe1defaa098f1c192181b3d837
