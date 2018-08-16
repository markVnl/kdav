Summary: Kopano Sabre-DAV integration
Name:    kdav
Version: 0.0.0
Release: 0.1%{?dist}
License: AGPL
URL:     https://stash.kopano.io/projects/KC/repos/kdav
Source0: https://github.com/markVnl/kdav/archive/%{version}.tar.gz
Source1: kdav.conf
Source2: kdav.lr
Patch0:  config_uri.patch
BuildArch: noarch

Requires: kopano-server
Requires: rh-php71-php-fpm, rh-php71-php-mbstring

%description
Sabre-DAV implementation for Kopano

%prep
%setup -q
%patch0 -p1

%build


%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_datarootdir}/kdav
cp -a *  %{buildroot}%{_datarootdir}/kdav/
rm -rf   %{buildroot}%{_datarootdir}/kdav/{centos,tests,composer.*,LICENSE,README.md,TRADEMARKS}

mkdir -p %{buildroot}/%{_sysconfdir}/kopano/kdav
mv %{buildroot}/%{_datarootdir}/kdav/config.php %{buildroot}/%{_sysconfdir}/kopano/kdav
ln -s "%{_sysconfdir}/kopano/kdav/config.php" %{buildroot}/%{_datarootdir}/kdav/config.php

mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d
install -m 0664 %{SOURCE1} %{buildroot}%{_sysconfdir}/httpd/conf.d/
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
install -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/kdav

# install dirs
install -d -m 0750 %{buildroot}%{_sharedstatedir}/kopano/kdav
install -d -m 0750 %{buildroot}%{_localstatedir}/log/kdav

%clean
rm -rf %{buildroot}

%files
%doc LICENSE 
%defattr(-,root,root)
%{_datarootdir}/kdav
%config(noreplace) %{_sysconfdir}/httpd/conf.d/kdav.conf
%dir %{_sysconfdir}/kopano/kdav
%config(noreplace) %{_sysconfdir}/kopano/kdav/config.php
%{_sysconfdir}/logrotate.d/kdav
%attr(0750,kopano,apache) %dir %{_sharedstatedir}/kopano/kdav
%attr(0750,apache,apache) %dir %{_localstatedir}/log/kdav

