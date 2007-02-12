Summary:	Super sed - version of sed with a few new features
Summary(pl.UTF-8):	Super sed - wersja seda z kilkoma nowymi możliwościami
Name:		ssed
Version:	3.62
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://sed.sourceforge.net/grabbag/ssed/sed-%{version}.tar.gz
# Source0-md5:	8f35882af95da4e5ddbf3de1add26f79
URL:		http://sed.sourceforge.net/grabbag/ssed/
Provides:	sed
Obsoletes:	sed
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ssed is a version of sed that supports a few new features, including
Perl regular expressions and much greater speed than GNU sed.

%description -l pl.UTF-8
ssed (Super Stream EDitor) jest edytorem strumieni lub wsadowym
(nieinteraktywnym) edytorem. Sed pobiera tekst na wejściu, przetwarza
go według zestawu operacji i oddaje na wyjściu przetworzony tekst.
ssed jest nową wersją GNU seda zawierającą nowe opcje i szybszą od
GNU seda.

%prep
%setup -q -n sed-%{version}

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f ssed.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README README.boot THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_infodir}/sed*
%{_mandir}/man1/*
