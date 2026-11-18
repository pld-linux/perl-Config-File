# TODO
# - before upgrading to 1.42 figure out WTF means ** UNAUTHORIZED RELEASE ** in CPAN for this pkg?
#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Config
%define		pnam	File
Summary:	Config-File - Parse a simple configuration file
Name:		perl-Config-File
Version:	1.54
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/authors/id/T/TH/THESEAL/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	cb43558413d78a7b868dd91d9837a3f8
URL:		http://search.cpan.org/dist/Config-File/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Pod
BuildRequires:	perl-Test-Pod-Coverage
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
read_config_file parses a simple configuration file and stores its
values in an anonymous hash reference.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{perl_vendorlib}/Config/*.pm
%{_mandir}/man3/*
