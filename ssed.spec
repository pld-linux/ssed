Name:		ssed
Summary:	super sed
Summary(pl):    super sed
Version:	3.57a
Release:	2
License:	GPL
Group:		Text tools 
Source0:	http://spazioweb.inwind.it/seders/ssed/sed-%{version}.tar.gz
URL:            http://spazioweb.inwind.it/seders/ssed/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Provides:	sed
Obsoletes:	sed

%description
ssed is a version of sed that supports a few new features, including
Perl regular expressions and much greater speed than GNU sed.

%description -l pl

ssed (Super Stream EDitor) jest edytorem strumieni lub wsadowym
(nieinteraktywnym) edytorem. Sed pobiera tekst na wej�ciu, przetwarza
go wed�ug zestawu operacji i oddaje na wyj�ciu przetworzony tekst.
ssed jest nowa wersja GNU seda zawierajaca nowe opcje i jest szybszy od
GNU seda.


%prep
%setup -q -n sed-%{version}

%build
%configure 

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT


gzip -9nf  ABOUT-NLS AUTHORS BUGS  ChangeLog NEWS README README.boot THANKS TODO \
	   $RPM_BUILD_ROOT/%{_infodir}/sed*
%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_infodir}/sed*.gz
%{_mandir}/man1/*
%{_datadir}/locale/*/LC_MESSAGES/*