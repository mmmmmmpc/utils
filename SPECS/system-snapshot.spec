Name:		system-snapshot
Version:	0.2
Release:	1
Summary:	System-Snapshot is an utility to enable a system rollback at filesystem level.

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
System-Snapshot is an utility to enable a system rollback at filesystem level.
It performs a /boot backup and creates filesystem snapshots using the provided configuration.
It assumes a system partitioning using LVM volumes for everything except /boot.
The default configuration requires the volumes to be snapshotted to be included in order to be functional.  

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
gzip -9 $RPM_BUILD_ROOT/usr/share/man/man8/system-snapshot.8

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
* Tue Oct 29 2013 Miguel Perez <mperez@redhat.com> 0.2-1
- Bumped release

* Thu May 23 2013 Miguel Perez <mperez@redhat.com> 0.1
- Initial release
- Added manpages
- Substituted system dirs for its macros counterparts

