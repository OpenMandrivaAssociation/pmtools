Summary:	Tools for examining kernel ACPI tables	
Name:		pmtools
Version:	20071116
Release:	%mkrel 1
License:	GPL
Group:		Development/Kernel		

Source:		http://www.lesswatts.org/patches/linux_acpi//%{name}-%{version}.tar.bz2		
Url:		http://www.lesswatts.org
BuildRoot:	%_tmppath/%name-%version-root

%description
This is a small collection of power management test and
investigation tools.  See http://acpi.sourceforge.net
for more information on ACPI for Linux.

%prep
%setup -q

%build
%make
%make -C madt

%install
mv madt/README madt/README.madt
install -d %buildroot%{_sbindir}
install madt/madt %buildroot%{_sbindir}
install acpidump/acpidump %buildroot%{_sbindir}
install acpidump/acpitbl %buildroot%{_sbindir}
install acpixtract/acpixtract %buildroot%{_sbindir}

%clean
rm -fr %buildroot

%files
%defattr(-,root,root)
%doc README COPYING madt/README.madt
%{_sbindir}/madt
%{_sbindir}/acpidump
%{_sbindir}/acpitbl
%{_sbindir}/acpixtract


