Summary: nethserver-traefik  install traefik
%define name nethserver-traefik
Name: %{name}
%define version 0.1.0
%define release 1
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Requires: nethserver-portainer
BuildRequires: nethserver-devtools
BuildArch: noarch

%description
Træfik is a modern HTTP reverse proxy and load balancer made to deploy microservices with ease.
It supports several backends (Docker, Swarm mode, Kubernetes, Marathon, Consul, Etcd, Rancher, 
Amazon ECS, and a lot more) to manage its configuration automatically and dynamically.

%changelog
* Thu Apr 05 2018 stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.0
- initial

%prep
%setup

%build
%{makedocs}
perl createlinks
mkdir -p root/etc/traefik

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-%{release}-filelist
%{genfilelist} $RPM_BUILD_ROOT \
> %{name}-%{version}-%{release}-filelist

%post
%postun

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update
%doc COPYING
