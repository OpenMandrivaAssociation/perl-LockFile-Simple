%define	upstream_name	 LockFile-Simple
%define	upstream_version 0.207

Name: 		perl-%{upstream_name}
Version: 	%perl_convert_version %{upstream_version}
Release: 	%mkrel 1

Summary: 	simple file locking scheme
License: 	GPL+ or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}/
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/LockFile/%{upstream_name}-%{upstream_version}.tar.gz


BuildArch: noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description 
The LockFile::Simple extension provides simple file locking, of the
advisory kind, i.e. it requires cooperation between applications wishing
to lock the same files.

It is meant to be used in quick-and-dirty scripts or more elaborated
programs that want a simple locking scheme, yet with a reasonable
level of configuration.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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

