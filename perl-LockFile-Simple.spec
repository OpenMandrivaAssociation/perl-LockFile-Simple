%define	module	LockFile-Simple
%define	version	0.2.5
%define	release	%mkrel 6
%define	pdir	LockFile

Summary: 	%{module} module for perl
Name: 		perl-%{module}
Version: 	%{version}
Release: 	%{release}
License: 	GPL or Artistic
Group:		Development/Perl
Source0:	%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/search?dist=%{module}
BuildArch: 	noarch
Requires:	perl , perl-base 
BuildRequires:	perl-devel

%description 
%{module} module for perl.  The LockFile::Simple extension 
provides simple file locking, of the advisory kind, i.e. it requires
cooperation between applications wishing to lock the same files.

It is meant to be used in quick-and-dirty scripts or more elaborated
programs that want a simple locking scheme, yet with a reasonable
level of configuration.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(444,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/LockFile/*.pm
%{perl_vendorlib}/LockFile/Lock/*
%{_mandir}/*/*

