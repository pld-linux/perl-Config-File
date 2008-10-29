%include	/usr/lib/rpm/macros.perl
Summary:	Config-File - Parse a simple configuration file
Name:		perl-Config-File
Version:	1.42
Release:	1
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/G/GW/GWOLF/Config-File-%{version}.tar.gz
# Source0-md5:	7e80687e56478c22f13b56932ef213f8
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Config-File - Parse a simple configuration file

%prep
%setup -q -n Config-File-%{version}

%build
touch Makefile.PL
%{__perl} -MExtUtils::MakeMaker -e 'WriteMakefile(NAME=>"ConfigReader::Spec");' \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/ConfigFile.pm
%dir %{perl_vendorlib}/Config
%{perl_vendorlib}/Config/File.pm
%{_mandir}/man3/*
