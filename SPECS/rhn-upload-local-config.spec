Name:		rhn-upload-local-config
Version:	0.1
Release:	1
Summary:	Utility to upload files as local config files to a channel in Satellite.

Group:		System Environment/Tools
License:	GPL
Source0:	%{name}-%{version}.tar.gz
URL:		https://github.com/mperezco/utils
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

BuildRequires:	/bin/tar
Requires:	python
Provides:	rhn-upload-local-config

# disable debug packages and the stripping of the binaries
%global _enable_debug_package 0
%global debug_package %{nil}

%description
Utility to upload files as local config files to a channel in Satellite.

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

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post

%preun

%files
%defattr(-,root,root,-)
%attr(0755,root,root) %{_bindir}/rhn-upload-local-config


%changelog
* Thu Nov 07 2013 Miguel Perez <mperez@redhat.com> 0.1-1
- Initial release

