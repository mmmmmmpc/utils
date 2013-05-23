Name:		system-snapshot
Version:	0.1
Release:	1
Summary:	Util to create merge or discard filesystem snapshots

Group:		System Environment/Tools
License:	GPL
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

BuildRequires:	/bin/tar
Requires:	bash
Provides:	system-snapshot

# disable debug packages and the stripping of the binaries
%global _enable_debug_package 0
%global debug_package %{nil}

%description
Util to create merge or discard filesystem snapshots

%prep
%setup -q 

%build

%install
# Clean the buildroot
rm -rf $RPM_BUILD_ROOT

# Create the buildroot
mkdir -p $RPM_BUILD_ROOT

# Copy package files
mkdir -p $RPM_BUILD_ROOT
cp -arfv * $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post

%preun

%files
%defattr(-,root,root,-)
%config(noreplace) %attr(0640,root,root) %{_sysconfdir}/sysconfig/system-snapshot
%attr(0750,root,root) %{_sbindir}/system-snapshot
%attr(0644,root,root) %{_mandir}/man8/system-snapshot.8.gz

%changelog
* Thu May 23 2013 Miguel Perez <mperez@redhat.com>
- Initial release
- Added manpages
- Substituted system dirs for its macros counterparts

