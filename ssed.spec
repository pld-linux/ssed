Summary:	Super sed
Summary(pl):    Super sed
Name:		ssed
Version:	3.58
Release:	1
License:	GPL
Group:		Applications/Text
#Source0Download:	http://sed.sourceforge.net/grabbag/ssed/testo.htm
Source0:	http://sed.sourceforge.net/grabbag/ssed/sed-%{version}.tar.gz
URL:            http://sed.sourceforge.net/grabbag/ssed/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Provides:	sed
Obsoletes:	sed

%description
ssed is a version of sed that supports a few new features, including
Perl regular expressions and much greater speed than GNU sed.

%description -l pl
ssed (Super Stream EDitor) jest edytorem strumieni lub wsadowym
(nieinteraktywnym) edytorem. Sed pobiera tekst na wej¶ciu, przetwarza
go wed³ug zestawu operacji i oddaje na wyj¶ciu przetworzony tekst.
ssed jest nowa wersja GNU seda zawierajaca nowe opcje i jest szybszy od
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

%find_lang ssed

%clean
rm -rf $RPM_BUILD_ROOT

%files -f ssed.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README README.boot THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_infodir}/sed*
%{_mandir}/man1/*
