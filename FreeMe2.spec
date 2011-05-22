Summary:	Remove wm-drm protection from wmv/asf/wma files
Name:		FreeMe2
Version:	0.4
Release:	1
License:	GPL v3
Group:		Applications/Multimedia
Source0:	http://downloads.sourceforge.net/freeme2/%{name}_src-%{version}.tgz
# Source0-md5:	c12175638e1bf238d9bd41de6fc91942
URL:		http://sourceforge.net/projects/freeme2
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Freeme2 is a program based on famous freeme app created by Beale
Screamer and based on viodentias findings. It strips wm-drm protection
from wmv/asf/wma files as well as video/audio streams.

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
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
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/FreeMe2
