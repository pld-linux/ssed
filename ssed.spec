Name:		ssed
Summary:	super sed
Summary(pl):    super sed
Version:	3.57a
Release:	1
License:	GPL
Group:		Text tools 
Source0:	http://spazioweb.inwind.it/seders/ssed/sed-%{version}.tar.gz
URL:            http://spazioweb.inwind.it/seders/ssed/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ssed is a version of sed that supports a few new features, including
Perl regular expressions and much greater speed than GNU sed.

%prep
%setup -q -n sed-%{version}

%build
%configure 
#	--enable-html \  
#	   --enable-pcregrep

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%__mv $RPM_BUILD_ROOT%{_bindir}/sed $RPM_BUILD_ROOT%{_bindir}/ssed

for i in `find $RPM_BUILD_ROOT/%{_mandir}/man1/  -type f`
do
  j=`echo $i | %__sed "s/sed\.\([0-9]\)/ssed.\1/g"` ;
  if [ "$i" != "$j" ]; then %__mv $i $j ; fi ;
done

for i in `find $RPM_BUILD_ROOT/%{_infodir} -type f`
do
 j=`echo $i | %__sed "s/sed\./ssed.\1/g"` ;
 if [ "$i" != "$j" ]; then %__mv $i $j ; fi ;
done

for i in `find $RPM_BUILD_ROOT/%{_datadir}/locale/ -type f`
do
  j=`echo $i | %__sed "s/sed\.mo/ssed.mo/g"`;	
  if [ "$i" != "$j" ]; then %__mv $i $j ; fi;	
done

gzip -9nf  ABOUT-NLS AUTHORS BUGS  ChangeLog NEWS README README.boot THANKS TODO \
	   $RPM_BUILD_ROOT/%{_infodir}/ssed*
%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_infodir}/ssed*.gz
%{_mandir}/man1/*
%{_datadir}/locale/*/LC_MESSAGES/*
