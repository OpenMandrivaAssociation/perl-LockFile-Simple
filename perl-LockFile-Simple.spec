%define	upstream_name	 LockFile-Simple
%define upstream_version 0.208
Name:		perl-%{upstream_name}
Version:	0.208
Release:	1

Summary:	The LockFile::Simple extension provides simple file locking
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/LockFile-Simple
Source0:	https://cpan.metacpan.org/authors/id/S/SC/SCHWIGON/lockfile-simple/LockFile-Simple-0.208.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description 
The LockFile::Simple extension provides simple file locking, of the
advisory kind, i.e. it requires cooperation between applications wishing
to lock the same files.

It is meant to be used in quick-and-dirty scripts or more elaborated
programs that want a simple locking scheme, yet with a reasonable
level of configuration.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make
make test

%install
%makeinstall_std

%files
%defattr(444,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/LockFile/*.pm
%{perl_vendorlib}/LockFile/Lock/*
%{_mandir}/*/*

