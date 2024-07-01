#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v13
# autospec commit: dc0ff31b4314
#
Name     : perl-LWP-Protocol-https
Version  : 6.14
Release  : 52
URL      : https://cpan.metacpan.org/authors/id/O/OA/OALDERS/LWP-Protocol-https-6.14.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/O/OA/OALDERS/LWP-Protocol-https-6.14.tar.gz
Summary  : 'Provide https support for LWP::UserAgent'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-LWP-Protocol-https-license = %{version}-%{release}
Requires: perl-LWP-Protocol-https-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Encode::Locale)
BuildRequires : perl(IO::Socket::SSL)
BuildRequires : perl(IO::Socket::SSL::Utils)
BuildRequires : perl(LWP::Protocol::http)
BuildRequires : perl(LWP::UserAgent)
BuildRequires : perl(Net::HTTPS)
BuildRequires : perl(Test::Needs)
BuildRequires : perl(Test::RequiresInternet)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package dev
Summary: dev components for the perl-LWP-Protocol-https package.
Group: Development
Provides: perl-LWP-Protocol-https-devel = %{version}-%{release}
Requires: perl-LWP-Protocol-https = %{version}-%{release}

%description dev
dev components for the perl-LWP-Protocol-https package.


%package license
Summary: license components for the perl-LWP-Protocol-https package.
Group: Default

%description license
license components for the perl-LWP-Protocol-https package.


%package perl
Summary: perl components for the perl-LWP-Protocol-https package.
Group: Default
Requires: perl-LWP-Protocol-https = %{version}-%{release}

%description perl
perl components for the perl-LWP-Protocol-https package.


%prep
%setup -q -n LWP-Protocol-https-6.14
cd %{_builddir}/LWP-Protocol-https-6.14

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-LWP-Protocol-https
cp %{_builddir}/LWP-Protocol-https-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-LWP-Protocol-https/569ee72f3d4d71fe8a66726859393611b73b5ba5 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/LWP::Protocol::https.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-LWP-Protocol-https/569ee72f3d4d71fe8a66726859393611b73b5ba5

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
