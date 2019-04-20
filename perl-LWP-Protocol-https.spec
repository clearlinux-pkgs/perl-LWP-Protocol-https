#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-LWP-Protocol-https
Version  : 6.07
Release  : 27
URL      : https://cpan.metacpan.org/authors/id/O/OA/OALDERS/LWP-Protocol-https-6.07.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/O/OA/OALDERS/LWP-Protocol-https-6.07.tar.gz
Summary  : 'Provide https support for LWP::UserAgent'
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan
BuildRequires : perl(Encode::Locale)
BuildRequires : perl(HTML::HeadParser)
BuildRequires : perl(HTTP::Date)
BuildRequires : perl(HTTP::Request)
BuildRequires : perl(IO::Socket::SSL)
BuildRequires : perl(LWP::UserAgent)
BuildRequires : perl(Mozilla::CA)
BuildRequires : perl(Net::HTTPS)
BuildRequires : perl(Net::SSL)
BuildRequires : perl(Net::SSLeay)
BuildRequires : perl(Test::RequiresInternet)
BuildRequires : perl(Try::Tiny)
BuildRequires : perl(URI)

%description
######################################################################
LWP::Protocol::https 6.06
######################################################################

%package dev
Summary: dev components for the perl-LWP-Protocol-https package.
Group: Development
Provides: perl-LWP-Protocol-https-devel = %{version}-%{release}

%description dev
dev components for the perl-LWP-Protocol-https package.


%prep
%setup -q -n LWP-Protocol-https-6.07

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
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
/usr/lib/perl5/vendor_perl/5.28.2/LWP/Protocol/https.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/LWP::Protocol::https.3
