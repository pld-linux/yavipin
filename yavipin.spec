
# TODO:
# - add to /etc/modules.conf: alias char-major-10-200 tun
# - check for kernel 2.2 (currently tested on kernel 2.4)
# Warning:
# In case not using --comp we get:
# yavipind: src/comp.c:55: comp_init: Assertion `comp_algoid >= 1 && comp_algoid

Summary:	Secure tunnel using the state of art in network security
Summary(pl):	Bezpieczny tunel u¿ywaj±cy regu³ sztuki bezpieczeñstwa sieciowego
Name:		yavipin
Version:	0.9.6
Release:	0.3
Epoch:		1
License:	Unknown
Group:		Networking/Daemons
Vendor:		Jerome Etienne (jme at off.net)
Source0:	http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tgz
# Source0-md5:	62ea055b362bd331b1ca98ce9953b7a8
URL:		http://yavipin.sourceforge.net/
BuildRequires:	autoconf
#BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	openssl-devel >= 0.9.7
BuildRequires:	zlib-devel
#Requires:	kernel >= 2.4
Requires:	dev >= 2.8.0-29
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
#%%{__aclocal}
#%%{__autoheader}
%{__autoconf}
#%%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

#%%{__make} install DESTDIR=$RPM_BUILD_ROOT #deosn't work - manuall install

install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install src/yavipind $RPM_BUILD_ROOT%{_sbindir}
install src/yavipind.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%attr(754,root,root) /etc/rc.d/init.d/vtund
#%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/sysconfig/vtun
#%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/vtund.conf
%attr(755,root,root) %{_sbindir}/yavipind
%{_mandir}/man*/*
