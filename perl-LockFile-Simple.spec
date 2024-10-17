%define	upstream_name	 LockFile-Simple
%define upstream_version 0.208

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.208
Release:	3

Summary:	The LockFile::Simple extension provides simple file locking
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/LockFile/LockFile-Simple-0.208.tar.gz

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
%setup -q -n %{upstream_name}-%{upstream_version}

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

%changelog
* Tue Jul 07 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.207.0-1mdv2010.0
+ Revision: 393281
- update to 0.207
- using %%perl_convert_version
- fixed summary, license & description fields
- using plain url for source0

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.2.5-8mdv2009.0
+ Revision: 241612
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Aug 20 2007 Thierry Vignaud <tv@mandriva.org> 0.2.5-6mdv2008.0
+ Revision: 67618
- use %%mkrel


* Thu Sep 23 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.2.5-6mdk
- 0.2.5

* Thu Aug 14 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.2.5-5mdk
- rebuild for new perl
- drop $RPM_OPT_FLAGS, noarch..
- use %%makeinstall_std macro

* Wed May 28 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.2.5-4mdk
- rebuild for new auto{prov,req}

* Sat Feb 01 2003 Lenny Cartier <lenny@mandrakesoft.com 0.2.5-3mdk
- rebuild

* Wed Jul 31 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.2.5-2mdk
- rebuild with new perl

* Mon Jun 17 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.2.5-1mdk
- from Peter Chen <petechen@netilla.com> :
	- 0.2.5


