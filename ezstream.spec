Summary:	Command-line source client for Icecast media streaming servers
Summary(pl.UTF-8):	Klient źródłowy dla serwerów strumieni multimedialnych Icecast
Name:		ezstream
Version:	1.0.2
Release:	1
License:	GPL v2
Group:		Applications/Multimedia
Source0:	https://downloads.xiph.org/releases/ezstream/%{name}-%{version}.tar.gz
# Source0-md5:	247867e7c1e3c349aa9c7af79e666d4d
URL:		https://www.icecast.org/ezstream/
BuildRequires:	libshout-devel >= 2.2
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRequires:	taglib-devel >= 1.4
Requires:	libshout >= 2.2
Requires:	taglib >= 1.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The ezstream utility is command-line source client for the Icecast
media streaming server.

%description -l pl.UTF-8
ezstream to obsługiwany z linii poleceń klient źródłowy dla serwerów
strumieni multimedialnych Icecast.

%prep
%setup -q

# strip GPL text
%{__sed} -i -e '12,$d' COPYING

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/ezstream
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/examples
%{__rm} examples/Makefile*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog NEWS README.md examples
%attr(755,root,root) %{_bindir}/ezstream
%attr(755,root,root) %{_bindir}/ezstream-cfgmigrate
%attr(755,root,root) %{_bindir}/ezstream-file.sh
%{_mandir}/man1/ezstream.1*
%{_mandir}/man1/ezstream-cfgmigrate.1*
%{_mandir}/man1/ezstream-file.sh.1*
