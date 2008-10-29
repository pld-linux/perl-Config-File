# TODO
# - before upgrading to 1.42 figure out WTF means ** UNAUTHORIZED RELEASE ** in CPAN for this pkg?
#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Config
%define		pnam	File
Summary:	Config-File - Parse a simple configuration file
Name:		perl-Config-File
Version:	1.41
Release:	0.1
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Config/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0a01e87cf799ca24cab941b18ef24514
URL:		http://search.cpan.org/dist/Config-File/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
read_config_file parses a simple configuration file and stores its
values in an anonymous hash reference.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{perl_vendorlib}/ConfigFile.pm
rm $RPM_BUILD_ROOT%{_mandir}/man3/ConfigFile.3pm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Config/File.pm
%{_mandir}/man3/*
