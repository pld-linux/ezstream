Summary:	Command-line source client for Icecast media streaming servers
Summary(pl.UTF-8):	Klient źródłowy dla serwerów strumieni multimedialnych Icecast
Name:		ezstream
Version:	0.5.2
Release:	1
License:	GPL v2
Group:		Applications/Multimedia
Source0:	http://downloads.xiph.org/releases/ezstream/%{name}-%{version}.tar.gz
# Source0-md5:	5f608530cdd9748f7556b5b1e0b77d85
URL:		http://www.icecast.org/ezstream.php
BuildRequires:	libogg-devel >= 2:1.0
BuildRequires:	libshout-devel >= 2.2
BuildRequires:	libvorbis-devel >= 1:1.0
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	taglib-devel >= 1.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The ezstream utility is command-line source client for the Icecast
media streaming server.

%description -l pl.UTF-8
ezstream to obsługiwany z linii poleceń klient źródłowy dla serwerów
strumieni multimedialnych Icecast.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/ezstream
%{_mandir}/man1/ezstream.1*
