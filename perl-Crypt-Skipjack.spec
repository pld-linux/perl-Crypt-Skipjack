#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Crypt
%define	pnam	Skipjack
Summary:	Crypt::Skipjack - Crypt::CBC-compliant block cipher
Summary(pl):	Crypt::Skipjack - szyfr blokowy kompatybilny z Crypt::CBC
Name:		perl-Crypt-Skipjack
Version:	1.0.2
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	46196172e7020917f8249f36f8b55c21
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Skipjack is the secret key encryption algorithm designed by the
National Security Agency, and is used in the Clipper chip and Fortezza
PC card. It was implemented in tamper-resistant hardware and its
structure had been classified since its introduction in 1993. Skipjack
was unclassified on June 24, 1998. Skipjack is an 80-bit key, 64-bit
block cipher. This module supports the Crypt::CBC interface.

%description -l pl
Skipjack to algorytm szyfrowania klucza tajnego opracowany przez NSA
(National Security Agency), u¿ywany w uk³adzie Clipper i kartach PC
Fortezza. By³ zaimplementowany w zabezpieczonym przed intruzami
sprzêcie, a jego struktura by³a zastrze¿ona od wprowadzenia w 1993
roku do 24 czerwca 1998. Skipjack to 64-bitowy szyfr blokowy z
80-bitowym kluczem. Ten modu³ obs³uguje interfejs Crypt::CBC.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cd examples
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
for f in * ; do
	sed -e "s@#!/usr/local/bin/perl@#!/usr/bin/perl@" $f \
		> $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/$f
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Crypt/Skipjack.pm
%dir %{perl_vendorarch}/auto/Crypt/Skipjack
%{perl_vendorarch}/auto/Crypt/Skipjack/Skipjack.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/Skipjack/Skipjack.so
%{_mandir}/man3/*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}
