Summary:	Secure tunnel using the state of art in network security.
Summary(pl):	Bezpieczny tunel.
Name:		yavipin
Version:	0.9.6
Release:	0.1
Epoch:		1
License:	Unknown
Group:		Networking/Daemons
Vendor:		Jerome Etienne (jme at off.net)
Source0:	http://twtelecom.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tgz
URL:		http://yavipin.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake

BuildRequires:	glib-devel
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel


BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Yavipind is a secure tunnel aka 2 peers securely forwarding packets
toward each other. It forwards any kind of packet (IPv4, IPv6 or
other) sent over the virtual point-to-point device (e.g. tun0). It
fully runs in linux userspace.

%description -l pl
Yavipind jest pakietem tworz±cym bezpieczne tunele pomiêdzy dwoma
komputerami. Przesy³a ka¿dy rodzaj pakietów (IPv4, IPv6, inne) poprzez
wirtualne urz±dzenie point-to-point (np. tun0). Pracuje ca³kowicie w
przestrzeni u¿ytkownika.

%prep
%setup -q -n %{name}

%build
#%{__aclocal}
#%{__autoheader}
%{__autoconf}
#%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
