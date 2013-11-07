Name:		system-snapshot
Version:	0.3
Release:	3
Summary:	System-Snapshot is an utility to enable a system rollback at filesystem level.

Group:		System Environment/Tools
License:	GPL
Source0:	%{name}-%{version}.tar.gz
URL:		https://github.com/mperezco/utils
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

BuildRequires:	/bin/tar
Requires:	bash, rsync
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
cp -arfv * $RPM_BUILD_ROOT
gzip -9 $RPM_BUILD_ROOT/usr/share/man/man8/system-snapshot.8
mkdir -p $RPM_BUILD_ROOT/var/system-snapshot

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
%dir %{_localstatedir}/system-snapshot


%changelog
* Thu Nov 07 2013 Miguel Perez <mperez@redhat.com> 0.3-3
- Updated to commit e5138c6564d7b704e5785d9aba5cd20db6ff94e0

* Tue Nov 05 2013 Miguel Perez <mperez@redhat.com> 0.3-2
- Updated to commit 2249a6d172f082d94b561ee0a1b9c64e83bf7bf6
- Includes free space checking in VGs and backup dir

* Tue Nov 05 2013 Miguel Perez <mperez@redhat.com> 0.3-1
- Bumped release

* Tue Nov 05 2013 Miguel Perez <mperez@redhat.com> 0.2-2
- Added new default dir to avoid tmpwatch cleanup
- Updated sources

* Tue Oct 29 2013 Miguel Perez <mperez@redhat.com> 0.2-1
- Bumped release

* Thu May 23 2013 Miguel Perez <mperez@redhat.com> 0.1
- Initial release
- Added manpages
- Substituted system dirs for its macros counterparts

