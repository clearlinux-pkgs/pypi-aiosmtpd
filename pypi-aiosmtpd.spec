#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-aiosmtpd
Version  : 1.4.2
Release  : 1
URL      : https://files.pythonhosted.org/packages/ff/69/011cee7fe1332f749dac4e65cbc64b3e1a2984d9a7bae9257b1a5e671d01/aiosmtpd-1.4.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/ff/69/011cee7fe1332f749dac4e65cbc64b3e1a2984d9a7bae9257b1a5e671d01/aiosmtpd-1.4.2.tar.gz
Summary  : aiosmtpd - asyncio based SMTP server
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-aiosmtpd-bin = %{version}-%{release}
Requires: pypi-aiosmtpd-python = %{version}-%{release}
Requires: pypi-aiosmtpd-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(atpublic)
BuildRequires : pypi(attrs)
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
aiosmtpd - asyncio based SMTP server
        ######################################
        
        | |github license| |_| |PyPI Version| |PyPI Python|
        | |GA badge| |codecov| |_| |LGTM.com| |readthedocs| |_|
        | |GH Release| |_| |PullRequests| |_| |LastCommit|
        |

%package bin
Summary: bin components for the pypi-aiosmtpd package.
Group: Binaries

%description bin
bin components for the pypi-aiosmtpd package.


%package python
Summary: python components for the pypi-aiosmtpd package.
Group: Default
Requires: pypi-aiosmtpd-python3 = %{version}-%{release}

%description python
python components for the pypi-aiosmtpd package.


%package python3
Summary: python3 components for the pypi-aiosmtpd package.
Group: Default
Requires: python3-core
Provides: pypi(aiosmtpd)
Requires: pypi(atpublic)
Requires: pypi(attrs)

%description python3
python3 components for the pypi-aiosmtpd package.


%prep
%setup -q -n aiosmtpd-1.4.2
cd %{_builddir}/aiosmtpd-1.4.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1651801173
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/aiosmtpd

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
