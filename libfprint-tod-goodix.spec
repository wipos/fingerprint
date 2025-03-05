Name:           libfprint-tod-goodix
Version:        0.0.6
Release:        1%{?dist}
Summary:        Goodix driver module for fingerprint reader to support 0x27C6 0x533C, 0x27C6 0x538C, 0x27C6 0x530C and 0x27C6 0x5840.

License:        GPL-3.0
Source0:        http://dell.archive.canonical.com/updates/pool/public/libf/libfprint-2-tod1-goodix/libfprint-2-tod1-goodix_%{version}.orig.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:       libfprint-tod

%global debug_package %{nil}

%description
Goodix driver module for fingerprint reader to support 0x27C6 0x533C, 0x27C6 0x538C, 0x27C6 0x530C and 0x27C6 0x5840.


%prep
%setup -q -n libfprint-2-tod1-goodix-%{version}


%build
# empty


%install
install -p -d -m 0755 %{buildroot}/%{_libdir}/libfprint-2/tod-1/
install -m 0644 usr/lib/x86_64-linux-gnu/libfprint-2/tod-1/libfprint-tod-goodix-53xc-%{version}.so %{buildroot}/%{_libdir}/libfprint-2/tod-1/


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_libdir}/libfprint-2/tod-1/libfprint-tod-goodix-53xc-%{version}.so

%changelog

* Repackage for WIPOS
